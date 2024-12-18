rsync
*******

Date: 2024-11-11 18:29

Status:

Description
*************

A utility to synchronize files. Can be configured to tunnel inside SSH
connections.

Port
=====

``873/tcp``

**Example**: –list-only to list on remove server

.. code-block:: console

   rsync --list-only 10.129.250.213::

Footprinting
*************

Example 1:

.. code-block:: console

   rsync -e ssh -azvp  files destination_ip:/filesystem_path

Example 2:

.. code-block:: console

   sudo nmap -sV -p 873 127.0.0.1 

Example 3: Enumeration of a open share

.. code-block:: console

   rsync -av --list-only rsync://127.0.0.1/dev

Using netcat to list shares

example:

.. code-block:: console

   nc -nv 127.0.0.1 873

   UNKNOWN) [127.0.0.1] 873 (rsync) open
   @RSYNCD: 31.0
   @RSYNCD: 31.0
   #list
   dev             Dev Tools
   @RSYNCD: EXIT

References
*************
https://academy.hackthebox.com/module/112/section/1240
