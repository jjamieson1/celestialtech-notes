Celestial Security Documentation
############################################

.. image:: img/hacker_cover.jpeg
   

These are my personal notes that are a perpetual work in progress.  I use these notes to study for various 
industry exams, and I also use them as references during engagements.

.. toctree::
   :maxdepth: 1
   :caption: Hack the Box Certifications

   CPTS/Certified Penetration Tester
   CDSA/Certified Defensive Security Analyst

.. toctree::
   :maxdepth: 1
   :caption: Offensive Methods

   OFSEC/recon/Active Scanning


.. toctree::
   :maxdepth: 1 
   :caption: Overview 

   CPTS/Overview/Introduction to Active Directory
   CPTS/Overview/Penetration Testing Overview
   CPTS/Overview/Types of Penetration testing
   CPTS/Overview/Vulnerability Assessment

.. toctree::
   :maxdepth: 1
   :caption: Reconnaissance

   CPTS/Reconnaissance/Penetration Testing Overview
   CPTS/Reconnaissance/Network Enumeration with nmap
   CPTS/Reconnaissance/Footprinting
   CPTS/Reconnaissance/Infrastructure Enumeration
   CPTS/Reconnaissance/Host Enumeration
   CPTS/Reconnaissance/fingerprinting
   CPTS/Reconnaissance/Initial Enumeration of a AD Domain
   CPTS/Reconnaissance/External Recon and Enumeration Principles
   CPTS/Reconnaissance/Information Gathering

.. toctree::
   :maxdepth: 1
   :caption: Initial Access

   CPTS/Initial Access/File Inclusion
   CPTS/Initial Access/SSH Forwarding
   CPTS/Initial Access/Dynamic Port Forwarding with SSH and SOCKS Tunneling
   CPTS/Initial Access/Remote-Reverse Port Forwarding with SSH
   CPTS/Initial Access/Meterpreter Tunneling and Port Forwarding
   CPTS/Initial Access/Socat Redirection with a Reverse Shell
   CPTS/Initial Access/Socat Redirection with a Bind Shell
   CPTS/Initial Access/SSH for Windows: plink.exe
   CPTS/Initial Access/SSH Pivoting with Sshuttle
   CPTS/Initial Access/Web Server Pivoting with Rpivot
   CPTS/Initial Access/Port Forwarding with Windows Netsh
   CPTS/Initial Access/DNS Tunneling with Dnscat2
   CPTS/Initial Access/SOCKS5 Tunneling with Chisel
   CPTS/Initial Access/ICMP Tunneling with SOCKS
   CPTS/Initial Access/RDP and SOCKS Tunneling with SocksOverRDP
   CPTS/Initial Access/LLMNR NBT-NS Poisoning from Linux
   CPTS/Initial Access/LLMNR NBT-NS Poisoning from Windows
   CPTS/Initial Access/Password Attacks
   CPTS/Initial Access/Remote Password Attacks
   CPTS/Initial Access/Using the Metasploit Framework
   CPTS/Initial Access/Shells and Payloads
   CPTS/Initial Access/Attacking Common Services
   CPTS/Initial Access/Active Directory Enumeration Attacks

.. toctree::
   :maxdepth: 1
   :caption: Lateral Movement

   CPTS/Lateral Movement/File Transfers
   CPTS/Lateral Movement/Changing the user-agent to avoid detection
   CPTS/Lateral Movement/Native File Transfer Powershell 
   CPTS/Lateral Movement/Creating a secure upload server using Nginx
   CPTS/Lateral Movement/Hunting for Files
   CPTS/Lateral Movement/Linux Pass the Ticket
   CPTS/Lateral Movement/Pivoting-Tunneling and Port Forwarding

