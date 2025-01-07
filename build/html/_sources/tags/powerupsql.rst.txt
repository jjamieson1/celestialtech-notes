PowerUpSQL
##############

Date: 2025-01-04 15:48:56

Status: #new 

Tags: :ref:`mssql clients`


Description
******************
Scott Sutherland (@nullbind) from NetSPI has authored PowerUpSQL, a PowerShell Toolkit for Attacking SQL Server. Major contributors include Antti Rantasaari, Eric Gruber (@egru), and Thomas Elling (@thomaselling). Before executing any of the below commands, download PowerUpSQL and load it into your PowerShell instance. Get PowerUpSQL here:

Installation
***************

.. code-block:: powershell

    PS C:\htb> git clone https://github.com/NetSPI/PowerUpSQL 
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




References
**************
PowerupSQL cheat sheet https://github.com/NetSPI/PowerUpSQL/wiki/PowerUpSQL-Cheat-Sheet