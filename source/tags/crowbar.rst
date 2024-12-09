############
crowbar
############

Date: 2024-11-29 18:42

Status:

Tags: 

*****************
Description
*****************

A utility used to spray passwords ## Installation

.. code-block:: bash

   git clone https://github.com/galkan/crowbar
   cd crowbar
   pip install -r requirements.txt


*****************
Usage
*****************

Example 1: Attacking RDP
.. code-block::

   crowbar -b rdp -s 192.168.220.142/32 -U users.txt -c 'password123'


*****************
References
*****************
https://academy.hackthebox.com/module/116/section/1171
https://github.com/galkan/crowbar
