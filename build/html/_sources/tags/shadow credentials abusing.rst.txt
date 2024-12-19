shadow credentials abusing
##########################


Date: 2024-12-19 13:29:19

Status: #complete

Tags: :ref:`Active Directory Enumeration Attacks`

Description
***********

The techniques for DACL-based attacks against User and Computer objects in Active Directory have been established for years. If we compromise an account that has delegated rights over a user account, we can simply reset their password, or, if we want to be less disruptive, we can set an SPN or disable Kerberos pre-authentication and try to roast the account. For computer accounts, it is a bit more complicated, but RBCD can get the job done.

References
**********
https://posts.specterops.io/shadow-credentials-abusing-key-trust-account-mapping-for-takeover-8ee1a53566ab