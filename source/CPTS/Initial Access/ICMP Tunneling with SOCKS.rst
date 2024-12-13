ICMP Tunneling with SOCKS
#########################

Description
***********

By leveraging ICMP requests and responses we can encapsulate our traffic in this data.  This is an 
important tool for sites with very restrictive firewalls.

In this example we will be using a tool called ptunnel-ng


Installation
************

.. code-block:: console

    git clone https://github.com/utoni/ptunnel-ng.git
    cd  ptunnel-ng
    sudo ./autogen.sh


**Alternative approach and building a static binary**

.. code-block:: console

    Temen@htb[/htb]$ sudo apt install automake autoconf -y
    Temen@htb[/htb]$ cd ptunnel-ng/
    Temen@htb[/htb]$ sed -i '$s/.*/LDFLAGS=-static "${NEW_WD}\/configure" --enable-static $@ \&\& make clean \&\& make -j${BUILDJOBS:-4} all/' autogen.sh
    Temen@htb[/htb]$ sudo ./autogen.sh

Attack example
**************

Step 1: Transfer the binary to the pivot host

Step 2: Start the service on the pivot host

.. code-block:: console

    ## The ip address is the local address where the client will be connecting
    sudo ./ptunnel-ng -r10.129.202.64 -R22


Step 3:  Start the client on the attack host

.. code-block:: console

    sudo ./ptunnel-ng -p10.129.202.64 -l2222 -r10.129.202.64 -R22


Step 4:  Connect via port 2222 with SSH

.. code-block:: console

    ssh -p2222 -lubuntu 127.0.0.1


**Alternate** Connecting with port forwarding with

.. code-block:: console

    ssh -D 9050 -p2222 -lubuntu 127.0.0.1

Now we can use proxychains to run other programs

.. code-block:: console

    proxychains nmap -sV -sT 172.16.5.19 -p3389

