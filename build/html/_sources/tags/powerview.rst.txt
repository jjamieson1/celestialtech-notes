powerview
#########

Date: 2024-12-19 13:57:40

Status:

Tags: 

Description
***********
A PowerShell tool and a .NET port of the same used to gain situational awareness in AD. These tools can be used as replacements for various Windows net* commands and more. PowerView and SharpView can help us gather much of the data that BloodHound does, but it requires more work to make meaningful relationships among all of the data points. These tools are great for checking what additional access we may have with a new set of credentials, targeting specific users or computers, or finding some "quick wins" such as users that can be attacked via Kerberoasting or ASREPRoasting.

is a tool written in PowerShell to help us gain situational awareness within an AD environment. Much like BloodHound, it provides a way to identify where users are logged in on a network, enumerate domain information such as users, computers, groups, ACLS, trusts, hunt for file shares and passwords, perform Kerberoasting, and more. It is a highly versatile tool that can provide us with great insight into the security posture of our client's domain. It requires more manual work to determine misconfigurations and relationships within the domain than BloodHound but, when used right, can help us to identify subtle misconfigurations.

Let's examine some of PowerView's capabilities and see what data it returns. The table below describes some of the most useful functions PowerView offers.


`Export-PowerViewCSV`	Append results to a CSV file
`ConvertTo-SID`	        Convert a User or group name to its SID value
`Get-DomainSPNTicket`	Requests the Kerberos ticket for a specified Service Principal Name (SPN) account

**Domain/LDAP Functions:**	

`Get-Domain`	                Will return the AD object for the current (or specified) domain
`Get-DomainController`	        Return a list of the Domain Controllers for the specified domain
`Get-DomainUser`	            Will return all users or specific user objects in AD
`Get-DomainComputer`	        Will return all computers or specific computer objects in AD
`Get-DomainGroup`	            Will return all groups or specific group objects in AD
`Get-DomainOU`	                Search for all or specific OU objects in AD
`Find-InterestingDomainAcl`	    Finds object ACLs in the domain with modification rights set to non-built in objects
`Get-DomainGroupMember`	        Will return the members of a specific domain group
`Get-DomainFileServer`	        Returns a list of servers likely functioning as file servers
`Get-DomainDFSShare`	        Returns a list of all distributed file systems for the current (or specified) domain

**GPO Functions:**	

`Get-DomainGPO`             	Will return all GPOs or specific GPO objects in AD
`Get-DomainPolicy`	            Returns the default domain policy or the domain controller policy for the current domain

**Computer Enumeration Functions:**	

`Get-NetLocalGroup`	            Enumerates local groups on the local or a remote machine
`Get-NetLocalGroupMember`	    Enumerates members of a specific local group
`Get-NetShare`	                Returns open shares on the local (or a remote) machine
`Get-NetSession`	            Will return session information for the local (or a remote) machine
`Test-AdminAccess`	            Tests if the current user has administrative access to the local (or a remote) machine

**Threaded 'Meta'-Functions:**	

`Find-DomainUserLocation`	        Finds machines where specific users are logged in
`Find-DomainShare`	                Finds reachable shares on domain machines
`Find-InterestingDomainShareFile`	Searches for files matching specific criteria on readable shares in the domain
`Find-LocalAdminAccess`	            Find machines on the local domain where the current user has local administrator access

**Domain Trust Functions:**	

`Get-DomainTrust`	            Returns domain trusts for the current domain or a specified domain
`Get-ForestTrust`           	Returns all forest trusts for the current forest or a specified forest
`Get-DomainForeignUser`	        Enumerates users who are in groups outside of the user's domain
`Get-DomainForeignGroupMember`	Enumerates groups with users outside of the group's domain and returns each foreign member
`Get-DomainTrustMapping`	    Will enumerate all trusts for the current domain and any others seen.


References
**********
https://github.com/PowerShellMafia/PowerSploit/blob/master/Recon/PowerView.ps1