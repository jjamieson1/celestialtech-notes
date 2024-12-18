#####
rdp
#####

Status:

Description
***********
A client for linux

Example 1: xfreerdp on linux to connect to rdp sessions. start with:

.. code-block:: console

   xfreerdp /v:ip_address /u:username /p:password /dynamic-resolution

Footprinting
************
Example 1: Using nmap

.. code-block:: console

   nmap -sV -sC 10.129.201.248 -p3389 --script rdp*

To investigate that your traffic you can use –packet-trace

Example 2: Nmap and packet trace

.. code-block:: console

   nmap -sV -sC 10.129.201.248 -p3389 --packet-trace --disable-arp-ping -n

Installation:
*************
.. code-block:: console

   sudo cpan 
   git clone https://github.com/CiscoCXSecurity/rdp-sec-check.git && cd rdp-sec-check

Usage
*****
.. code-block:: console

   ./rdp-sec-check.pl 10.129.201.248

References
**********
https://academy.hackthebox.com/module/112/section/1242
