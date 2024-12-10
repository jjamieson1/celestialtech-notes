############
gobuster
############

2024-11-16 19:33

Status:

Tags: `Certified Penetration Tester <Certified Penetration Tester>`__
`Footprinting <Footprinting>`__
`Information Gathering <Information Gathering>`__

*****************
Description
*****************


Brute forces directory listings, vhosts and subdomains

******************
Installation
******************

.. code-block:: console

   go install gobuster

*****************
Usage
*****************

Example 1: -x look for a particular file, -w wordlist to use

.. code-block:: console 

   gobuster dir -u 10.129.126.187 -x php -w wordlists/SecLists/Discovery/Web-Content/common.txt

Example 2: Targeting a virtual host
.. code-block:: console

   gobuster vhost -u http://94.237.51.74:56507 -w ~/HTB/wordlists/SecLists/Discovery/DNS/subdomains-top1million-110000.txt --append-domain

`Resource securitynewspaper <https://www.securitynewspaper.com/2019/11/04/bruteforce-any-website-with-gobuster-step-by-step-guide/>`__


*****************
References
*****************
https://academy.hackthebox.com/module/144/section/1257
