Active Directory Enumeration Attacks
####################################

Date: 2024-12-19 12:54:04

Status: #in-progress

Tags: :ref:`Certified Penetration Tester`

Introduction
**************

Active directory came out in 2000 with the release of Windows Server 2000.  Active Directory (AD) is based
on the x.500 protocol.  AD provides structures for:

- Users
- Groups
- Network Devices
- File shares
- Policies
- devices and trusts

AD provides authentication, accounting and authorization within a Windows enterprise. 

See more on AD in the module:  :ref:`Introduction to Active Directory` 

:ref:`External Recon and Enumeration Principles`
************************************************

:ref:`Initial Enumeration of a AD Domain`
*****************************************

:ref:`LLMNR/NBT-NS Poisoning - from Linux`
********************************************

:ref:`llmnr-nbt-ns poisoning - from windows`
************************************************

:ref:`Password Spraying`
****************************

:ref:`Enumerating and Retrieving Password Policies`
******************************************************

:ref:`Internal Password Spraying from Linux`
***********************************************

:ref:`Internal Password Spraying from Windows` 
***********************************************







Tools of the trade
******************

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


Stories from the field
**********************

Scenario 1: Waiting on An Admin 
================================

During this engagement, I compromised a single host and gained SYSTEM level access. Because this was a domain-joined host, I was able to use this access to enumerate the domain. I went through all of the standard enumeration, but did not find much. There were Service Principal Names (SPNs) present within the environment, and I was able to perform a Kerberoasting attack and retrieve TGS tickets for a few accounts. I attempted to crack these with :ref:`hashcat` and some of my standard wordlists and rules, but was unsuccessful at first. I ended up leaving a cracking job running overnight with a very large wordlist combined with the :ref:`d3ad0ne` rule that ships with :ref:`hashcat`. The next morning I had a hit on one ticket and retrieved the cleartext password for a user account. This account did not give me significant access, but it did give me write access on certain file shares. I used this access to drop SCF files around the shares and left Responder going. After a while, I got a single hit, the NetNTLMv2 hash of a user. I checked through the BloodHound output and noticed that this user was actually a domain admin! Easy day from here.

Scenario 2: Spraying the night away
===================================

Password spraying can be an extremely effective way to gain a foothold in a domain, but we must exercise great care not to lock out user accounts in the process. On one engagement, I found an SMB NULL session using the :ref:`enum4linux-ng` tool and retrieved both a listing of all users from the domain, and the domain password policy. Knowing the password policy was crucial because I could ensure that I was staying within the parameters to not lock out any accounts and also knew that the policy was a minimum eight-character password and password complexity was enforced (meaning that a user's password required 3/4 of special character, number, uppercase, or lower case number, i.e., Welcome1). I tried several common weak passwords such as Welcome1, Password1, Password123, Spring2018, etc. but did not get any hits. Finally, I made an attempt with Spring@18 and got a hit! Using this account, I ran :ref:`bloodHound` and found several hosts where this user had local admin access. I noticed that a domain admin account had an active session on one of these hosts. I was able to use the Rubeus tool and extract the Kerberos TGT ticket for this domain user. From there, I was able to perform a pass-the-ticket attack and authenticate as this domain admin user. As a bonus, I was able to take over the trusting domain as well because the Domain Administrators group for the domain that I took over was a part of the Administrators group in the trusting domain via nested group membership, meaning I could use the same set of credentials to authenticate to the other domain with full administrative level access.

Scenario 3: Fighting in the Dark
================================

I had tried all of my standard ways to obtain a foothold on this third engagement, and nothing had worked. I decided that I would use the :ref:`kerbrute` tool to attempt to enumerate valid usernames and then, if I found any, attempt a targeted password spraying attack since I did not know the password policy and did not want to lock any accounts out. I used the linkedin2username tool (https://github.com/initstring/linkedin2username) to first mashup potential usernames from the company's LinkedIn page. I combined this list with several username lists from the statistically-likely-usernames GitHub repo (https://github.com/insidetrust/statistically-likely-usernames) and, after using the userenum feature of :ref:`kerbrute`, ended up with 516 valid users. I knew I had to tread carefully with password spraying, so I tried with the password Welcome2021 and got a single hit! Using this account, I ran the Python version of BloodHound from my attack host and found that all domain users had RDP access to a single box. I logged into this host and used the PowerShell tool DomainPasswordSpray to spray again. I was more confident this time around because I could a) view the password policy and b) the DomainPasswordSpray tool will remove accounts close to lockout from the target list. Being that I was authenticated within the domain, I could now spray with all domain users, which gave me significantly more targets. I tried again with the common password Fall2021 and got several hits, all for users not in my initial wordlist. I checked the rights for each of these accounts and found that one was in the Help Desk group, which had GenericAll rights over the Enterprise Key Admins group (https://bloodhound.readthedocs.io/en/latest/data-analysis/edges.html#genericall). The Enterprise Key Admins group had GenericAll privileges over a domain controller, so I added the account I controlled to this group, authenticated again, and inherited these privileges. Using these rights, I performed the :ref:`shadow credentials abusing` attack and retrieved the NT hash for the domain controller machine account. With this NT hash, I was then able to perform a DCSync attack and retrieve the NTLM password hashes for all users in the domain because a domain controller can perform replication, which is required for DCSync.
