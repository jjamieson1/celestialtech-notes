enum4linux-ng
###############

Date: 2024-11-09 15:38

Status:

Description
*************

A enumeration tool for SMB

Installation
*************
The tool which returns a ton of information can be installed like this:

.. code-block:: console

   git clone https://github.com/cddmp/enum4linux-ng.git
   cd enum4linux-ng
   pip3 install -r requirements.txt

Usage
**********
Enumerate the target
=====================

Example 1: enumeration

.. code-block:: console

   ./enum4linux-ng.py 10.10.11.45 -A -C

Enumeration with password
==========================

Example 1: And can be used against a target like this: The password can
also be a NTLM hash

.. code-block:: console

   jjamieso@fatmex:~/HTB/enum4linux-ng$ ./enum4linux-ng.py 10.10.11.42 -u Olivia -p 'ichliebedich' -oY out
   ENUM4LINUX - next generation (v1.3.4)

    ==========================
   |    Target Information    |
    ==========================
   [*] Target ........... 10.10.11.42
   [*] Username ......... 'Olivia'
   [*] Random Username .. 'pdgblrok'
   [*] Password ......... 'ichliebedich'
   [*] Timeout .......... 5 second(s)

    ====================================
   |    Listener Scan on 10.10.11.42    |
    ====================================
   [*] Checking LDAP
   [+] LDAP is accessible on 389/tcp
   [*] Checking LDAPS
   [+] LDAPS is accessible on 636/tcp
   [*] Checking SMB
   [+] SMB is accessible on 445/tcp
   [*] Checking SMB over NetBIOS
   [+] SMB over NetBIOS is accessible on 139/tcp

    ===================================================
   |    Domain Information via LDAP for 10.10.11.42    |
    ===================================================
   [*] Trying LDAP
   [+] Appears to be root/parent DC
   [+] Long domain name is: administrator.htb

    ==========================================================
   |    NetBIOS Names and Workgroup/Domain for 10.10.11.42    |
    ==========================================================
   [-] Could not get NetBIOS names information via 'nmblookup': timed out

    ========================================
   |    SMB Dialect Check on 10.10.11.42    |
    ========================================
   [*] Trying on 445/tcp
   [+] Supported dialects and settings:
   Supported dialects:
     SMB 1.0: false
     SMB 2.02: true
     SMB 2.1: true
     SMB 3.0: true
     SMB 3.1.1: true
   Preferred dialect: SMB 3.0
   SMB1 only: false
   SMB signing required: true

    ==========================================================
   |    Domain Information via SMB session for 10.10.11.42    |
    ==========================================================
   [*] Enumerating via unauthenticated SMB session on 445/tcp
   [+] Found domain information via SMB
   NetBIOS computer name: DC
   NetBIOS domain name: ADMINISTRATOR
   DNS domain: administrator.htb
   FQDN: dc.administrator.htb
   Derived membership: domain member
   Derived domain: ADMINISTRATOR

    ========================================
   |    RPC Session Check on 10.10.11.42    |
    ========================================
   [*] Check for null session
   [+] Server allows session using username '', password ''
   [*] Check for user session
   [+] Server allows session using username 'Olivia', password 'ichliebedich'
   [*] Check for random user
   [-] Could not establish random user session: STATUS_LOGON_FAILURE

    ==================================================
   |    Domain Information via RPC for 10.10.11.42    |
    ==================================================
   [+] Domain: ADMINISTRATOR
   [+] Domain SID: S-1-5-21-1088858960-373806567-254189436
   [+] Membership: domain member

    ==============================================
   |    OS Information via RPC for 10.10.11.42    |
    ==============================================
   [*] Enumerating via unauthenticated SMB session on 445/tcp
   [+] Found OS information via SMB
   [*] Enumerating via 'srvinfo'
   [+] Found OS information via 'srvinfo'
   [+] After merging OS information we have the following result:
   OS: Windows 10, Windows Server 2019, Windows Server 2016
   OS version: '10.0'
   OS release: ''
   OS build: '20348'
   Native OS: not supported
   Native LAN manager: not supported
   Platform id: '500'
   Server type: '0x80102b'
   Server type string: Wk Sv PDC Tim NT

    ====================================
   |    Users via RPC on 10.10.11.42    |
    ====================================
   [*] Enumerating users via 'querydispinfo'
   [+] Found 10 user(s) via 'querydispinfo'
   [*] Enumerating users via 'enumdomusers'
   [+] Found 10 user(s) via 'enumdomusers'
   [+] After merging user results we have 10 user(s) total:
   '1108':
     username: olivia
     name: Olivia Johnson
     acb: '0x00000214'
     description: (null)
   '1109':
     username: michael
     name: Michael Williams
     acb: '0x00000210'
     description: (null)
   '1110':
     username: benjamin
     name: Benjamin Brown
     acb: '0x00000210'
     description: (null)
   '1112':
     username: emily
     name: Emily Rodriguez
     acb: '0x00000210'
     description: (null)
   '1113':
     username: ethan
     name: Ethan Hunt
     acb: '0x00000210'
     description: (null)
   '3601':
     username: alexander
     name: Alexander Smith
     acb: '0x00000211'
     description: (null)
   '3602':
     username: emma
     name: Emma Johnson
     acb: '0x00000211'
     description: (null)
   '500':
     username: Administrator
     name: (null)
     acb: '0x00000210'
     description: Built-in account for administering the computer/domain
   '501':
     username: Guest
     name: (null)
     acb: '0x00000215'
     description: Built-in account for guest access to the computer/domain
   '502':
     username: krbtgt
     name: (null)
     acb: '0x00000011'
     description: Key Distribution Center Service Account

    =====================================
   |    Groups via RPC on 10.10.11.42    |
    =====================================
   [*] Enumerating local groups
   [+] Found 6 group(s) via 'enumalsgroups domain'
   [*] Enumerating builtin groups
   [+] Found 28 group(s) via 'enumalsgroups builtin'
   [*] Enumerating domain groups
   [+] Found 15 group(s) via 'enumdomgroups'
   [+] After merging groups results we have 49 group(s) total:
   '1101':
     groupname: DnsAdmins
     type: local
   '1102':
     groupname: DnsUpdateProxy
     type: domain
   '1111':
     groupname: Share Moderators
     type: local
   '498':
     groupname: Enterprise Read-only Domain Controllers
     type: domain
   '512':
     groupname: Domain Admins
     type: domain
   '513':
     groupname: Domain Users
     type: domain
   '514':
     groupname: Domain Guests
     type: domain
   '515':
     groupname: Domain Computers
     type: domain
   '516':
     groupname: Domain Controllers
     type: domain
   '517':
     groupname: Cert Publishers
     type: local
   '518':
     groupname: Schema Admins
     type: domain
   '519':
     groupname: Enterprise Admins
     type: domain
   '520':
     groupname: Group Policy Creator Owners
     type: domain
   '521':
     groupname: Read-only Domain Controllers
     type: domain
   '522':
     groupname: Cloneable Domain Controllers
     type: domain
   '525':
     groupname: Protected Users
     type: domain
   '526':
     groupname: Key Admins
     type: domain
   '527':
     groupname: Enterprise Key Admins
     type: domain
   '544':
     groupname: Administrators
     type: builtin
   '545':
     groupname: Users
     type: builtin
   '546':
     groupname: Guests
     type: builtin
   '548':
     groupname: Account Operators
     type: builtin
   '549':
     groupname: Server Operators
     type: builtin
   '550':
     groupname: Print Operators
     type: builtin
   '551':
     groupname: Backup Operators
     type: builtin
   '552':
     groupname: Replicator
     type: builtin
   '553':
     groupname: RAS and IAS Servers
     type: local
   '554':
     groupname: Pre-Windows 2000 Compatible Access
     type: builtin
   '555':
     groupname: Remote Desktop Users
     type: builtin
   '556':
     groupname: Network Configuration Operators
     type: builtin
   '557':
     groupname: Incoming Forest Trust Builders
     type: builtin
   '558':
     groupname: Performance Monitor Users
     type: builtin
   '559':
     groupname: Performance Log Users
     type: builtin
   '560':
     groupname: Windows Authorization Access Group
     type: builtin
   '561':
     groupname: Terminal Server License Servers
     type: builtin
   '562':
     groupname: Distributed COM Users
     type: builtin
   '568':
     groupname: IIS_IUSRS
     type: builtin
   '569':
     groupname: Cryptographic Operators
     type: builtin
   '571':
     groupname: Allowed RODC Password Replication Group
     type: local
   '572':
     groupname: Denied RODC Password Replication Group
     type: local
   '573':
     groupname: Event Log Readers
     type: builtin
   '574':
     groupname: Certificate Service DCOM Access
     type: builtin
   '575':
     groupname: RDS Remote Access Servers
     type: builtin
   '576':
     groupname: RDS Endpoint Servers
     type: builtin
   '577':
     groupname: RDS Management Servers
     type: builtin
   '578':
     groupname: Hyper-V Administrators
     type: builtin
   '579':
     groupname: Access Control Assistance Operators
     type: builtin
   '580':
     groupname: Remote Management Users
     type: builtin
   '582':
     groupname: Storage Replica Administrators
     type: builtin

    =====================================
   |    Shares via RPC on 10.10.11.42    |
    =====================================
   [*] Enumerating shares
   [+] Found 5 share(s):
   ADMIN$:
     comment: Remote Admin
     type: Disk
   C$:
     comment: Default share
     type: Disk
   IPC$:
     comment: Remote IPC
     type: IPC
   NETLOGON:
     comment: Logon server share
     type: Disk
   SYSVOL:
     comment: Logon server share
     type: Disk
   [*] Testing share ADMIN$
   [+] Mapping: DENIED, Listing: N/A
   [*] Testing share C$
   [+] Mapping: DENIED, Listing: N/A
   [*] Testing share IPC$
   [+] Mapping: OK, Listing: NOT SUPPORTED
   [*] Testing share NETLOGON
   [+] Mapping: OK, Listing: OK
   [*] Testing share SYSVOL
   [+] Mapping: OK, Listing: OK

    ========================================
   |    Policies via RPC for 10.10.11.42    |
    ========================================
   [*] Trying port 445/tcp
   [+] Found policy:
   Domain password information:
     Password history length: 24
     Minimum password length: 7
     Maximum password age: 41 days 23 hours 53 minutes
     Password properties:
     - DOMAIN_PASSWORD_COMPLEX: false
     - DOMAIN_PASSWORD_NO_ANON_CHANGE: false
     - DOMAIN_PASSWORD_NO_CLEAR_CHANGE: false
     - DOMAIN_PASSWORD_LOCKOUT_ADMINS: false
     - DOMAIN_PASSWORD_PASSWORD_STORE_CLEARTEXT: false
     - DOMAIN_PASSWORD_REFUSE_PASSWORD_CHANGE: false
   Domain lockout information:
     Lockout observation window: 30 minutes
     Lockout duration: 30 minutes
     Lockout threshold: None
   Domain logoff information:
     Force logoff time: not set

References
*************
https://github.com/cddmp/enum4linux-ng
