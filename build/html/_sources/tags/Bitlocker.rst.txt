###########
Bitlocker
###########

2024-11-28 10:52

Status:

Tags: 

*******************
Cracking Bitlocker
*******************

Example 1: Using John to extract the hash

.. code-block:: console

   Temen@htb[/htb]$ bitlocker2john -i Backup.vhd > backup.hashes
   Temen@htb[/htb]$ grep "bitlocker\$0" backup.hashes > backup.hash
   Temen@htb[/htb]$ cat backup.hash

Using hashcat to crack the password:

.. code-block:: console

   hashcat -m 22100 backup.hash /opt/useful/seclists/Passwords/Leaked-Databases/rockyou.txt -o backup.cracked


*************
References
*************
