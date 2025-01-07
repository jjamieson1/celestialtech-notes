Kerberos Double Hop Problem
##############################

Date: 2025-01-05 08:10:06

Tags: :ref:`active directory enumeration attacks`

Status: #new

Description
************

Kerberose tickets are issued to a resource, and will not permit you to keep reusing it across hosts as you would with a hash or password. 


Solutions
*************

Solution 1: PSCredential Objects
==================================

Create an object 

.. code-block:: powershell

    PS C:\Users\backupadm\Documents> $SecPassword = ConvertTo-SecureString '!qazXSW@' -AsPlain
    PS C:\Users\backupadm\Documents>  $Cred = New-Object System.Management.Automation.PSCredential('INLANEFREIGHT\backupadm', $SecPassword)

Now in :ref:`powerview`, we just need to add `-credential $Cred` to our commands 


Solution 2: Register PSSession configuration
===============================================

registering a new session configuration using the Register-PSSessionConfiguration cmdlet.

.. code-block:: powershell

    PS C:\htb> Register-PSSessionConfiguration -Name backupadmsess -RunAsCredential inlanefreight\backupadm

Then restarting the WinRM service with : `Restart-Service WinRM`

References 
************
https://academy.hackthebox.com/module/143/section/1573