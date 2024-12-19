#######################
Host Based Enumeration
#######################

Status: draft

Date: 2024-11-09 14:48

Tags: "ref":`fierce <fierce>`

******
FTP
******

================
General Notes 
================

Always try anonymous login if it is available: 

.. code-block:: console

   ftp 172.16.10.10
   Username: anonymous
   Password: anonymous (or keys you want to put in.)

================
FTP nmap Scan
================
Listing all the possible scripts that can be run in nmap

.. code-block:: console

    $ ls -lh /usr/share/nmap/scripts/ | grep ftp
    -rw-r--r-- 1 root root 4.5K Oct 12 09:29 ftp-anon.nse
    -rw-r--r-- 1 root root 3.2K Oct 12 09:29 ftp-bounce.nse
    -rw-r--r-- 1 root root 3.1K Oct 12 09:29 ftp-brute.nse
    -rw-r--r-- 1 root root 3.2K Oct 12 09:29 ftp-libopie.nse
    -rw-r--r-- 1 root root 3.3K Oct 12 09:29 ftp-proftpd-backdoor.nse
    -rw-r--r-- 1 root root 3.7K Oct 12 09:29 ftp-syst.nse
    -rw-r--r-- 1 root root 5.9K Oct 12 09:29 ftp-vsftpd-backdoor.nse
    -rw-r--r-- 1 root root 5.8K Oct 12 09:29 ftp-vuln-cve2010-4221.nse
    -rw-r--r-- 1 root root 5.7K Oct 12 09:29 tftp-enum.nse

.. code-block:: console

    nmap x.x.x.x -p 21 -sV --script=exampleScript1.nse,exampleScript2.nse

================================
FTP Bounce attack with nmap
================================
By exploiting FTP we can scan another target on the same network that is not connected to the public internet.

.. code-block::  console

    nmap -Pn -v -n -p80 anonymous:password@10.10.110.213 172.17.0.2

================================
Manual Connection with nc
================================

.. code-block:: console

    nc -vn 172.16.10.10 21

================================
Connect with a browser
================================

.. code-block:: console

    ftp://172.16.10.10


================================
Examples using netexec
================================

