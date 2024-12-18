SNMP
#######

Date: 2024-11-11 09:52

Status:

Description
************

Simple network management protocol. There are version 1, 2 and 3. In
version 3 authentication was added for more security (preshared key)

Ports
*********

| ``161 udp`` Transmits control commands
| ``162 tcp`` SNMP devices can initialize requests to other devices.

MIB (management information base)
***********************************

a schema that is used across various manufacturers for interoperability.

OID
*****

Represents a node in the hierarchical namespace. OID’s can be searched
in the OID registry at https://www.alvestrand.no/objectid/

Community Strings
********************

Can be viewed clear text over a transmission, you can view them as a
password.

Configuration
***************

.. code-block:: console

   Temen@htb[/htb]$ cat /etc/snmp/snmpd.conf | grep -v "#" | sed -r '/^\s*$/d'

   sysLocation    Sitting on the Dock of the Bay
   sysContact     Me <me@example.org>
   sysServices    72
   master  agentx
   agentaddress  127.0.0.1,[::1]
   view   systemonly  included   .1.3.6.1.2.1.1
   view   systemonly  included   .1.3.6.1.2.1.25.1
   rocommunity  public default -V systemonly
   rocommunity6 public default -V systemonly
   rouser authPrivUser authpriv -V systemonly

Footprinting
**************

SNMPwalk
===========

Example 1: an unauthenticated request

.. code-block:: console

   snmpwalk -v2c -c public 10.129.14.128

onesixtone
============

This tool can be used to brute force the names of the community strings.
We can use a tool like :ref:`crunch` to create new word lists.

Example 1: Brute force community string

.. code-block:: console

   sudo apt install onesixtyone
   onesixtyone -c /home/jjamieso/HTB/wordlist/SecLists/Discovery/SNMP/snmp.txt 10.129.14.128

braa
========

Once we know the name of the community string we can use braa to brute
force the individual OIDs and enumerate the information.

Example 1: Install and use

.. code-block:: console

   sudo apt install braa
   braa <community string>@<IP>:.1.3.6.*   # Syntax
   braa public@10.129.14.128:.1.3.6.*

References
*************
https://academy.hackthebox.com/module/112/section/1075
