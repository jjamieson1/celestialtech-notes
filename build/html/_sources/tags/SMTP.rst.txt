SMTP
######

Date: 2024-11-10 17:36

Status:

Description
*************
Nowadays it is known as ESMTP (enhanced smtp) using TLS

Enumeration
***********

Example 1: Using Nmap to get the version

.. code-block:: console

    sudo nmap 10.129.14.128 -sC -sV -p25

Example 2: To check for an open relay

.. code-block:: console

   sudo nmap 10.129.200.67 -p25 --script smtp-open-relay -v

smtp-user-enum
*****************

A tool written in Perl found at
Download https://pentestmonkey.net/tools/smtp-user-enum/smtp-user-enum-1.2.tar.gz

Example 1: Help

.. code-block:: console

   ./smtp-user-enum -?

Example 2: Scanned with defaults and a word list

.. code-block:: console

   ./smtp-user-enum.pl -U /home/jjamieso/HTB/footprinting-wordlist.txt -t 10.129.200.67 -t 15 -v

Metasploit
**************
The module that can perform user enumeration via SMTP in Metasploit
Framework is the following:

**auxiliary/scanner/smtp/smtp_enum** 
References
***********
https://academy.hackthebox.com/module/112/section/1072
https://pentestlab.blog/2012/11/20/smtp-user-enumeration/
