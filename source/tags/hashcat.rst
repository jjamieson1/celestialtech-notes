hashcat
############
2024-11-23 10:28

Status:

Tags: 

:ref:`Certified Penetration Tester <Certified Penetration Tester>`
:ref:`Password Attacks <Password Attacks>`


Description
*****************
A hash cracking utility utilizing word lists and rules


Installation
******************

Example 1: installation

.. code-block:: console 

   sudo apt install hashcat



Usage
*****************

| -a is the mode.
| \* 0 is straight mode \* 1 is combination more

-m is the hash type. You can use :ref:`hashid <hashid>` to help identify
this

**create a SHA1 hash to test with**

.. code-block:: console

   echo -n 'St@r5h1p2019' | sha1sum | awk '{print $1}' | tee hash


Rules
*****************

Example 1: Append 2020 to the end of all attempts

.. code-block:: console

   echo 'c so0 si1 se3 ss5 sa@ $2 $0 $2 $0' > rule.txt

The first letter word is capitalized with the ``c`` function. Then rule
uses the substitute function ``s`` to replace ``o`` with ``0``, ``i``
with ``1``, ``e`` with ``3`` and a with ``@``. At the end, the year
``2020`` is appended to it.

Example 2 : Debuging the rule

.. code-block:: console

   hashcat -r rule.txt test.txt --stdout

Example 3: using a hashcat rule

.. code-block:: console

   hashcat -a 0 -m 1000 hash.txt ../wordlists/rockyou.txt -r /usr/share/hashcat/rules/d3ad0ne.rule


Mask Attack
*****************

Example

.. code-block:: console

   hashcat -a 3 -m 0 <hash> -1 01 'ILFREIGHT?l?l?l?l?l20?1?d'


Hybrid attack
*****************

Example 1:

.. code-block:: console

   hashcat -a 7 -m 0 hybrid_hash_prefix -1 01 '20?1?d' ~/HTB/wordlists/rockyou.txt

Example 2:

.. code-block:: console

   hashcat -a6 hashfile.txt rockyou.txt ?d?d?d

Example 3: Hybrid attack with masks and increment:

.. code-block:: console

   hashcat -a6 hasfile.txt rockyou.txt -i ?u?l?l?l??d?d?s

Example 4: Classic hybrid attack the other way around with a mask:

.. code-block:: console

   hashcat -a7 ?d?d?d hashfile.txt rockyou.txt

Example 5: Classic hybrid attack the other way around with mask and
increment:

.. code-block:: console

   hashcat -a7 -i ?d?d?d hashfile.txt rockyou.txt


Advanced Attacks
*****************



Loopback
===========

Password that have been cracked before are added to the dictionary until
no new passwords are found.

Example 1: Loopback

.. code-block:: console

   hashcat -a 0 <hash> wordlist/rockyou.txt  --loopback -r rule.txt


Raking
===========

Raking will generate random rules and running them over the hashes. This
is useful if you have run out of success with standard measures.

Example 1: Adding -g to generate random rules
``Example 2: Raking hashat -a 0 <hash> wordlist/rockyou.txt  --loopback -g``

Example 2: Raking and saving random rules to a file for analysis

.. code-block:: console

   hashat -a 0 <hash> wordlist/rockyou.txt  --loopback -g --debug-mode=1 --debug-file=matched.rule


:ref:`cewl <cewl>`
======================

For generating custom word lists based off a website.


hashcat-utils
======================

**Installation**

.. code-block:: console

   Temen@htb[/htb]$ git clone https://github.com/hashcat/hashcat-utils.git
   Temen@htb[/htb]$ cd hashcat-utils/src
   Temen@htb[/htb]$ make


hashid
========

Identifies the type of hash. 
.. code-block:: console

   pip install hashid


References
****************
https://www.prosec-networks.com/en/blog/password-cracking/
