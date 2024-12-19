wmiexec.py
##########

Date: 2024-12-19 14:26:02

Status: 

Tags:

Description
***********

A similar approach to smbexec but executing commands through WMI.
Main advantage here is it runs under the user (has to be Admin)
account, not SYSTEM, plus, it doesn't generate noisy messages
in the event log that smbexec.py does when creating a service.
Drawback is it needs DCOM, hence, I have to be able to access
DCOM ports at the target machine.

References
*************
https://github.com/fortra/impacket/blob/master/examples/wmiexec.py