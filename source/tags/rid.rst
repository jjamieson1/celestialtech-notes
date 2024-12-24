rid 
####

Date: 2024-12-23 17:04:23

Tags: #new

Status: 

Description
*************
A unique identifier (represented in hexadecimal format) utilized by Windows to track and identify objects.
here are accounts that you will notice that have the same RID regardless of what host you are on. Accounts 
like the built-in Administrator for a domain will have a RID [administrator] rid:[0x1f4], which, when converted 
to a decimal value, equals 500. The built-in Administrator account will always have the RID value Hex 0x1f4, or 500. 

This will always be the case. Since this value is unique to an object, we can use it to enumerate further information about it from the domain. 



References
***********
https://docs.microsoft.com/en-us/windows/security/identity-protection/access-control/security-identifiers
