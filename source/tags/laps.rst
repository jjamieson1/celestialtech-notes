laps
#####

Date: 2024-12-19 14:14:49

Status: 

Tags:

Description
***********
Microsoft Local Administrator Password Solution (LAPS) provides automated local administrator account management for every computer in Active Directory (LAPS is best for workstation local admin passwords). A client-side component installed on every computer generates a random password, updates the (new) LAPS password attribute on the associated AD computer account, and sets the password locally. LAPS configuration is managed through Group Policy which provides the values for password complexity, password length, local account name for password change, password change frequency, etc.


References
**********
https://adsecurity.org/?p=1790