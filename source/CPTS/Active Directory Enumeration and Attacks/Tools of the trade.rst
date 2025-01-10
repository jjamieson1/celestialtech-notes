Tools of the trade
#######################

Date: 2025-01-05 08:10:06

Tags: :ref:`active directory enumeration attacks`

Status: #new

----



- :ref:`powerview` A PowerShell tool and a .NET port of the same used to gain situational awareness in AD. These tools can be used as replacements for various Windows net* commands and more. PowerView and SharpView can help us gather much of the data that BloodHound does, but it requires more work to make meaningful relationships among all of the data points. These tools are great for checking what additional access we may have with a new set of credentials, targeting specific users or computers, or finding some "quick wins" such as users that can be attacked via Kerberoasting or ASREPRoasting.
- :ref:`sharpview` see above
- :ref:`sharpHound` The C# data collector to gather information from Active Directory about varying AD objects such as users, groups, computers, ACLs, GPOs, user and computer attributes, user sessions, and more. The tool produces JSON files which can then be ingested into the BloodHound GUI tool for analysis.
- :ref:`bloodhound.py` Used to visually map out AD relationships and help plan attack paths that may otherwise go unnoticed. Uses the SharpHound PowerShell or C# ingestor to gather data to later be imported into the BloodHound JavaScript (Electron) application with a Neo4j database for graphical analysis of the AD environment.
- :ref:`kerbrute` A tool written in Go that uses Kerberos Pre-Authentication to enumerate Active Directory accounts, perform password spraying, and brute-forcing.
- :ref:`impacket` 	A collection of tools written in Python for interacting with network protocols. The suite of tools contains various scripts for enumerating and attacking Active Directory.
- :ref:`responder` Responder is a purpose-built tool to poison LLMNR, NBT-NS, and MDNS, with many different functions.
- :ref:`inveigh` Similar to Responder, a PowerShell tool for performing various network spoofing and poisoning attacks.
- :ref:`rpcinfo` The rpcinfo utility is used to query the status of an RPC program or enumerate the list of available RPC services on a remote host. The "-p" option is used to specify the target host. For example the command "rpcinfo -p 10.0.0.1" will return a list of all the RPC services available on the remote host, along with their program number, version number, and protocol. Note that this command must be run with sufficient privileges.
- :ref:`crackmapexec` CME is an enumeration, attack, and post-exploitation toolkit which can help us greatly in enumeration and performing attacks with the data we gather. CME attempts to "live off the land" and abuse built-in AD features and protocols like SMB, WMI, WinRM, and MSSQL.
- :ref:`rubeus` Rubeus is a C# tool built for Kerberos Abuse.
- :ref:`rpcclient` A part of the Samba suite on Linux distributions that can be used to perform a variety of Active Directory enumeration tasks via the remote RPC service.
- :ref:`getuserspns.py`  Another Impacket module geared towards finding Service Principal names tied to normal users.
- :ref:`hashcat` A great hash cracking and password recovery tool.
- :ref:`enum4linux-ng` A rework of the original Enum4linux tool that works a bit differently.
- :ref:`ldapsearch` Built-in interface for interacting with the LDAP protocol.
- :ref:`windapsearch` A Python script used to enumerate AD users, groups, and computers using LDAP queries. Useful for automating custom LDAP queries.
- :ref:`domainPasswordSpray` DomainPasswordSpray is a tool written in PowerShell to perform a password spray attack against users of a domain.
- :ref:`LAPSToolkit` The toolkit includes functions written in PowerShell that leverage PowerView to audit and attack Active Directory environments that have deployed Microsoft's Local Administrator Password Solution (LAPS).
- :ref:`smbmap` SMB share enumeration across a domain.
- :ref:`psexec.py` Part of the Impacket toolkit, it provides us with Psexec-like functionality in the form of a semi-interactive shell.
- :ref:`wmiexec.py` Part of the Impacket toolkit, it provides the capability of command execution over WMI
- :ref:`snaffler` Useful for finding information (such as credentials) in Active Directory on computers with accessible file shares.
- :ref:`smbserver.py` Simple SMB server execution for interaction with Windows hosts. Easy way to transfer files within a network.
- :ref:`setspn.exe` Adds, reads, modifies and deletes the Service Principal Names (SPN) directory property for an Active Directory service account.
- :ref:`mimikatz` Performs many functions. Notably, pass-the-hash attacks, extracting plaintext passwords, and Kerberos ticket extraction from memory on a host.
- :ref:`secretsdump.py` Remotely dump SAM and LSA secrets from a host.
- :ref:`evil-winrm` Provides us with an interactive shell on a host over the WinRM protocol.
- :ref:`mssqlclient.py` art of the Impacket toolkit, it provides the ability to interact with MSSQL databases.
- :ref:`nopac.py` Exploit combo using CVE-2021-42278 and CVE-2021-42287 to impersonate DA from standard domain user.
- :ref:`rcpdump.py` Part of the Impacket toolset, RPC endpoint mapper.
- :ref:`CVE-2021-1675.py` Printnightmare PoC in python.
- :ref:`impacket-ntlmrelayx` Part of the Impacket toolset, it performs SMB relay attacks.
- :ref:`petitpotam.py` PoC tool for CVE-2021-36942 to coerce Windows hosts to authenticate to other machines via MS-EFSRPC EfsRpcOpenFileRaw or other functions.
- :ref:`gettgtpkinit.py` Tool for manipulating certificates and TGTs.
- :ref:`getnthash.py` This tool will use an existing TGT to request a PAC for the current user using U2U.
- :ref:`adidnsdump` A tool for enumerating and dumping DNS records from a domain. Similar to performing a DNS Zone transfer.
- :ref:`gpp-decrypt` Extracts usernames and passwords from Group Policy preferences files.
- :ref:`GetNPUsers.py` Part of the Impacket toolkit. Used to perform the ASREPRoasting attack to list and obtain AS-REP hashes for users with the 'Do not require Kerberos preauthentication' set. These hashes are then fed into a tool such as Hashcat for attempts at offline password cracking.
- :ref:`lookupsid.py` SID bruteforcing tool.c
- :ref:`ticketer.py` A tool for creation and customization of TGT/TGS tickets. It can be used for Golden Ticket creation, child to parent trust attacks, etc.
- :ref:`raiseChild.py` Part of the Impacket toolkit, It is a tool for automated child to parent domain privilege escalation.
- :ref:`Active Directory Explorer` Active Directory Explorer (AD Explorer) is an AD viewer and editor. It can be used to navigate an AD database and view object properties and attributes. It can also be used to save a snapshot of an AD database for offline analysis. When an AD snapshot is loaded, it can be explored as a live version of the database. It can also be used to compare two AD database snapshots to see changes in objects, attributes, and security permissions.
- :ref:`PingCastle` Used for auditing the security level of an AD environment based on a risk assessment and maturity framework (based on CMMI adapted to AD security).
- :ref:`Group3r` Group3r is useful for auditing and finding security misconfigurations in AD Group Policy Objects (GPO).
- :ref:`ADRecon` A tool used to extract various data from a target AD environment. The data can be output in Microsoft Excel format with summary views and analysis to assist with analysis and paint a picture of the environment's overall security state.