.. code-block:: console

    netexec ftp 172.21.0.0
    netexec ftp 172.21.0.0 -u 'a' -p ''
    netexec ftp 172.21.0.0 -u 'anonymous' -p '''


******
SMB
******
================================
Enumerating version with nmap
================================

.. code-block:: console

    sudo nmap 10.129.14.128 -sV -sC -p139,445

================================
Using scripts with nmap
================================

listing all scripts:

.. code-block:: console

    jjamieso@fatmex:/usr/share/nmap/scripts$ ls -l smb*
    -rw-r--r-- 1 root root  3753 Apr  1  2024 smb2-capabilities.nse
    -rw-r--r-- 1 root root  2689 Apr  1  2024 smb2-security-mode.nse
    -rw-r--r-- 1 root root  1408 Apr  1  2024 smb2-time.nse
    -rw-r--r-- 1 root root  5269 Apr  1  2024 smb2-vuln-uptime.nse
    -rw-r--r-- 1 root root 45061 Apr  1  2024 smb-brute.nse
    -rw-r--r-- 1 root root  5289 Apr  1  2024 smb-double-pulsar-backdoor.nse
    -rw-r--r-- 1 root root  4840 Apr  1  2024 smb-enum-domains.nse
    -rw-r--r-- 1 root root  5971 Apr  1  2024 smb-enum-groups.nse
    -rw-r--r-- 1 root root  8043 Apr  1  2024 smb-enum-processes.nse
    -rw-r--r-- 1 root root 27274 Apr  1  2024 smb-enum-services.nse
    -rw-r--r-- 1 root root 12017 Apr  1  2024 smb-enum-sessions.nse
    -rw-r--r-- 1 root root  6923 Apr  1  2024 smb-enum-shares.nse
    -rw-r--r-- 1 root root 12527 Apr  1  2024 smb-enum-users.nse
    -rw-r--r-- 1 root root  4418 Apr  1  2024 smb-flood.nse
    -rw-r--r-- 1 root root  7471 Apr  1  2024 smb-ls.nse
    -rw-r--r-- 1 root root  8758 Apr  1  2024 smb-mbenum.nse
    -rw-r--r-- 1 root root  8220 Apr  1  2024 smb-os-discovery.nse
    -rw-r--r-- 1 root root  4982 Apr  1  2024 smb-print-text.nse
    -rw-r--r-- 1 root root  1833 Apr  1  2024 smb-protocols.nse
    -rw-r--r-- 1 root root 63596 Apr  1  2024 smb-psexec.nse
    -rw-r--r-- 1 root root  5190 Apr  1  2024 smb-security-mode.nse
    -rw-r--r-- 1 root root  2424 Apr  1  2024 smb-server-stats.nse
    -rw-r--r-- 1 root root 14159 Apr  1  2024 smb-system-info.nse
    -rw-r--r-- 1 root root  7524 Apr  1  2024 smb-vuln-conficker.nse
    -rw-r--r-- 1 root root  6402 Apr  1  2024 smb-vuln-cve2009-3103.nse
    -rw-r--r-- 1 root root 23154 Apr  1  2024 smb-vuln-cve-2017-7494.nse
    -rw-r--r-- 1 root root  6545 Apr  1  2024 smb-vuln-ms06-025.nse
    -rw-r--r-- 1 root root  5386 Apr  1  2024 smb-vuln-ms07-029.nse
    -rw-r--r-- 1 root root  5688 Apr  1  2024 smb-vuln-ms08-067.nse
    -rw-r--r-- 1 root root  5647 Apr  1  2024 smb-vuln-ms10-054.nse
    -rw-r--r-- 1 root root  7214 Apr  1  2024 smb-vuln-ms10-061.nse
    -rw-r--r-- 1 root root  7344 Apr  1  2024 smb-vuln-ms17-010.nse
    -rw-r--r-- 1 root root  4400 Apr  1  2024 smb-vuln-regsvc-dos.nse
    -rw-r--r-- 1 root root  6586 Apr  1  2024 smb-vuln-webexec.nse
    -rw-r--r-- 1 root root  5084 Apr  1  2024 smb-webexec-exploit.nse

Using scripts:

.. code-block:: console

    nmap x.x.x.x -p139,445 -sV --script=exampleScript1.nse,exampleScript2.nse

================================
Anonymous Authentication 
================================

Example 1:  Listing shares

.. code-block:: console

    smbclient -N -L //10.10.10.10

Example 2: Connecting anonymously

.. code-block:: console

    smbclient //10.10.10.10/notes

================================
Using rpcclient
================================

.. code-block:: console

    rpcclient -U "%" 10.10.10.10

Once connected in the rpcclient console, use help to see all the available commands that can be run. 

================================
SMBMap Enumeration
================================

Example 1: enumeration

.. code-block:: console

     smbmap -H 10.129.14.128

    [+] Finding open SMB ports....
    [+] User SMB session established on 10.129.14.128...
    [+] IP: 10.129.14.128:445       Name: 10.129.14.128                                     
            Disk                                                    Permissions     Comment
            ----                                                    -----------     -------
            print$                                                  NO ACCESS       Printer Drivers
            home                                                    NO ACCESS       INFREIGHT Samba
            dev                                                     NO ACCESS       DEVenv
            notes                                                   NO ACCESS       CheckIT
            IPC$                                                    NO ACCESS       IPC Service (DEVSM)

Example 2: recursive listing of files

.. code-block:: console

    smbmap -H 10.10.10.10 -r <sharename>

Example 3: Downloading files 

.. code-block:: console

    smbmap -h 10.10.10.10 --download "notes/note.txt"

================================
Using netexec 
================================

Example 1:  Enumeration

.. code-block:: console

    crackmapexec smb 10.129.248.196 --shares -u 'alex' -p 'lol123!mD' -d 'WINMEDIUM'

    SMB         10.129.248.196  445    WINMEDIUM        [*] Windows 10.0 Build 17763 x64 (name:WINMEDIUM) (domain:WINMEDIUM) (signing:False) (SMBv1:False)
    SMB         10.129.248.196  445    WINMEDIUM        [+] WINMEDIUM\alex:lol123!mD 
    SMB         10.129.248.196  445    WINMEDIUM        [*] Enumerated shares
    SMB         10.129.248.196  445    WINMEDIUM        Share           Permissions     Remark
    SMB         10.129.248.196  445    WINMEDIUM        -----           -----------     ------
    SMB         10.129.248.196  445    WINMEDIUM        ADMIN$                          Remote Admin
    SMB         10.129.248.196  445    WINMEDIUM        C$                              Default share
    SMB         10.129.248.196  445    WINMEDIUM        devshare        READ,WRITE      
    SMB         10.129.248.196  445    WINMEDIUM        IPC$            READ            Remote IPC
    SMB         10.129.248.196  445    WINMEDIUM        Users           READ         

================================
Enumeration with enum4linux-ng
================================

Example 1: Anonymous enumeration

.. code-block:: console

    ./enum4linux-ng.py 10.10.10.10 -A -C 
       
Example 2: With credentials

.. code-block:: console

    ./enum4linux-ng.py 10.10.11.42 -u user -p 'password' -oY out
    

*****
NFS
*****

Example 1:  nmap scan

.. code-block:: console

    sudo nmap 10.129.14.128 -p111,2049 -sV -sC


Example 2: Using an NFS script

.. code-block:: console

    jjamieso@fatmex:/usr/share/nmap/scripts$ ls -l nfs*
    -rw-r--r-- 1 root root 14534 Apr  1  2024 nfs-ls.nse
    -rw-r--r-- 1 root root  2714 Apr  1  2024 nfs-showmount.nse
    -rw-r--r-- 1 root root  9947 Apr  1  2024 nfs-statfs.nse

    sudo nmap --script nfs*.nse 10.129.14.128 -sV -p111,2049

Example 3: Listing shares on an NFS server

.. code-block:: console

    showmount -e 10.129.14.128

    # Then to mount the share

    mkdir target-NFS
    sudo mount -t nfs 10.129.14.128:/ ./target-NFS/ -o nolock
    cd target-NFS

    ## Unmount the share
    cd / 
    sudo umount /target-NFS

*****
DNS
*****

Example 1: Enumerating and looking for zone transfers

.. code-block:: console

    fierce --domain xyz.com --dns-servers 1.1.1.1

Example 2: Other DNS servers

.. code-block:: console

    dig ns inlanefreight.htb @10.129.14.128

Example 3:  Sometime you can get the version information with the CHAOS query and TXT

.. code-block:: console 

    dig CH TXT version.bind 10.129.120.85

Example 4: Zone transfer request

.. code-block:: console

    dig axfr inlanefreight.htb @10.129.14.128 

Example 5:Going after internal machines

.. code-block:: console

    dig axfr internal.inlanefreight.htb @10.129.14.128


Example 6: Brute forcing sub-domains (using a wordlist  and loop)

.. code-block:: console

    for sub in $(cat /opt/useful/seclists/Discovery/DNS/subdomains-top1million-110000.txt);do dig $sub.inlanefreight.htb @10.129.14.128 | grep -v ';\|SOA' | sed -r '/^\s*$/d' | grep $sub | tee -a subdomains.txt;done

Example 7: Using using :ref:`dnsenum <dnsenum>`

.. code-block:: console

    dnsenum --dnsserver 10.129.73.113 --enum -p 0 -s 0 -o subdomains.txt -f  /home/jjamieso/HTB/wordlists/SecLists/Discovery/DNS/subdomains-top1million-110000.txt inlanefreight.htb

Example 7: using :ref:`dnsrecon <dnsrecon>`

.. code-block:: console

    dnsrecon -d www.example.com -a 
    dnsrecon -d www.example.com -t axfr
    dnsrecon -d "startIP-endIP"
    dnsrecon -d www.example.com -D "namelist" -t brt

Example 8: Using :ref:`dnsX <dnsx>`

.. code-block:: console

    dnsx -l domains.txt -resp -a -aaaa -cname -mx -ns -soa -txt
    dnsx -silent -d megacorpone.com -w /usr/share/seclists/Discovery/DNS/dns-Jhaddix.txt

Example 9: using :ref:`subfinder <subfinder>`

.. code-block:: console

    subfinder -silent -d megacorpone.com | dnsx -silent
    subfinder -silent -d megacorpone.com | dnsx -silent -a -resp
    subfinder -silent -d megacorpone.com | dnsx -silent -a -resp-only
    subfinder -silent -d megacorpone.com | dnsx -silent -cname -resp
    subfinder -silent -d megacorpone.com | dnsx -silent -asn

Example 10: Using nmap and scripts

.. code-block:: console

    $ ls -lh /usr/share/nmap/scripts/ | grep dns
    -rw-r--r-- 1 root root 1.5K Nov  1  2023 broadcast-dns-service-discovery.nse
    -rw-r--r-- 1 root root 5.3K Nov  1  2023 dns-blacklist.nse
    -rw-r--r-- 1 root root 9.9K Nov  1  2023 dns-brute.nse
    -rw-r--r-- 1 root root 6.5K Nov  1  2023 dns-cache-snoop.nse
    -rw-r--r-- 1 root root  15K Nov  1  2023 dns-check-zone.nse
    -rw-r--r-- 1 root root  15K Nov  1  2023 dns-client-subnet-scan.nse
    -rw-r--r-- 1 root root  10K Nov  1  2023 dns-fuzz.nse
    -rw-r--r-- 1 root root 3.8K Nov  1  2023 dns-ip6-arpa-scan.nse
    -rw-r--r-- 1 root root  13K Nov  1  2023 dns-nsec3-enum.nse
    -rw-r--r-- 1 root root  11K Nov  1  2023 dns-nsec-enum.nse
    -rw-r--r-- 1 root root 3.4K Nov  1  2023 dns-nsid.nse
    -rw-r--r-- 1 root root 4.3K Nov  1  2023 dns-random-srcport.nse
    -rw-r--r-- 1 root root 4.3K Nov  1  2023 dns-random-txid.nse
    -rw-r--r-- 1 root root 1.5K Nov  1  2023 dns-recursion.nse
    -rw-r--r-- 1 root root 2.2K Nov  1  2023 dns-service-discovery.nse
    -rw-r--r-- 1 root root 5.6K Nov  1  2023 dns-srv-enum.nse
    -rw-r--r-- 1 root root 5.7K Nov  1  2023 dns-update.nse
    -rw-r--r-- 1 root root 2.1K Nov  1  2023 dns-zeustracker.nse
    -rw-r--r-- 1 root root  26K Nov  1  2023 dns-zone-transfer.nse
    -rw-r--r-- 1 root root 3.9K Nov  1  2023 fcrdns.nse

    nmap x.x.x.x -v -p 53 --script=exampleScript1.nse,exampleScript2.nse

*****
SMTP
*****

Nowadays it is known as ESMTP (enhanced smtp) using TLS

Example 1: using nmap to get the version

.. code-block:: console
    
    sudo nmap 10.129.14.128 -sC -sV -p25

Example 2: using nmap and scripts

.. code-block:: console

    jjamieso@fatmex:/usr/share/nmap/scripts$ ls -l smtp*
    -rw-r--r-- 1 root root  4309 Apr  1  2024 smtp-brute.nse
    -rw-r--r-- 1 root root  4957 Apr  1  2024 smtp-commands.nse
    -rw-r--r-- 1 root root 12006 Apr  1  2024 smtp-enum-users.nse
    -rw-r--r-- 1 root root  5873 Apr  1  2024 smtp-ntlm-info.nse
    -rw-r--r-- 1 root root 10148 Apr  1  2024 smtp-open-relay.nse
    -rw-r--r-- 1 root root   716 Apr  1  2024 smtp-strangeport.nse
    -rw-r--r-- 1 root root 14781 Apr  1  2024 smtp-vuln-cve2010-4344.nse
    -rw-r--r-- 1 root root  7719 Apr  1  2024 smtp-vuln-cve2011-1720.nse
    -rw-r--r-- 1 root root  7603 Apr  1  2024 smtp-vuln-cve2011-1764.nse

    sudo nmap 10.129.200.67 -p25 --script smtp-* -v

Example 3: :ref:`smtp-user-enum <smtp-user-enum>`

.. code-block:: console

    ./smtp-user-enum.pl -U /home/jjamieso/HTB/footprinting-wordlist.txt -t 10.129.200.67 -t 15 -v


**************
References
**************
https://academy.hackthebox.com/module/112/section/1065
https://academy.hackthebox.com/module/112/section/1062
https://academy.hackthebox.com/module/112/section/1061
https://academy.hackthebox.com/module/112/section/1061
https://academy.hackthebox.com/module/112/section/1067
https://github.com/cddmp/enum4linux-ng
https://academy.hackthebox.com/module/116/section/1512
