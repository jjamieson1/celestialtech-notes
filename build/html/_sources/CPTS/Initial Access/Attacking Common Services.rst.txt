Attacking Common Services
##########################

Date: 2024-11-28 22:01

Status:

Using the OS Utilities
***********************

- :ref:`Windows CMD`

- :ref:`powershell`

- :ref:`Linux Mount`

- :ref:`Bash`

- :ref:`sqsh`

- :ref:`sqlcmd`

Attacking :ref:`FTP`
***********************

- Brute forcing with :ref:`medusa`

- FTP bounce attacks :ref:`FTP`

- FTP Exploits :ref:`FTP`

Attacking :ref:`SMB`
************************

- :ref:`Enumerating SMB`

- :ref:`SMB Anonymous Authentication <Anonymous Authentication>`

- Using :ref:`smbmap <smbmap>` to list shares, files and permission

-  List shares :ref:`SMBMap Enumerating services`

-  Recursive list files :ref:`SMBMap Recursive listing of files`

-  Download files :ref:`SMBMap Downloading files`

-  Using :ref:`rpcclient <rpcclient>` to enumerate users

-  Using :ref:`enum4linux-ng <enum4linux-ng>` to enumerate the target

-  Using :ref:`crackmapexec <crackmapexec>` to brute force

-  Using :ref:`psexec <psexec>`

-  Using :ref:`responder <responder>` to capture hashes

-  Using :ref:`impacket <impacket>`

-  Using :ref:`RPC <RPC>` with :ref:`rpcclient <rpcclient>`

Attacking SQL
*****************

- Banner grabbing :ref:`MSSQL Footprinting <MSSQL Footprinting>`

- Connecting with :ref:`sqlcmd <sqlcmd>` on a Windows host

- Connecting with :ref:`sqsh <sqsh>` on a Linux Host

- Connecting and using the Windows account :ref:`sqsh Connecting using domain credentials <sqsh Connecting using domain credentials>`

- xp_cmdshell on :ref:`MSSQL <MSSQL>`

- Writing files/shells in :ref:`MySQL Dropping shells and writing files <MySQL Dropping shells and writing files>`

- Writing/Reading files with :ref:`MSSQL Writing files <MSSQL Writing files>`

- Reading files in :ref:`MySQL <MySQL>`

- Stealing MSSQL service hash :ref:`MSSQL <MSSQL>`

Attacking :ref:`rdp <rdp>`
***************************

- Password spraying with :ref:`crowbar <crowbar>`

- Password spraying with :ref:`hydra <hydra>`

- RDP Session Hijacking with :ref:`tscon.exe <tscon.exe>`

- RDP using pass the hash :ref:`xfreerdp Usage <xfreerdp Usage>`

Attacking DNS
**************

- Enumerating DNS with :ref:`fierce <fierce>`

- Enumerating subdomains with :ref:`subfinder <subfinder>`

- Brute forcing DNS that has no Internet access with :ref:`subbrute <subbrute>`

- DNS Poisoning with :ref:`ettercap <ettercap>` and :ref:`bettercap <bettercap>` to perform :ref:`MITM6 <MITM6>`

Attacking Mail Services
**************************

**Notes**: You can verify that a user exists on the socket, by using
VRFY (for users) and EXPN (for mail groups) and examining the response (
+OK versus -ERR)

- Enumerating users with :ref:`smtp-user-enum <smtp-user-enum>`

- Cloud enumeration by password spraying with :ref:`O365spray <O365spray>`

- Password attacks with :ref:`hydra <hydra>`

- Checking for an open Relay with :ref:`nmap Checking for a SMTP open-relay <nmap Checking for a SMTP open-relay>`

References
**************
https://academy.hackthebox.com/module/116/section/1140
https://github.com/puzzithinker/cybersecurity_cheatsheets/blob/main/ATTACKING%20COMMON%20SERVICES.md
