Remote Password Attacks
########################

Date: 2024-11-22 08:03

Status:

Attacking network services
****************************
:ref:`crackmapexec` Remote services like Windows
:ref:`winrm` allows tools like :ref:`crackmapexec`
can attack this service. (also attacks LDAP, :ref:`SMB`,
:ref:`MSSQL`)

:ref:`evil-winrm` This tool allows us to interactively
communicate with WinRM

:ref:`hydra` is a tool to brute force :ref:`ssh`

:ref:`hydra` A tool to brute force :ref:`rdp` to get
credentials, and use them on :ref:`xfreerdp`

:ref:`hydra` A tool to brute force :ref:`smb` shares,
but may not work with version 3

:ref:`Using the Metasploit Framework` By
using the scanning module in *auxilary/scanner/smb/smb_login* we can
force smb v3. Once you have credentials you can use
:ref:`crackmapexec` to see what shares are available.

:ref:`smbclient` To interact with SMB in a FTP like interface.

References
**************
https://academy.hackthebox.com/module/147/section/1327
