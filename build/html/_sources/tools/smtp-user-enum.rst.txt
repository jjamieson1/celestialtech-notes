###############
smtp-user-enum
###############

Status: draft

Date: 2024-11-09 14:48

Tags: 

*************
Description
*************
Use the VRFY method (-M VRFY) to search for the specified user (-u root) on the target server (-t 192.168.1.25):

**************
Installation
**************

.. code-block::

    sudo apt install smtp-user-enum


Usage
*****

.. code-block::

    smtp-user-enum -M VRFY -u root -t 192.168.1.25


***********
References
***********
https://www.kali.org/tools/smtp-user-enum/