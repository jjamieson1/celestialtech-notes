Network Enumeration with nmap
###############################

Status: draft

Date: 2024-11-09 14:48

Tags: 

Description
***********
Versatile network scanner that can be used for various reconnaissance tasks, including service and OS fingerprinting.

Features
********
Can be used with scripts (NSE) to perform more specialised fingerprinting.

Examples
********


Example 1: OS Host detection
==============================

.. code-block:: console
  
    sudo nmap -v -O 192.168.86.39

Example 2: Banner grab to enumerate ports
=========================================

.. code-block:: console

    sudo nmap -v 192.168.86.39 --script banner.nse

Example 3: You can update the nmap database with:
==================================================

.. code-block:: console

    sudo nmap --script-updatedb



Ping Sweep
==========

.. code-block:: console

    nmap -sn 10.0.0.0/24

Adding --script-trace to the nmap command will show which scripts are running during the scan

Checking for a SMTP open-relay
===============================

.. code-block:: console
    
    nmap -p25 -Pn --script smtp-open-relay 10.10.11.213



References
************
https://academy.hackthebox.com/module/144/section/3075
