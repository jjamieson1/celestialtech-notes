whatweb
########

Date: 2024-11-17 08:14

Status:

Description
***************

Command-line tool for website fingerprinting.

Features
*********

Uses a vast database of signatures to identify various web technologies.

Example:

.. code-block:: console

   whatweb 10.10.10.75/nibbleblog

Output

.. code-block:: console

   http://10.10.10.75/nibbleblog [301 Moved Permanently] Apache[2.4.18], Country[RESERVED][ZZ], HTTPServer[Ubuntu Linux][Apache/2.4.18 (Ubuntu)], IP[10.10.10.75], RedirectLocation[http://10.10.10.75/nibbleblog/], Title[301 Moved Permanently]
   http://10.10.10.75/nibbleblog/ [200 OK] Apache[2.4.18], Cookies[PHPSESSID], Country[RESERVED][ZZ], HTML5, HTTPServer[Ubuntu Linux][Apache/2.4.18 (Ubuntu)], IP[10.10.10.75], JQuery, MetaGenerator[Nibbleblog], PoweredBy[Nibbleblog], Script, Title[Nibbles - Yum yum]

References
*************
https://academy.hackthebox.com/module/144/section/3075
