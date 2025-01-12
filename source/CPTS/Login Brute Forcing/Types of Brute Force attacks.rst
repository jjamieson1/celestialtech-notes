Types of Brute Force attacks 
################################

Date: 2025-01-10 13:38:45

Status: Draft 

Tags: :ref:`certified penetration tester`, :ref:`login brute forcing`

----

Types of Brute Force Attacks
*******************************


Simple Brute Force
====================

Description
--------------
Systematically tries all possible combinations of characters within a defined character set and length range.

Example
-----------
Trying all combinations of lowercase letters from 'a' to 'z' for passwords of length 4 to 6.

Best Used When
-----------------
No prior information about the password is available, and computational resources are abundant.

----

Dictionary Attack
===================

Description
---------------
Uses a pre-compiled list of common words, phrases, and passwords.

Example
-----------
Trying passwords from a list like 'rockyou.txt' against a login form.


Best Used When
-----------------

The target will likely use a weak or easily guessable password based on common patterns.

----

Hybrid Attack
==================

Description
---------------
Combines elements of simple brute force and dictionary attacks, often appending or prepending characters to dictionary words.

Example
-----------
Adding numbers or special characters to the end of words from a dictionary list.


Best Used When
-----------------
The target might use a slightly modified version of a common password.

----

Credential Stuffing
===================

Description
---------------
Leverages leaked credentials from one service to attempt access to other services, assuming users reuse passwords.


Example
-----------
Using a list of usernames and passwords leaked from a data breach to try logging into various online accounts.


Best Used When
-----------------
A large set of leaked credentials is available, and the target is suspected of reusing passwords across multiple services.

----

Password Spraying
===================

Description
---------------
Attempts a small set of commonly used passwords against a large number of usernames.

Example
-----------
Trying passwords like 'password123' or 'qwerty' against all usernames in an organization.


Best Used When
-----------------
Account lockout policies are in place, and the attacker aims to avoid detection by spreading attempts across multiple accounts.

----

Rainbow Table Attack
===================

Description
---------------
Targets a single password against multiple usernames, often used in conjunction with credential stuffing attacks.

Example
-----------
Using a leaked password from one service to try logging into multiple accounts with different usernames.


Best Used When
-----------------
A strong suspicion exists that a particular password is being reused across multiple accounts.

----

Reverse Brute Force
=====================

Description
--------------
Targets a single password against multiple usernames, often used in conjunction with credential stuffing attacks.

Example
-----------
Using a leaked password from one service to try logging into multiple accounts with different usernames.

Best used when...
-------------------
A strong suspicion exists that a particular password is being reused across multiple accounts.

----

Distributed Brute Force
==========================

Description
---------------
Distributes the brute forcing workload across multiple computers or devices to accelerate the process.

Example
----------

Using a cluster of computers to perform a brute-force attack significantly increases the number of combinations that can be tried per second.

Best Used when
-----------------
The target password or key is highly complex, and a single machine lacks the computational power to crack it within a reasonable timeframe.

----

When to use brute force techniques
*************************************

- When other avenues are exhausted. 
- Password policies are weak 
- Specific accounts are targeted 

References
************

https://academy.hackthebox.com/module/57/section/506