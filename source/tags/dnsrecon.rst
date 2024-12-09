########
dnsrecon
########


Status: draft

Date: 2024-11-09 14:48

Tags: 


Installation
************

.. code-block::

    sudo apt install dnsrecon


Usage
*****

.. code-block::

    dnsrecon -d www.example.com -a 
    dnsrecon -d www.example.com -t axfr
    dnsrecon -d "startIP-endIP"
    dnsrecon -d www.example.com -D "namelist" -t brt


References
**********
https://www.kali.org/tools/dnsenum/
