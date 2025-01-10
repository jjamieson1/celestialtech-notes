Enumerating and Retrieving Password Policies
##############################################

Date: 2024-12-20 11:00:19

Status: #new

Tags: :ref:`active directory enumeration attacks`

----

Description
*************

If the client does not provide the password policy, or if this is a 
grey/black box pentest, there are other means to retrieve the Password
policy by using tools such as:

1. :ref:`crackmapexec`
2. :ref:`rpcclient`

Examples from Linux tools
**************************

Using :ref:`crackmapexec`
===========================

By using a known username/password

.. code-block:: bash

    crackmapexec smb 172.16.5.5 -u avazquez -p Password123 --pass-pol

--pass-pol option will return the policy


Using :ref:`rpcclient` 
========================

using rpcclient to check for :ref:`smb` NULL session access with no 
known username/password. 

.. code-block:: bash

    rpcclient -U "" -N 172.16.5.5
    rpcclient $> querydominfo
    Domain:		INLANEFREIGHT
    Server:		
    Comment:	
    Total Users:	3650
    Total Groups:	0
    Total Aliases:	37
    Sequence No:	1
    Force Logoff:	-1
    Domain Server State:	0x1
    Server Role:	ROLE_DOMAIN_PDC
    Unknown 3:	0x1

    rpcclient $> getdompwinfo
    min_password_length: 8
    password_properties: 0x00000001
        DOMAIN_PASSWORD_COMPLEX


Using :ref:`enum4linux-ng` 
=============================

.. note:: See :ref:`enum4linux-ng` for installation and other uses. 

.. code-block:: bash

    enum4linux-ng -P 172.16.5.5 -oA ilfreight

This creates a file with the domain information if successful. 

Using :ref:`ldapsearch` anonymous bind
========================================

This is a legacy configuration, modern systems require authentication (post Windows Server 2003)

Example using :ref:`ldapsearch`
-----------------------------------

.. code-block:: console

    ldapsearch -h 172.16.5.5 -x -b "DC=INLANEFREIGHT,DC=LOCAL" -s sub "*" | grep -m 1 -B 10 pwdHistoryLength


Enumeration NULL Session from Windows
****************************************

Example: Establish a null session from Windows

.. code-block:: powershell

    C:\htb> net use \\DC01\ipc$ "" /u:""
    The command completed successfully.

We can also use a username/password to attempt to connect.

Common errors when connecting
================================

error: account disabled

.. code-block:: console

    C:\htb> net use \\DC01\ipc$ "" /u:guest
    System error 1331 has occurred.

    This user can't sign in because this account is currently disabled.

error: password incorrect

.. code-block:: console

     C:\htb> net use \\DC01\ipc$ "password" /u:guest
    System error 1326 has occurred.

    The user name or password is incorrect.

error: Account is locked out (password policy)

.. code-block:: console

     C:\htb> net use \\DC01\ipc$ "password" /u:guest
    System error 1909 has occurred.

    The referenced account is currently locked out and may not be logged on to.

Enumerating Password policy from windows
*******************************************

Example: using net.exe 

.. code-block:: console

    C:\htb> net accounts

    Force user logoff how long after time expires?:       Never
    Minimum password age (days):                          1
    Maximum password age (days):                          Unlimited
    Minimum password length:                              8
    Length of password history maintained:                24
    Lockout threshold:                                    5
    Lockout duration (minutes):                           30
    Lockout observation window (minutes):                 30
    Computer role:                                        SERVER
    The command completed successfully.

This policy is ideal for :ref:`password spraying`.  The eight charr minimum means we can try weak passwords.  We 
can try up to 4 attempts, without locking an account, and the reset lasts 30 minutes. 

Example: using :ref:`powerview` 

.. code-block:: powershell

    PS C:\htb> import-module .\PowerView.ps1
    PS C:\htb> Get-DomainPolicy

    Unicode        : @{Unicode=yes}
    SystemAccess   : @{MinimumPasswordAge=1; MaximumPasswordAge=-1; MinimumPasswordLength=8; PasswordComplexity=1;
                    PasswordHistorySize=24; LockoutBadCount=5; ResetLockoutCount=30; LockoutDuration=30;
                    RequireLogonToChangePassword=0; ForceLogoffWhenHourExpire=0; ClearTextPassword=0;
                    LSAAnonymousNameLookup=0}
    KerberosPolicy : @{MaxTicketAge=10; MaxRenewAge=7; MaxServiceAge=600; MaxClockSkew=5; TicketValidateClient=1}
    Version        : @{signature="$CHICAGO$"; Revision=1}
    RegistryValues : @{MACHINE\System\CurrentControlSet\Control\Lsa\NoLMHash=System.Object[]}
    Path           : \\INLANEFREIGHT.LOCAL\sysvol\INLANEFREIGHT.LOCAL\Policies\{31B2F340-016D-11D2-945F-00C04FB984F9}\MACHI
                    NE\Microsoft\Windows NT\SecEdit\GptTmpl.inf
    GPOName        : {31B2F340-016D-11D2-945F-00C04FB984F9}
    GPODisplayName : Default Domain Policy

This command versus net.exe is that it yields the password complexity requirement 

.. note:: Password complexity is enabled, meaning that a user must choose a password with 3/4 of the following: an uppercase letter, lowercase letter, number, special character (Password1 or Welcome1 would satisfy the "complexity" requirement here, but are still clearly weak passwords).

.. note:: The selection of a tool to use in any engagement is dependant on the rules of engagement.  (stealthy, EDR, anti-virus and potential restrictions on the host)


References
************

https://academy.hackthebox.com/module/143/section/1490