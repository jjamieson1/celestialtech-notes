medusa
#######

Date: 2024-11-29 08:57

Status:

Installation
***************

.. code-block:: console

   sudo apt-get -y update
   sudo apt install medusa

Usage
***********

By using the `-t` option you can instantiate multiple threads. 

FTP
=====

Example 1: Brute forcing FTP

.. code-block:: console

    medusa -u fiona -P /usr/share/wordlists/rockyou.txt -h 10.129.203.7 -M ftp

Example 2: Parallel connections with threads

.. code-block:: console

   medusa -U ./users.list -P ./pws.list -M ftp  -h 10.129.175.180 -n 2121 -v5 -L -t 11

HTTP
======

Example 1: Brute-forcing login forms on web applications over HTTP (GET/POST)

.. code-block:: bash

   medusa -M http -h www.example.com -U users.txt -P passwords.txt -m DIR:/login.php -m FORM:username=^USER^&password=^PASS^

Example 2: Brute forcing login forms on websites using HTTP POST requests.

.. code-block:: bash

   medusa -M web-form -h www.example.com -U users.txt -P passwords.txt -m FORM:"username=^USER^&password=^PASS^:F=Invalid"

Example 3: Web Servers with Basic HTTP Authentication

.. code-block:: bash 

   medusa -H web_servers.txt -U usernames.txt -P passwords.txt -M http -m GET 



IMAP
======

Example 1: Brute-forcing IMAP logins, often used to access email servers.

.. code-block:: bash

   medusa -M imap -h mail.example.com -U users.txt -P passwords.txt

MySQL 
======
Example 1: Brute-forcing MySQL database credentials, commonly used for web applications and databases.

.. code-block:: bash 

   medusa -M mysql -h 192.168.1.100 -u root -P passwords.txt

POP3 
======

Example 1: Brute-forcing POP3 logins, typically used to retrieve emails from a mail server.

.. code-block:: bash

   medusa -M pop3 -h mail.example.com -U users.txt -P passwords.txt

RDP
=====

Example 1: Brute-forcing RDP logins, commonly used for remote desktop access to Windows systems.

.. code-block:: bash

   medusa -M rdp -h 192.168.1.100 -u admin -P passwords.txt

SSHv2 
======

Example 1: Brute-forcing SSH logins, commonly used for secure remote access.

.. code-block:: bash

   medusa -M ssh -h 192.168.1.100 -u root -P passwords.txt

Example 2: 

.. code-block:: bash

   medusa -h <IP> -n <PORT> -u sshuser -P 2023-200_most_used_passwords.txt -M ssh -t 

   
SVN 
=====

Example 1: Brute-forcing Subversion (SVN) repositories for version control.

.. code-block:: bash

   medusa -M svn -h 192.168.1.100 -u admin -P passwords.txt

Telnet
========

Example 1: Brute-forcing Telnet services for remote command execution on older systems.

.. code-block:: bash

   medusa -M telnet -h 192.168.1.100 -u admin -P passwords.txt

VNC 
=====

Example 1: Brute-forcing VNC login credentials for remote desktop access.

.. code-block:: bash

   medusa -M vnc -h 192.168.1.100 -P passwords.txt

Testing for Empty or Default passwords 
=========================================

.. code-block:: bash 

   medusa -h 10.0.0.5 -U usernames.txt -e ns -M service_name

This command instructs Medusa to:

- Target the host at 10.0.0.5.
- Use the usernames from usernames.txt.
- Perform additional checks for empty passwords (-e n) and passwords matching the username (-e s).
- Use the appropriate service module (replace service_name with the correct module name).

References
**************
- https://academy.hackthebox.com/module/116/section/1165
- https://academy.hackthebox.com/module/57/section/512
