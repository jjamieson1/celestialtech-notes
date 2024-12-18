smtp-user-enum 
***************

Date: 2024-11-30 14:58

Status: #mail

Installation
****************
.. code-block:: console

   git clone https://github.com/pentestmonkey/smtp-user-enum

Usage
******

Example 1: username hunting

.. code-block:: console

   smtp-user-enum -M RCPT -U userlist.txt -D inlanefreight.htb -t 10.129.203.7

References
**********
https://academy.hackthebox.com/module/116/section/1173
