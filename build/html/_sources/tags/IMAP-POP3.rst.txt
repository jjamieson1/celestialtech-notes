IMAP-POP3
#############

Date: 2024-11-10 18:55

Status:

Default Ports
***************

IMAP: 143, 993 (TLS) POP: 110, 995 (TLS)

Footprinting the service
***************************

Example 1: nmap the relevant ports with

.. code-block:: console

   sudo nmap 10.129.14.128 -sV -p110,143,993,995 -sC

Example 2: Curl can be used to connect to these protocols too if the
user/password is known

.. code-block:: console

    curl -k 'imaps://10.129.14.128' --user user:p4ssw0rd -v

Example 3: Connecting with OpenSSL and POP3 and IMAP

.. code-block:: console

   openssl s_client -connect 10.129.14.128:pop3s
   openssl s_client -connect 10.129.14.128:imaps

References
************
https://academy.hackthebox.com/module/112/section/1073
