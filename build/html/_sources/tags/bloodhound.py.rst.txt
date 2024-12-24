bloodhound.py
###############

Date: 2024-12-04 15:10

Status:

Tags:


Installation
****************

.. code-block:: console

   git clone https://github.com/dirkjanm/bloodhound.py


Usage
****************

.. code-block:: console

   bloodhound-py -d certified.htb -u 'judith.mader' -p 'judith09' -gc DC01.certified.htb -ns 10.10.11.41 -c all


Example: Bloodhound.py Collecting all information 
===================================================

.. code-block:: bash

   Temen@htb[/htb]$ sudo bloodhound-python -u 'username' -p 'password' -ns 172.16.5.5 -d inlanefreight.local -c all 

Once the utility has completed, you can find the results in files in the current directory. 


References
****************
https://academy.hackthebox.com/module/143/section/1269