WMI
#####

Date: 2024-11-11 18:45

Status:

Description
**************

Windows Management Instrumentation

Footprinting
*************
Ports
==========
``135/tcp``

Example 1: Using WMIexec.py with password

.. code-block:: console

    /usr/share/doc/python3-impacket/examples/wmiexec.py Cry0l1t3:"P455w0rD!"@10.129.201.248 "hostname"


Using WMI to enumerate the host
********************************

.. list-table:: WMI Commands 
   :widths: 50 50
   :header-rows: 1

   * - Commands
     - Description
   * - `wmic qfe get Caption,Description,HotFixID,InstalledOn`
     - Prints the patch level and description of the Hotfixes applied
   * - `wmic computersystem get Name,Domain,Manufacturer,Model,Username,Roles /format:List`
     - Displays basic host information to include any attributes within the list
   * - `wmic process list /format:list`
     - A listing of all processes on host
   * - `wmic ntdomain list /format:list`
     - Displays information about the Domain and Domain Controllers
   * - `wmic useraccount list /format:list`
     - Displays information about all local accounts and any domain accounts that have logged into the device
   * - `wmic group list /format:list`
     - Information about all local groups
   * - `wmic sysaccount list /format:list`
     - Dumps information about any system accounts that are being used as service accounts.

Example 2:

.. code-block:: powershell

    PS C:\htb> wmic ntdomain get Caption,Description,DnsForestName,DomainName,DomainControllerAddress

References
************
https://academy.hackthebox.com/module/112/section/1242s
