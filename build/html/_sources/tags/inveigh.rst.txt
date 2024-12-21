inveigh
########

Date: 2024-12-20 08:21:28

Tags: :ref:`active directory enumeration attacks`

Status: #new

Description
********************

Inveigh is a cross-platform .NET IPv4/IPv6 machine-in-the-middle tool for penetration testers. 
This repo contains the primary C# version as well as the legacy PowerShell version.

Installation
************

Start by cloning the repo

.. code-block:: console

    git clone https://github.com/Kevin-Robertson/Inveigh

The powershell version is included in the root of the project.  
The binary version must be compiled.  Please see the official repository for compile options and instructions.


Usage
******

Powershell version (no longer maintained)
===========================================

import the module 

.. code-block:: powershell

    PS C:\htb> Import-Module .\Inveigh.ps1
    PS C:\htb> (Get-Command Invoke-Inveigh).Parameters

Start the capture with 

.. code-block:: powershell

    PS C:\htb> Invoke-Inveigh Y -NBNS Y -ConsoleOutput Y -FileOutput Y

C# version
=============

.. code-block:: powershell

    PS C:\htb> .\Inveigh.exe

This utility is interactive, drop to its shell with esc. 

.. code-block:: powershell

    help

    =============================================== Inveigh Console Commands ===============================================

    Command                           Description
    ========================================================================================================================
    GET CONSOLE                     | get queued console output
    GET DHCPv6Leases                | get DHCPv6 assigned IPv6 addresses
    GET LOG                         | get log entries; add search string to filter results
    GET NTLMV1                      | get captured NTLMv1 hashes; add search string to filter results
    GET NTLMV2                      | get captured NTLMv2 hashes; add search string to filter results
    GET NTLMV1UNIQUE                | get one captured NTLMv1 hash per user; add search string to filter results
    GET NTLMV2UNIQUE                | get one captured NTLMv2 hash per user; add search string to filter results
    GET NTLMV1USERNAMES             | get usernames and source IPs/hostnames for captured NTLMv1 hashes
    GET NTLMV2USERNAMES             | get usernames and source IPs/hostnames for captured NTLMv2 hashes
    GET CLEARTEXT                   | get captured cleartext credentials
    GET CLEARTEXTUNIQUE             | get unique captured cleartext credentials
    GET REPLYTODOMAINS              | get ReplyToDomains parameter startup values
    GET REPLYTOHOSTS                | get ReplyToHosts parameter startup values
    GET REPLYTOIPS                  | get ReplyToIPs parameter startup values
    GET REPLYTOMACS                 | get ReplyToMACs parameter startup values
    GET IGNOREDOMAINS               | get IgnoreDomains parameter startup values
    GET IGNOREHOSTS                 | get IgnoreHosts parameter startup values
    GET IGNOREIPS                   | get IgnoreIPs parameter startup values
    GET IGNOREMACS                  | get IgnoreMACs parameter startup values
    SET CONSOLE                     | set Console parameter value
    HISTORY                         | get command history
    RESUME                          | resume real time console output
    STOP                            | stop Inveigh


References
***********
https://github.com/Kevin-Robertson/Inveigh/wiki/Parameters
https://academy.hackthebox.com/module/143/section/1420
https://github.com/Kevin-Robertson/Inveigh