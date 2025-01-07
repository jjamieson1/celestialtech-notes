Access Control List (ACL) Abuse Primer
###########################################

Date: 2024-12-30 10:20:20

Status: #new

Tags: :ref:`active directory enumeration attacks`


Types of Access Control
***************************

**DACL**

(Discretionary Access Control List) defines which security principals are granted of denied access to an object.  They are made up of ACE's 
that either allow/deny access. 

**SACL**

(System Access Control Lists) Allows admins to log access attempts to secured objects. 

Access Control Entries (ACEs)
*********************************

Three main types of ACEs:

- Access Denied 
- Access Allowed
- System Audit 

Each ACE is made up of 4 components:

- System Identifier (SID) of the user or group
- A flag denoting the type of ACE 
- A set of flags denoting inheritance 
- An access mask 

Abusing ACLs
****************

1. ForceChangePassword: Gives the right to reset a users password without knowing the old password. 
2. GenericWrite: Gives write access to any non-protected attribute on an object. If we have this on a user, we can assign them an SPN and perform a kerberoasting attack.
3. AddSelf: add yourself to a security group.
4. GenericAll: Grants full control over an object.

Possible ACE attacks and tools needed
***************************************

.. image:: ../../img/ACL_attacks_graphic.png


References
***************
https://academy.hackthebox.com/module/143/section/1456