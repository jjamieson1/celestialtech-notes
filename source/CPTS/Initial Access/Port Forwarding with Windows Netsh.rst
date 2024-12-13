Port Forwarding with Windows Netsh
##################################

Description
***********

A Windows command line utility for:
1. Finding routes
2. Viewing firewall configs
3. Adding proxies
4. Creating port forwarding rules

**Example** of port forwarding using netsh

Given the pivot host at 10.129.15.15 we need to get to an address on the otherwise inaccessible 172.16.5 network

.. code-block:: console

    C:\Windows\system32> netsh.exe interface portproxy add v4tov4 listenport=8080 listenaddress=10.129.15.150 connectport=3389 connectaddress=172.16.5.25

To verify this is running you can check with:

.. code-block:: console

    C:\Windows\system32> netsh.exe interface portproxy show v4tov4

    Listen on ipv4:             Connect to ipv4:

    Address         Port        Address         Port
    --------------- ----------  --------------- ----------
    10.129.42.198   8080        172.16.5.25     3389

Now on our attack host we can pivot through the pivot host and get to the 172.16 network.  

Reference
*********
https://academy.hackthebox.com/module/158/section/1435

