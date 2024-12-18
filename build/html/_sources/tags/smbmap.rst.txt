smbmap
#######

Date: 2024-11-09 15:35

Status:

Installation
***************

Usage
***********


SMBMap Enumerating services
============================

Example 1: Used for enumeration of SMB services

.. code-block:: console


   smbmap -H 10.129.14.128

   [+] Finding open SMB ports....
   [+] User SMB session established on 10.129.14.128...
   [+] IP: 10.129.14.128:445       Name: 10.129.14.128                                     
           Disk                                                    Permissions     Comment
           ----                                                    -----------     -------
           print$                                                  NO ACCESS       Printer Drivers
           home                                                    NO ACCESS       INFREIGHT Samba
           dev                                                     NO ACCESS       DEVenv
           notes                                                   NO ACCESS       CheckIT
           IPC$                                                    NO ACCESS       IPC Service (DEVSM)

SMBMap Recursive listing of files
===================================

Example 1: Used to recursively list files in a share

.. code-block:: console

   smbmap -H 10.129.14.128 -r <share-name>

SMBMap Downloading files
==========================

Example 1: Download

.. code-block:: console

   smbmap -H 10.129.14.128 --download "notes\note.txt"

References
************
https://academy.hackthebox.com/module/116/section/1167
