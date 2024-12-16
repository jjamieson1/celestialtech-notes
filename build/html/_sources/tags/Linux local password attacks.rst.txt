Linux local password attacks
#############################

2024-11-22 12:29

Status:


Credential hunting in Linux
*******************************

Searching files for passwords
================================
Example 1: Looking for configuration files

.. code-block:: console

   for l in $(echo ".conf .config .cnf");do echo -e "\nFile extension: " $l; find / -name *$l 2>/dev/null | grep -v "lib\|fonts\|share\|core" ;done

Example 2: Looking for credentials in Database files

.. code-block:: console 

   for l in $(echo ".sql .db .*db .db*");do echo -e "\nDB File extension: " $l; find / -name *$l 2>/dev/null | grep -v "doc\|lib\|headers\|share\|man";done

Example 3: Looking for notes

.. code-block:: console

   find /home/* -type f -name "*.txt" -o ! -name "*.*"

Example 4: Looking for scripts

.. code-block:: console

   for l in $(echo ".py .pyc .pl .go .jar .c .sh");do echo -e "\nFile extension: " $l; find / -name *$l 2>/dev/null | grep -v "doc\|lib\|headers\|share";done

Example 5: Looking at cronjobs

.. code-block:: console

   crontab -e
   cat /etc/crontab
   ls -ls /etc/cron.*/

Looking for keys
===================

Example 1: Looking for private keys

.. code-block:: console

   grep -rnw "PRIVATE KEY" /home/* 2>/dev/null | grep ":1"

Example 1: Looking for public keys

.. code-block:: console


   grep -rnw "ssh-rsa" /home/* 2>/dev/null | grep ":1"

Looking at history files
========================

Example 1: bash_history

.. code-block:: console

   tail -n5 /home/*/.bash*

Looking in Logs
=================

Example 1: grepping in files like /var/log/\*

.. code-block:: console

   for i in $(ls /var/log/* 2>/dev/null);do GREP=$(grep "accepted\|session opened\|session closed\|failure\|failed\|ssh\|password changed\|new user\|delete user\|sudo\|COMMAND\=\|logs" $i 2>/dev/null); if [[ $GREP ]];then echo -e "\n#### Log file: " $i; grep "accepted\|session opened\|session closed\|failure\|failed\|ssh\|password changed\|new user\|delete user\|sudo\|COMMAND\=\|logs" $i 2>/dev/null;fi;done

Looking in memory and cache
=============================

Example 1: Using
:doc: `mimpenguin <https://github.com/huntergregal/mimipenguin>` to look at
credentials stored in browsers ( requires root)

.. code-block:: console

   sudo python3 mimipenguin.py

Example 2: Using :ref: `lazagne`

Credentials in Browsers
==========================

Example 1: Getting the password for Mozilla

.. code-block:: console 

   cat .mozilla/firefox/1bplpd86.default-release/logins.json | jq .

There is a tool called `Firefox Decrypt <Firefox Decrypt>`__ that can
crack passwords and also `lazagne <lazagne>`__ using the browser option

Passwd, Shadow and Opasswd
===========================
The shadow password hashing algorithm can be determined by this format?

.. code-block:: console

   $<type>$<salt>$<hashed>

   $1$ – MD5
   $2a$ – Blowfish
   $2y$ – Eksblowfish
   $5$ – SHA-256
   $6$ – SHA-512

The Opasswd file, requires root permission to read, holds old passwords
that the PAM module uses to prevent users from using old passwords.

Example 1: Un-shadowing the ``/etc/passwd`` file

.. code-block:: console

   Temen@htb[/htb]$ sudo cp /etc/passwd /tmp/passwd.bak 
   Temen@htb[/htb]$ sudo cp /etc/shadow /tmp/shadow.bak 
   Temen@htb[/htb]$ unshadow /tmp/passwd.bak /tmp/shadow.bak > /tmp/unshadowed.hashes

Example 2: Cracking the hash file

.. code-block:: console

   hashcat -m 1800 -a 0 /tmp/unshadowed.hashes rockyou.txt -o /tmp/unshadowed.cracked

Example 3: Cracking an md5 hashes

.. code-block:: console

   hashcat -m 500 -a 0 md5-list rockyou.txt

TUqr7QfLTLhruhVbCP

References
***********
https://academy.hackthebox.com/module/147/section/1320
