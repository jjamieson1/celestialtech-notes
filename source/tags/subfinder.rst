subfinder
###########

Status: draft

Date: 2024-11-09 14:48

Tags: 

Description
************

This package contains a subdomain discovery tool that discovers valid subdomains for websites by using passive online sources. It has a simple modular architecture and is optimized for speed. subfinder is built for doing one thing only - passive subdomain enumeration, and it does that very well.

**************
Installation
**************

.. code-block:: console

    sudo apt install subfinder

*********
Usage
*********

Example: 

.. code-block:: console
    
    subfinder -silent -d megacorpone.com | dnsx -silent
    subfinder -silent -d megacorpone.com | dnsx -silent -a -resp
    subfinder -silent -d megacorpone.com | dnsx -silent -a -resp-only
    subfinder -silent -d megacorpone.com | dnsx -silent -cname -resp
    subfinder -silent -d megacorpone.com | dnsx -silent -asn 



************
References
************
https://www.kali.org/tools/subfinder/
