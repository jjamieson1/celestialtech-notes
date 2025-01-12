hydra
############

Date: 2024-11-30 15:04

Status: #draft

Tags: :ref:`certified penetration tester`, :ref:`login brute forcing`

----

Description
*****************
A utility for applying wordlist attacks to common services. 


Installation
******************

.. code-block:: bash 

   sudo apt-get -y update
   sudo apt install hydra


Usage
*****************

FTP
=====
Used to brute-force login credentials for FTP services, commonly used to transfer files over a network

.. code-block:: bash

   hydra -l admin -P /path/to/password_list.txt ftp://192.168.1.100

example 2: Testing FTP Credentials on a Non-Standard Port

.. code-block:: bash
   
   hydra -L usernames.txt -P passwords.txt -s 2121 -V ftp.example.com ftp


SSH
==================
Targets SSH services to brute-force credentials, commonly used for secure remote login to systems

.. code-block:: bash

   hydra -L <user.list> -P <password.list> ssh://<tagetIP>

 
HTTP 
=====
Used to brute-force login credentials for HTTP web login forms using either GET or POST requests.

Example 1: Brute force a login form

.. code-block:: bash

   hydra -l admin -P /path/to/password_list.txt http-post-form "/login.php:user=^USER^&pass=^PASS^:F=incorrect"

Example 2: To launch a brute-force attack against this Basic HTTP service, use the following Hydra command:

.. code-block:: bash

   hydra -L usernames.txt -P passwords.txt www.example.com http-get / -s 81

Let's break down the command:

- `-l basic-auth-user` This specifies that the username for the login attempt is 'basic-auth-user'.
- `-P 2023-200_most_used_passwords.txt` This indicates that Hydra should use the password list contained in the file '2023-200_most_used_passwords.txt' for its brute-force attack.
- `127.0.0.1` This is the target IP address, in this case, the local machine (localhost).
- `http-get /` This tells Hydra that the target service is an HTTP server and the attack should be performed using HTTP GET requests to the root path ('/').
- `-s 81` This overrides the default port for the HTTP service and sets it to 81.

Example 3: Brute-Forcing a Web Login Form

.. code-block:: bash

   hydra -l admin -P passwords.txt www.example.com http-post-form "/login:user=^USER^&pass=^PASS^:S=302"

- Use the username "admin".
- Use the list of passwords from the passwords.txt file.
- Target the login form at /login on www.example.com.
- Employ the http-post-form module with the specified form parameters.
- Look for a successful login indicated by the HTTP status code 302.

Example 4: HTTP Post example 

Considering a post submission like this:

.. code-block:: bash

   POST /login HTTP/1.1
   Host: www.example.com
   Content-Type: application/x-www-form-urlencoded
   Content-Length: 29

   username=john&password=secret123

hydra can be set with

.. code-block:: bash

   hydra ... http-post-form "/login:user=^USER^&pass=^PASS^:F=Invalid credentials"

Where `F` is a string to indicate failure.  Or using the `S` option to look for a success string We can also set the command to respond to a status code: 

.. code-block:: bash

   hydra ... http-post-form "/login:user=^USER^&pass=^PASS^:S=Dashboard"

We can also set the command to respond to a status code: 

.. code-block:: 

   hydra ... http-post-form "/login:user=^USER^&pass=^PASS^:S=302"

.. code-block:: bash

   hydra -L top-usernames-shortlist.txt -P 2023-200_most_used_passwords.txt -f IP -s 5000 http-post-form "/:username=^USER^&password=^PASS^:F=Invalid credentials"

SMTP
======
Attacks email servers by brute-forcing login credentials for SMTP, commonly used to send emails.

.. code-block:: bash

   hydra -l admin -P /path/to/password_list.txt smtp://mail.server.com

IMAP 
=====
Used to brute-force credentials for IMAP services, which allow users to access their email remotely.

.. code-block:: bash

   hydra -l user@example.com -P /path/to/password_list.txt imap://mail.server.com

MYSQL
======
Attempts to brute-force login credentials for MySQL databases.

.. code-block:: bash

   hydra -l root -P /path/to/password_list.txt mysql://192.168.1.100

MSSQL
========
Targets Microsoft SQL servers to brute-force database login credentials.

.. code-block:: bash

   hydra -l sa -P /path/to/password_list.txt mssql://192.168.1.100

VNC
=====
Brute-forces VNC services, used for remote desktop access

.. code-block:: bash

   hydra -P /path/to/password_list.txt vnc://192.168.1.100


RDP
==================
Targets Microsoft RDP services for remote login brute-forcing.

Example 1:  Trying both lists

.. code-block:: bash

   hydra -L <user.list> -P <password.list> rdp://<targetIP>

Example 2: Password Spraying

.. code-block:: bash

   hydra -L usernames.txt -p 'password123' 192.168.2.143 rdp

Example 3: Advanced RDP Brute-Forcing

Now, imagine you're testing a Remote Desktop Protocol (RDP) service on a server with IP 192.168.1.100. You suspect the username is "administrator," and that the password consists of 6 to 8 characters, including lowercase letters, uppercase letters, and numbers. To carry out this precise attack, use the following Hydra command:
 
.. code-block:: bash

   hydra -l administrator -x 6:8:abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 192.168.1.100 rdp

- Use the username "administrator".
- Generate and test passwords ranging from 6 to 8 characters, using the specified character set.
- Target the RDP service on 192.168.1.100.
- Employ the rdp module for the attack.

SMB
==================

.. code-block:: bash
   
   hydra -L <user.list> -P <password.list> ssh://<tagetIP>


Hydra for POP3
==================
Targets email retrieval services to brute-force credentials for POP3 login.

Example 1: Password spray attack for POP3

.. code-block:: bash

   hydra -L users.txt -p 'Company01!' -f 10.10.110.20 pop3



References
*****************

https://academy.hackthebox.com/module/116/section/1173
https://academy.hackthebox.com/module/57/section/504