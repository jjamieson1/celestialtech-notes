sqsh
#####

Date: 2024-11-28 22:22

Status:

sqsh Description
*****************

A command line utility for quering the MSSQL database

sqshUsage
***********

sqsh Connecting using DB credentials
======================================

Example 1: Connecting to the service

.. code-block:: console

   sqsh -S 10.10.10.10 -U username -P password

sqsh Connecting using domain credentials
******************************************

Example 1: Using domain creds

.. code-block:: console

   sqsh -S 10.129.203.7 -U .\\username -P 'MyPassword!' -h

References
**************
https://academy.hackthebox.com/module/116/section/1140
