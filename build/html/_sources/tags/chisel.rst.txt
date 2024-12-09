########
chisel
########

Date: 2024-11-27 14:05

Status:

Tags: 

*************
Installation
*************

.. code-block:: bash

   Temen@htb[/htb]$ wget https://github.com/jpillora/chisel/releases/download/v1.7.7/chisel_1.7.7_linux_amd64.gz
   Temen@htb[/htb]$ gzip -d chisel_1.7.7_linux_amd64.gz
   Temen@htb[/htb]$ sudo mv chisel_* /usr/bin/chisel && suco chmod +x /usr/bin/chisel

   Temen@htb[/htb]$ sudo ./chisel server --reverse 

************
Usage
************

Example 1: Run a server on port 1080
.. code-block:: 

   sudo chisel server --port 1080 --reverse


Example 2: Run a client to connect to the server
.. code-block:: 

   c:\tools\chisel.exe client <attack-host>:1080 R:socks

************
References
************
https://academy.hackthebox.com/module/147/section/1657
