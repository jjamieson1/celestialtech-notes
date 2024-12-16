Linux Mount
############

Date: 2024-11-28 22:16

Status:


Installation
*****************

Example 1: Adding the CIFS extension

.. code-block:: console

   sudo apt install cifs-utils

Usage
*******

Mounting a Samba share
========================

Example 1: Using plaintext credentials

.. code-block:: console 

   sudo mount -t cifs -o username=plaintext,password=Password123,domain=. //192.168.220.129/Finance /mnt/Finance

Example 2: Using a credential file

.. code-block:: console

   mount -t cifs //192.168.220.129/Finance /mnt/Finance -o credentials=/path/credentialfile

   cat credentialfile
   username=plaintext
   password=Password123
   domain=.

References
*************
https://academy.hackthebox.com/module/116/section/1140
