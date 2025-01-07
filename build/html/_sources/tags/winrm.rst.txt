winrm
#######

Date: 2024-11-11 18:43

Status:

Description
************

A service on Windows to allow management via a SOAP interface.

Ports
*********

``5985`` ``5986`` ## Exploits There is a Ruby Gem called evil-winrm that
allows us to interactively get a shell. Example:


Usage
************

Using WinRM
=============

.. code-block:: console

   evil-winrm -i 10.129.136.91 -u administrator -p badminton

Using powershell
==================

.. code-block:: powershell

    PS C:\htb> $password = ConvertTo-SecureString "Klmcargo2" -AsPlainText -Force
    PS C:\htb> $cred = new-object System.Management.Automation.PSCredential ("INLANEFREIGHT\forend", $password)
    PS C:\htb> Enter-PSSession -ComputerName ACADEMY-EA-MS01 -Credential $cred

    [ACADEMY-EA-MS01]: PS C:\Users\forend\Documents> hostname
    ACADEMY-EA-MS01
    [ACADEMY-EA-MS01]: PS C:\Users\forend\Documents> Exit-PSSession
    PS C:\htb> 


Footprinting
*************

Example 1: using nmap

.. code-block:: console

   nmap -sV -sC 10.129.201.248 -p5985,5986 --disable-arp-ping -n

References
*************
https://academy.hackthebox.com/module/112/section/1242
