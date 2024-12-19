############
evil-winrm
############


Date: 2024-11-29 18:42

Status:

Tags:

*****************
Description
*****************
A tool to interactively communicate with the service  :ref:`winrm`


*************
installation
*************
.. code-block:: console

    sudo gem install evil-winrm



*****************
Usage
*****************

Example 1: Using a password

.. code-block:: console

    evil-winrm -i <targetIP> -u <username> -p <password>

Example 2: Using PTH (pass the hash)

.. code-block:: console
    
    evil-winrm -i 10.129.201.57  -u  Administrator -H "64f12cddaa88057e06a81b54e73b949b"

Example 3: Using Kerberose authentication

.. code-block:: console

    evil-winrm -i dc01 -r inlanefreight.htb


*****************
References
*****************
https://academy.hackthebox.com/module/147/section/1327
