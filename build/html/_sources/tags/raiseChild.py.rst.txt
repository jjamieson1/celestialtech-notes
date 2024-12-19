raiseChild.py
###############

Date: 2024-12-19 14:57:10

Status:

Tags:

Description
***********

 This script implements a child-domain to forest privilege escalation
   as detailed by Sean Metcalf (@PyroTek3) at https://adsecurity.org/?p=1640. We will
   be (ab)using the concept of Golden Tickets and ExtraSids researched and implemented
   by Benjamin Delpy (@gentilkiwi) in mimikatz (https://github.com/gentilkiwi/mimikatz).
   The idea of automating all these tasks came from @mubix.

   The workflow is as follows:
       Input:
           1) child-domain Admin credentials (password, hashes or aesKey) in the form of 'domain/username[:password]'
              The domain specified MUST be the domain FQDN.
           2) Optionally a pathname to save the generated golden ticket (-w switch)
           3) Optionally a target-user RID to get credentials (-targetRID switch)
              Administrator by default.
           4) Optionally a target to PSEXEC with the target-user privileges to (-target-exec switch).
              Enterprise Admin by default.

       Process:
           1) Find out where the child domain controller is located and get its info (via [MS-NRPC])
           2) Find out what the forest FQDN is (via [MS-NRPC])
           3) Get the forest's Enterprise Admin SID (via [MS-LSAT])
           4) Get the child domain's krbtgt credentials (via [MS-DRSR])
           5) Create a Golden Ticket specifying SID from 3) inside the KERB_VALIDATION_INFO's ExtraSids array
              and setting expiration 10 years from now
           6) Use the generated ticket to log into the forest and get the target user info (krbtgt/admin by default)
           7) If file was specified, save the golden ticket in ccache format
           8) If target was specified, a PSEXEC shell is launched

       Output:
           1) Target user credentials (Forest's krbtgt/admin credentials by default)
           2) A golden ticket saved in ccache for future fun and profit
           3) PSExec Shell with the target-user privileges (Enterprise Admin privileges by default) at target-exec
              parameter.

   IMPORTANT NOTE: Your machine MUST be able to resolve all the domains from the child domain up to the
                   forest. Easiest way to do is by adding the forest's DNS to your resolv.conf or similar

   E.G:
   Just in case, Microsoft says it all (https://technet.microsoft.com/en-us/library/cc759073(v=ws.10).aspx):
     A forest is the only component of the Active Directory logical structure that is a security boundary.
     By contrast, a domain is not a security boundary because it is not possible for administrators from one domain
     to prevent a malicious administrator from another domain within the forest from accessing data in their domain.
     A domain is, however, the administrative boundary for managing objects, such as users, groups, and computers.
     In addition, each domain has its own individual security policies and trust relationships with other domains.

References
**********
https://github.com/fortra/impacket/blob/master/examples/raiseChild.py