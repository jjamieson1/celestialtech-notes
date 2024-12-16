psexec
##########

Date: 2024-11-29 10:59

Status:

Description
*************

 A freeware utility for Windows. It works because it has a Windows
service image inside of its executable. It takes this service and
deploys it to the admin$ share (by default) on the remote machine. It
then uses the DCE/RPC interface over SMB to access the Windows Service
Control Manager API. Next, it starts the PSExec service on the remote
machine. The PSExec service then creates a `named
pipe <https://docs.microsoft.com/en-us/windows/win32/ipc/named-pipes>`__ that
can send commands to the system.

Linux implementations
***********************

:ref: `impacket`

:ref: `crackmapexec`

References
***************
https://academy.hackthebox.com/module/116/section/1167