.. toctree:: 
   :maxdepth: 1
   :caption: Glossary

   tags/Active Directory
   tags/Active Directory Explorer
   tags/ADRecon
   tags/adidnsdump
   tags/apache nutch
   tags/Application Testing
   tags/Attacking AD and NTDS.dit
   tags/Attacking LSASS
   tags/Attacking the SAM
   tags/Base64
   tags/Bash
   tags/bettercap
   tags/Bitlocker
   tags/Black box Testing
   tags/bloodhound
   tags/bloodhound.py
   tags/builtwith
   tags/burp suite
   tags/Certificates
   tags/cewl
   tags/chisel
   tags/Compliance Standards
   tags/crackmapexec
   tags/crawling
   tags/crowbar
   tags/crunch
   tags/cupp
   tags/CVE-2021-1675.py
   tags/CVSS
   tags/d3ad0ne
   tags/DKIM
   tags/domainPasswordSpray
   tags/DMARC
   tags/DNS
   tags/dnsenum
   tags/dnsrecon
   tags/dnsx
   tags/ettercap
   tags/enum4linux-ng
   tags/Evasive testing
   tags/evil-winrm
   tags/extent
   tags/GetNPUsers.py
   tags/fail2ban
   tags/ffuf
   tags/fierce
   tags/File Encryption on Linux
   tags/File Encryption Windows
   tags/finalRecon
   tags/Firefox Decrypt
   tags/FTP
   tags/gettgtpkinit.py
   tags/getnthash.py
   tags/getuserspns.py
   tags/git
   tags/gobuster
   tags/gpp-decrypt
   tags/Grey Box Testing
   tags/Group3r
   tags/hashcat
   tags/hippa
   tags/Hybrid evasive
   tags/hydra
   tags/IMAP-POP3
   tags/impacket
   tags/IPMP
   tags/iso-27001
   tags/inveigh
   tags/invoke-TheHash
   tags/john
   tags/keytab
   tags/keytabextract.py
   tags/kwprocessor
   tags/ldapsearch
   tags/lazagne
   tags/laps
   tags/LAPSToolkit
   tags/linkatz
   tags/Linux local password attacks
   tags/Linux Mount
   tags/lookupsid.py
   tags/kerbrute
   tags/md5sum
   tags/metasploit
   tags/medusa
   tags/Microsoft DREAD
   tags/mimikatz
   tags/mitm6
   tags/msfvenom
   tags/MSSQL
   tags/MySQL
   tags/mssqlclient.py
   tags/nessus
   tags/netcat
   tags/netcraft
   tags/net-webclient
   tags/Network Testing
   tags/NIST
   tags/NFS
   tags/nikto
   tags/nmap
   tags/nopac.py
   tags/netstat
   tags/Non-evasive testing
   tags/O365spray
   tags/openssl
   tags/Oracle TNS
   tags/OSINT Framework
   tags/OSSTMM
   tags/OWASP
   tags/owasp-zap
   tags/pentest
   tags/petitpotam.py
   tags/pci-dss
   tags/Physical Testing
   tags/PingCastle
   tags/powershell
   tags/powerview
   tags/PowerShell Web Uploads
   tags/princeprocessor
   tags/proxychains
   tags/psexec
   tags/psexec.py
   tags/PTES
   tags/pyenv
   tags/raiseChild.py
   tags/r-services
   tags/rdp
   tags/recon-ng
   tags/reconSpider
   tags/responder
   tags/rpc
   tags/rsync
   tags/rpcclient
   tags/rpcinfo
   tags/rcpdump.py
   tags/rubeus
   tags/S3 Buckets
   tags/shadow credentials abusing
   tags/sharpHound
   tags/sharpview
   tags/smb
   tags/smbserver.py
   tags/scrappy
   tags/sc.exe
   tags/secretsdump.py
   tags/setspn.exe
   tags/shells
   tags/smbmap
   tags/SMTP
   tags/smtp-user-enum
   tags/SNMP
   tags/SQL Injection
   tags/snaffler
   tags/Social Engineering Testing
   tags/ssh
   tags/spf
   tags/spiderfoot
   tags/SQL Injection Types
   tags/SQL Load file
   tags/sqlcmd
   tags/sqsh
   tags/subbrute
   tags/sudo
   tags/subfinder
   tags/Subverting SQL Query Logic
   tags/Symmetrical Encryption
   tags/targetedKerberoast.py
   tags/theharvester
   tags/ticketer.py
   tags/Transfer with Code
   tags/Transferring File with GfxDownloadWrapper.exe
   tags/tscon.exe
   tags/ufw
   tags/Python Uploadserver
   tags/Using Bitsadmin to send and receive files
   tags/Using Certutil to download
   tags/Using OpenSSL to send and receive files
   tags/Understanding User Privileges
   tags/Virtual Hosts
   tags/WAF
   tags/wafw00f
   tags/wappalyzer
   tags/web shells
   tags/Webdav
   tags/wget
   tags/whatweb
   tags/White Box Testing
   tags/whois
   tags/windapsearch
   tags/Windows CMD
   tags/Windows Lateral Movement
   tags/Windows Local Password Attacks
   tags/Windows Pass The Hash
   tags/Windows Pass The Ticket
   tags/Windows Passwords
   tags/winrm
   tags/WMI
   tags/wmiexec.py
   tags/wpscan 
   tags/xfreerdp
   tags/xxd
 
