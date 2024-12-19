rpcinfo
########

Date: 2024-12-19 15:09:22

Status: 

Tags:

Description
***********

The rpcinfo utility is used to query the status of an RPC program or enumerate the list of available RPC services on a remote host. The "-p" option is used to specify the target host. For example the command "rpcinfo -p 10.0.0.1" will return a list of all the RPC services available on the remote host, along with their program number, version number, and protocol. Note that this command must be run with sufficient privileges.

References
**********
https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/rpcinfo