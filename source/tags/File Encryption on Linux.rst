#########################
File Encryption on Linux
#########################


Date: 2024-11-29 18:42

Status:

Tags:

*****************
Description
*****************

OpenSSL is commonly installed on Linux

*****************
Usage
*****************

Example 1: To encrypt a file with a password:

.. code-block:: console

   Temen@htb[/htb]$ openssl enc -aes256 -iter 100000 -pbkdf2 -in /etc/passwd -out passwd.enc

Then to decrypt the file:

.. code-block:: console

   Temen@htb[/htb]$ openssl enc -d -aes256 -iter 100000 -pbkdf2 -in passwd.enc -out passwd 


*****************
References
*****************
~                  
