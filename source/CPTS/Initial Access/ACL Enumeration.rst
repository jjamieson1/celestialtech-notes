ACL Enumeration
##################

Date: 2024-12-30 18:49:57

Status: #new

Tags: :ref:`active directory enumeration attacks`

Enumerating ACLs with :ref:`powerview`
**************************************

Using :ref:`powerview` to enumerate can be very overwhelming, since it is likely to return numerous results. 

Example: 

.. code-block:: powershell

    PS C:\htb> Find-InterestingDomainAcl



References
****************
https://book.hacktricks.xyz/windows-hardening/active-directory-methodology/acl-persistence-abuse


import-module ./Powerview.ps1
$forend = Convert-NameToSid forend 
PS C:\htb> Get-DomainObjectACL -ResolveGUIDs -Identity "GPO Management" | ? {$_.SecurityIdentifier -eq $forend} -Verbose