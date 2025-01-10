Initial Enumeration of a AD Domain
##################################

Date: 2024-12-30 10:20:20

Status: #new

Tags: :ref:`active directory enumeration attacks`

----


Options to allow an initial foothold in a network to begin enumeration 
************************************************************************

1. A Virtual machine with VPN provided
2. A physical device plugged into a ethernet port with VPN
3. Physical presence in their office 
4. A Linux VM in the cloud with access to the internal network
5. VPN access into the network
6. From a corporate laptop connected by VPN
7. On a managed workstation

Mapping out the network
***********************

During the enumeration stage, we have access to tools like:  

1. fping 
2. responder
3. nmap 
4. tcpdump 

To start discovering hosts on various networks. 

.. code-block:: console

    fping -asgq 172.16.5.0/23

If we save the host list to a file, we can further enumerate the host for services and OS detection

.. code-block:: console

    sudo nmap -v -A -iL hosts.txt -oN output.txt

Identifying users
*****************

When no initial user is provided, there are techniques to identify users to work with:

Kerbrute
=========

See installation and usage :ref: `../../tags/kerbrute`

From Kerbrute we now have a list of usernames we can use in a password spray attack. 

About AD privileges
*******************

The `local system account <https://docs.microsoft.com/en-us/windows/win32/services/localsystem-account>`_ `NT Authority\SYSTEM` has the highest access
and is used to run most services. If this machine is part of a domain, it can be used to enumerate other machines in the domain.

Ways to get System level access
*******************************

1. Remote Windows exploits such as MS08-067, EternalBlue, or BlueKeep.
2. Abusing a service running in the context of the SYSTEM account, or abusing the service account SeImpersonate privileges using Juicy Potato. This type of attack is possible on older Windows OS' but not always possible with Windows Server 2019.
3. Local privilege escalation flaws in Windows operating systems such as the Windows 10 Task Scheduler 0-day.
4. Gaining admin access on a domain-joined host with a local account and using Psexec to launch a SYSTEM cmd window

How is a System account used
****************************
1. Enumerate the domain using built-in tools or offensive tools such as BloodHound and PowerView.
2. Perform Kerberoasting / ASREPRoasting attacks within the same domain.
3. Run tools such as Inveigh to gather Net-NTLMv2 hashes or perform SMB relay attacks.
4. Perform token impersonation to hijack a privileged domain user account.
5. Carry out ACL attacks.

References
**********
https://academy.hackthebox.com/module/143/section/1265s