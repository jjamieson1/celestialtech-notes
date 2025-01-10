Proxying Tools
###############

Date: 2025-01-09 16:02:52

Status: #draft 

Tags: :ref:`certified penetration tester`, :ref:`using web proxies`

----

Description 
***************

Proxy tools can also be used to intercept what command line tools are requesting. 

Proxychains 
***************

Setup 
=======

Edit your /etc/proxychains.conf file and add this line: 

.. code-block:: console

    #socks4         127.0.0.1 9050
    http 127.0.0.1 8080

You should also comment out `quiet_mode` to reduce noise. 

Now you can start any command with the proxychains command 


Usage
*******

Curl Example
==============

.. code-block:: console

    Temen@htb[/htb]$ proxychains curl http://SERVER_IP:PORT

    ProxyChains-3.1 (http://proxychains.sf.net)
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <title>Ping IP</title>
        <link rel="stylesheet" href="./style.css">
    </head>
    ...SNIP...
    </html>    

Nmap example 
==============

.. code-block:: bash

    Temen@htb[/htb]$ nmap --proxies http://127.0.0.1:8080 SERVER_IP -pPORT -Pn -sC

    Starting Nmap 7.91 ( https://nmap.org )
    Nmap scan report for SERVER_IP
    Host is up (0.11s latency).

    PORT      STATE SERVICE
    PORT/tcp open  unknown

    Nmap done: 1 IP address (1 host up) scanned in 0.49 seconds

.. note:: Not all options are enabled in this example, you can always fall back to using the proxychain command

Metaspoit example
=================

.. code-block:: bash

    Temen@htb[/htb]$ msfconsole

    msf6 > use auxiliary/scanner/http/robots_txt
    msf6 auxiliary(scanner/http/robots_txt) > set PROXIES HTTP:127.0.0.1:8080

    PROXIES => HTTP:127.0.0.1:8080


    msf6 auxiliary(scanner/http/robots_txt) > set RHOST SERVER_IP

    RHOST => SERVER_IP


    msf6 auxiliary(scanner/http/robots_txt) > set RPORT PORT

    RPORT => PORT


    msf6 auxiliary(scanner/http/robots_txt) > run

    [*] Scanned 1 of 1 hosts (100% complete)
    [*] Auxiliary module execution completed

