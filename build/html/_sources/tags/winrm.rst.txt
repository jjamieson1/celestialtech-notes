winrm
#######

Date: 2024-11-11 18:43

Status:

Description
************

A service on Windows to allow management via a SOAP interface.

Ports
*********

``5985`` ``5986`` ## Exploits There is a Ruby Gem called evil-winrm that
allows us to interactively get a shell. Example:

.. code-block:: console

   evil-winrm -i 10.129.136.91 -u administrator -p badminton

Footprinting
*************

Example 1: using nmap

.. code-block:: console

   nmap -sV -sC 10.129.201.248 -p5985,5986 --disable-arp-ping -n

References
*************
https://academy.hackthebox.com/module/112/section/1242
