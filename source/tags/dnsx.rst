#######
dnsx
#######

Status: draft

Date: 2024-11-09 14:48

Tags: 

**************
Installation
**************

.. code-block:: console

    sudo apt install dnsx

*********
Usage
*********

Example: 

.. code-block:: console
    
    dnsx -l domains.txt -resp -a -aaaa -cname -mx -ns -soa -txt
    dnsx -silent -d megacorpone.com -w /usr/share/seclists/Discovery/DNS/dns-Jhaddix.txt



************
References
************
https://www.kali.org/tools/dnsx/
