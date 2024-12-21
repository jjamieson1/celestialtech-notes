LLMNR/NBT-NS Poisoning - from Linux
###################################

Description
************
Using man in the middle (MITM) attacks leveraging 
Link-Local Multicast Name Resolution (LLMNR) and NetBIOS Name Service (NBT-NS) broadcasts
services by poisoning them.

Introduction
*************

LLMNR and NetBIOS Name Service serve as alternate methods when Name services fail.  If a DNS query fails, the client will reach out to all the other hosts and ask for resolution.  

If LLMNR `(port 5355/udp)` fails, the client will fall back to NBT-NS `(Port 137/udp)`.  

The hack
*********
Since any host can respond to these requests, our :ref: `responder` can be used to poison the requests.

Example
========

1. A host trys to connect to a print server with an invalid name
2. DNS responds and indicates that this does not exist.
3. The host then broadcasts out to the entire network asking for resolutuion.
4. The responder program responds that it is the printer it is looking for.
5. The host attempts to authenticate to responder, and the hash is captured.
6. The hash is cracked offline or used in a SMB Relay attack.

Tools for poisoning
====================

1. :ref:`responder`
2. :ref:`inveigh`
3. :ref:`metasploit`

References
***********
https://academy.hackthebox.com/module/143/section/1272
