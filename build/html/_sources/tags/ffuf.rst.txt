
############
ffuf
############

2024-11-17 12:10

Status:

Tags: `Certified Penetration Tester <Certified Penetration Tester>`__
`Information Gathering <Information Gathering>`__

*****************
Description
*****************
A fuzzing tool using wordlists


******************
Installation
******************
.. code-block:: console

   sudo apt install ffuf

*****************
Usage
*****************


Example 1: Fuzzing for file extensions

.. code-block:: console

   ffuf -u http://94.237.54.115:31131/blog/indexFUZZ -w ~/HTB/wordlists/SecLists/Discovery/Web-Content/web-extensions.txt 

Example 2 : searching for files

.. code-block:: console

   ffuf -u http://94.237.54.115:31131/blog/FUZZ.php -w ~/HTB/wordlists/SecLists/Discovery/Web-Content/common.txt

Example 3: Searching for directories

.. code-block:: console

   ffuf -u http://94.237.54.115:31131/blog/FUZZ.php -w ~/HTB/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-small.txt

Example 4: Recursion

.. code-block:: console 

   ffuf -w ~/HTB/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-small.txt -u http://SERVER_IP:PORT/FUZZ -recursion -recursion-depth 1 -e .php -v

Example 5: Finding subdomains

.. code-block:: console

   ffuf -w ~/HTB/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt -u https://FUZZ.inlanefreight.com/

Example 6: VHOST Enumeration (-fs filter file size)

.. code-block:: console


   ffuf -w ~/HTB/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt -u https://academy.htb -H "Host: FUZZ.academy.htb" -fs 4242

Example 7: Parameter fuzzing

.. code-block:: console

   ffuf -w ~/HTB/wordlists/SecLists/Discovery/Web-Content/burp-parameter-names.txt 
   -u http://admin.academy.htb:31131/admin/admin.php?FUZZ=key -fs xxx

Example 8: POST Parameter FUZZ

.. code-block:: console

   ffuf -w /~/HTB/wordlists/SecLists/Discovery/Web-Content/burp-parameter-names.txt -u http://admin.academy.htb:PORT/admin/admin.php -X POST -d 'FUZZ=key' -H 'Content-Type: application/x-www-form-urlencoded' -fs xxx

References
==========
