Shells and Payloads
#####################

Date: 2024-11-17 14:43

Status:

:ref:`shells`
**************

:ref:`msfvenom`
*****************

Payloads
*************

Type of payloads on Windows

+---+------------------------------------------------------------------+
| D | libraries that help other programs.                              |
| L |                                                                  |
| L |                                                                  |
| s |                                                                  |
+===+==================================================================+
| B | .bat files - automating sysadmin style tasks                     |
| a |                                                                  |
| t |                                                                  |
| c |                                                                  |
| h |                                                                  |
+---+------------------------------------------------------------------+
| V | Often used in MS Office scripting now                            |
| B |                                                                  |
| S |                                                                  |
+---+------------------------------------------------------------------+
| M | Microsoft Installer database. The installer looks for msi to     |
| S | understand the components needed to install. You can use         |
| I | `msiexec` to execute your payload.                               |
+---+------------------------------------------------------------------+
| P | This is a shell and scripting language                           |
| o |                                                                  |
| w |                                                                  |
| e |                                                                  |
| r |                                                                  |
| s |                                                                  |
| h |                                                                  |
| e |                                                                  |
| l |                                                                  |
| l |                                                                  |
+---+------------------------------------------------------------------+

Payload Generation
*********************

Tools for creating payloads

1. MSFVenom               https://github.com/rapid7/metasploit-framework  
2. Payload all the things https://github.com/swisskyrepo/PayloadsAllTheThings
3. Mythic C2              https://github.com/its-a-feature/Mythic
4. Nishang                https://github.com/samratashok/nishang
5. Darkarmour             https://github.com/bats3c/darkarmour

Payload Delivery
*********************

1. Impacket (psexec, smbclient, wmi, evil-winrm)
2. Payload all the things
3. SMB
4. Metasploit
5. Standard protocols (FTP, SSH, HTTPS)


Windows Shells
****************

CMD
=====

When to use: - older host when PS is not available - Simple
interactions - using batch files - Execution policies may effect you

Powershell
===========

When to use:

-  You are utilizing cmdlets or other custom scripts
-  interacting with .NET objects
-  stealthy is a lesser concern
-  planning to interact with cloud based services
-  If you script sets and uses aliases

When on the metepreter prompt, you can type shell and get a local prompt

Linux local shell
======================

When you drop a shell with a user that does not have a shell defined in
/etc/passwd ( ie: www-data) you can create one in python (if python is
installed) with:

.. code-block:: console

   python -c 'import pty; pty.spawn("/bin/sh")' 

To run sh:

.. code-block:: console

   /bin/sh -i

If Perl is installed:

.. code-block:: console

   perl —e 'exec "/bin/sh";'

If Ruby (must be run from a script)

.. code-block:: console

   ruby: exec "/bin/sh"

If lua (must be run from a script)

.. code-block:: console

   lua: os.execute('/bin/sh')

If awk

.. code-block:: console

   awk 'BEGIN {system("/bin/sh")}'

using find:

.. code-block:: console

   find / -name nameoffile -exec /bin/awk 'BEGIN {system("/bin/sh")}' \;

Using VIM

.. code-block:: console

   vim -c ':!/bin/sh'

Checking what `sudo <sudo>`__ permission a user has:

.. code-block:: console

   sudo -l

:ref:`web shells`
**********************************

References
***********
https://academy.hackthebox.com/module/115/section/1101
