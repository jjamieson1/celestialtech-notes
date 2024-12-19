GetNPUsers.py
#############

Date: 2024-12-19 14:52:35

Status:

Tags:

Description
***********

 This script will attempt to list and get TGTs for those users that have the property
'Do not require Kerberos preauthentication' set (UF_DONT_REQUIRE_PREAUTH).
For those users with such configuration, a John The Ripper output will be generated so
you can send it for cracking.

References
************
https://github.com/fortra/impacket/blob/master/examples/GetNPUsers.py