kerbrute
#########

Description
***********

A stealthy option for domain account enumeration.  It leverages kerberose authentication failures.
By using a list like `insidetrust <https://github.com/insidetrust/statistically-likely-usernames>`_  This tool will 
allow us to see which accounts are valid in this list.

Installation
************

.. code-block:: console

     sudo git clone https://github.com/ropnop/kerbrute.git
     cd kerbrute
     make linux 
     ## To make for all platforms use make all binaries found in dist folder


Usage
*****

.. code-block:: console

     kerbrute userenum -d INLANEFREIGHT.LOCAL --dc 172.16.5.5 jsmith.txt -o valid_ad_users

References
**********
https://academy.hackthebox.com/module/143/section/1265
