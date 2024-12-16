nikto
######

Date: 2024-11-17 08:27

Status:

Description
**************

A web scanner that looks for vulnerabilities

Installation
***************

.. code-block:: console

   Temen@htb[/htb]$ sudo apt update && sudo apt install -y perl
   Temen@htb[/htb]$ git clone https://github.com/sullo/nikto
   Temen@htb[/htb]$ cd nikto/program
   Temen@htb[/htb]$ chmod +x ./nikto.pl

Example: using the fingerprinting function

.. code-block:: console

    nikto -h inlanefreight.com -Tuning b

References
**************
https://academy.hackthebox.com/module/144/section/3075
