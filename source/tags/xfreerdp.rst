xfreerdp
##########

Date: 2024-11-21 10:53

Status:

xfreerdp Description
**********************

A Linux client to connect to rdp services

xfreerdp Installation
***************
.. code-block:: console

   sudo apt install xfreerdp

xfreerdp Usage
****************

.. code-block:: console

   xfreerdp /v:10.129.42.197 /u:user /p:password

xfreerdp on HTB 
*****************

.. code-block:: bash

   xfreerdp /v:10.129.4.230 /u:htb-student /p:Academy_student_AD! /dynamic-resolution /bpp:8 /async-update /auto-reconnect /compression

You can either enable or disable the clipboard with +clipboard or -clipboard

xfreerdp accessing with Pass the hash
***************************************

Step 1: Adding a reg key to allow it

.. code-block:: console

   C:\htb> reg add HKLM\System\CurrentControlSet\Control\Lsa /t REG_DWORD /v DisableRestrictedAdmin /d 0x0 /f

| Step 2:
| Use the hash instead of the password

.. code-block:: console

   xfreerdp /v:192.168.220.152 /u:lewen /pth:300FF5E89EF33F83A8146C10F5AB9BB9

References
*************
https://academy.hackthebox.com/module/147/section/1327
