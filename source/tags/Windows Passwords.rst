Windows Passwords
##################

Date: 2024-11-21 10:17

Status:

Windows Passwords
*****************

Windows Authentication process
=================================
**LSA** (Local security authority) A protected sub-system of windows
responsible for local account mapping, groups and authentication. Keeps
track of security policies, generate monitoring messages, checks
permissions.

LSASS
======

*Local Security Authority Subsystem Service*

A collection of modules and has access to all authentication processes.
Upon initial login LSASS will: 1. Cache creds locally in memory 2.
create access tokens 3. enforce security policies 4. write to the window
security log

SAM Database
================

*Security Account Manager*

User password are stored in either a LM or NTLM hash. Located if
**SystemRoot%/system32/config/SAM** and is mounted as HKLM/SAM.SYSTEM.
**System** level permissions are required to view it.

If a server is designated as a Workgroup, it will host a SAM database
locally. If the server is part of an active directory domain, it must
validate it’s credentials from AD which is stored in
**%SYSTEMROOT:raw-latex:`\ntds`.dit**

Credential Manager
=====================

 Users credentials are saved in their profile so that they can access
  network resources. It is stored in a credential locker in PS
  C::raw-latex:`\Users`[Username]:raw-latex:`\AppData`:raw-latex:`\Local`:raw-latex:`\Microsoft`[Vault/Credentials]

References
***************
https://academy.hackthebox.com/module/147/section/1313
