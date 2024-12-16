RDP and SOCKS Tunneling with SocksOverRDP
#########################################

Description
***********

In the case that there are no unix hosts, and Windows is the only option, we need to consider tools to pivot through
that can be built for Windows.

There are tools built on the Dynamic Virtual Channels (DVC) from the Remote Desktop Service feature of Windows.

Examples are : 

* https://github.com/nccgroup/SocksOverRDP
* https://www.proxifier.com/download/#win-tab

Usage
*****

Step 1: Copy the SocksOverRDPx64.zip to the Windows host

Step 2: Start by loading the SocksOverRDP.dll using regsvr32.exe

.. code-block:: console

    C:\Users\htb-student\Desktop\SocksOverRDP-x64> regsvr32.exe SocksOverRDP-Plugin.dll

Step 3: Connect to the target from the Windows pivot host with mstsc.exe - There will now be a notice that
says that the plugin is enabled and it will listen on 127.0.0.1:8080

Step 4: Transfer the SocksOverRDPx64.exe to the target and start the service with admin privs

Confirm it is started with:

.. code-block:: console

    C:\Users\htb-student\Desktop\SocksOverRDP-x64> netstat -antb | findstr 1080

    TCP    127.0.0.1:1080         0.0.0.0:0              LISTENING

Step 5:  Transfer the Proxifier portable to the pivot host and configure it to forward out packets to 
`127.0.0.1:1080`

With Proxifier running we can now start mstsc.exe and pivot all our traffic via 127.0.0.1:1090 tunneled to 
the target host using SocksOverRDP-server.exe. 


References
**********
