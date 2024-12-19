secretsdump.py
##############

Date: 2024-12-19 14:31:22

Status: 

Tags:

Description
***********
Performs various techniques to dump hashes from the
  remote machine without executing any agent there.
For SAM and LSA Secrets (including cached creds)
we try to read as much as we can from the registry
and then we save the hives in the target system
(%SYSTEMROOT%\\Temp dir) and read the rest of the
 data from there.
 
For NTDS.dit we either:
  a. Get the domain users list and get its hashes
    and Kerberos keys using [MS-DRDS] DRSGetNCChanges()
    call, replicating just the attributes we need.
  b. Extract NTDS.dit via vssadmin executed  with the
    smbexec approach.
    It's copied on the temp dir and parsed remotely.


References
**********
https://github.com/fortra/impacket/blob/master/examples/secretsdump.py