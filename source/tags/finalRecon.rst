##############
finalRecon
##############

2024-11-17 10:55

Status:

Tags: `Certified Penetration Tester <Certified Penetration Tester>`__
`Information Gathering <Information Gathering>`__

************
Details
************

A Python-based reconnaissance tool offering a range of modules for
different tasks like SSL certificate checking, Whois information
gathering, header analysis, and crawling. Its modular structure enables
easy customization for specific needs.

************
Installation
************

.. code-block:: console

   Temen@htb[/htb]$ git clone https://github.com/thewhiteh4t/FinalRecon.git
   Temen@htb[/htb]$ cd FinalRecon
   Temen@htb[/htb]$ pip3 install -r requirements.txt
   Temen@htb[/htb]$ chmod +x ./finalrecon.py
   Temen@htb[/htb]$ ./finalrecon.py --help

Example:

.. code-block:: console

   ./finalrecon.py --headers --whois --url http://inlanefreight.com

************
References
************
https://academy.hackthebox.com/module/144/section/3081
