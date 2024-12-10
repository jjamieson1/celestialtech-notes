#####################################################
Dynamic Port Forwarding with SSH and SOCKS Tunneling
#####################################################

*****************
Description
*****************
The process of using various methods outlined in this note to access hosts, networks and services not normally accessible from the public network.


==============================
SSH Tunnel over SOCKS Proxy
==============================

Step 1: Create a connection using dynamic port forwarding with:

.. code-block:: console

   ssh -D 9050 ubuntu@10.129.202.64

Step 2: Configure proxychains to use the tunnel.  Add the port association with the socks4 entry

.. code-block:: console

   Temen@htb[/htb]$ tail -4 /etc/proxychains.conf
   dynamic_chain
   # meanwile
   # defaults set to "tor"
   socks4 	127.0.0.1 9050

**note:** I had to switch from strict_chain to dynamic_chain for this to work

Step 3:  When you start the nmap with proxychains, the packets will route through the 9050 port locally to the ubuntu server.

.. code-block:: console

   proxychains nmap -v -sn 172.16.5.1-200

**Important Note** proxychains does not understant half open connections like a SYN scan.  It will only error on this.  You will need to do full connect scans using Proxychains.

====================================
Using applications and Proxychains
====================================

Any application that needs to reach out to ordinarily unreachable services can be started with Proxychains and the system will pivot through the connected server.

Example:  RDP Connection

.. code-block:: console
   
   proxychains xfreerdp /v:172.16.5.19 /u:victor /p:pass@123

