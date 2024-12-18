r-services
##############

Date: 2024-11-11 18:30

Status:


Ports
********

512, 513, 514 available through r-commands (

-  rcp
-  rexec
-  rlogin
-  rstat
-  ruptime
-  rwho

Configuration
***************

The configuration is defined in the /etc/hosts.equiv file

Example:

.. code-block:: console

   cat /etc/hosts.equiv

   # <hostname> <local username>
   pwnbox cry0l1t3

Footprinting
***************

Example 1: Using Nmap

.. code-block:: console

   sudo nmap -sV -p 512,513,514 10.0.17.2

Access Control and Trust
*************************

Example: .rhost file

.. code-block:: console

   cat .rhosts

   htb-student     10.0.17.5
   +               10.0.17.10
   +               +

**Note** the + = wildcard

example 2: Logging in with rlogin

.. code-block:: console

   rlogin 10.0.17.2 -l htb-student

Example 3: Listing other network users

.. code-block:: console

   rusers -al 10.0.17.5

   htb-student     10.0.17.5:console          Dec 2 19:57     2:25

References
************
https://academy.hackthebox.com/module/112/section/1240
