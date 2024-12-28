dsquery
########

Date: 2024-12-26 09:03:44

Status: #new

Tags: :ref:`active directory enumeration attacks`

Description
************

A built in utilty for querying Active Directory objects. 

Bloodhound and Powerview are better suited for this task, but if you
are living off the land, this will be your option.

**requires:** elevate privileges, or run from the SYSTEM context. 

Usage 
********

.. list-table:: Examples 
   :widths: 50 50
   :header-rows: 1

   * - Command
     - Description
   * - `dsquery user`
     - List users in the domain 
   * - `dsquery computer`
     - Listing computers in the domain
   * - `dsquery * "CN=Users,DC=INLANEFREIGHT,DC=LOCAL"`
     - Wild card search 
   * - `dsquery * -filter "(&(objectCategory=person)(objectClass=user)(userAccountControl:1.2.840.113556.1.4.803:=32))" -attr distinguishedName userAccountControl`
     - Users With Specific Attributes Set (PASSWD_NOTREQD)
   * - `dsquery * -filter "(userAccountControl:1.2.840.113556.1.4.803:=8192)" -limit 5 -attr sAMAccountName`
     - Searching for Domain Controllers

.. note:: 
    
    When searching for specific details you can create an OID string to look for specifics
    Please refer to https://ldap.com/ldap-oid-reference-guide/ for details.

OID match strings
==================

OIDs are rules used to match bit values with attributes, as seen above. For LDAP and AD, there are three main matching rules:

**1.2.840.113556.1.4.803**

When using this rule as we did in the example above, we are saying the bit value must match completely to meet the search requirements. Great for matching a singular attribute.

**1.2.840.113556.1.4.804**

When using this rule, we are saying that we want our results to show any attribute match if any bit in the chain matches. This works in the case of an object having multiple attributes set.

**1.2.840.113556.1.4.1941**

This rule is used to match filters that apply to the Distinguished Name of an object and will search through all ownership and membership entries.

References
***********
https://ldap.com/ldap-oid-reference-guide/
https://academy.hackthebox.com/module/143/section/1360