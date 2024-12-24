windapsearch
############

Date: 2024-12-19 14:11:19

Status: 

Tags:

Description
***********

windapsearch is a Python script to help enumerate users, groups and computers from a Windows domain through LDAP queries. By default, Windows Domain Controllers support basic LDAP operations through port 389/tcp. With any valid domain account (regardless of privileges), it is possible to perform LDAP queries against a domain controller for any AD related information.

You can always use a tool like ldapsearch to perform custom LDAP queries against a Domain Controller. I found myself running different LDAP commands over and over again, and it was difficult to memorize all the custom LDAP queries. So this tool was born to help automate some of the most useful LDAP queries a pentester would want to perform in an AD environment.


Usage 
*******

Example: Search for domain Admins
====================================

Listing users with domain admin privileges

.. code-block:: bash

    python3 windapsearch.py --dc-ip 172.16.5.5 -u username@inlanefreight.local -p password --da

Example: Windapsearch - Privileged Users
==========================================

Listing users with elevated privileges

.. code-block:: bash

    python3 windapsearch.py --dc-ip 172.16.5.5 -u usernmae@inlanefreight.local -p password -PU

References
**********
https://github.com/ropnop/windapsearch

