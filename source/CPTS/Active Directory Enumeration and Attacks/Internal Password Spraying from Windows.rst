Internal Password Spraying from Windows
#########################################

Date: 2024-12-20 15:49:28

Status: #new 

Tags: :ref:`active directory enumeration attacks`

----

Description
************

From a foothold domain connected Windows host we can use the :ref:`DomainPasswordSpray` tool.  
If we are authenticated it will create a user list for us, exclude accounts 1 attempt from lockout and
query the password policy. 


There are several options available to us with the tool. Since the host is domain-joined, we will skip the -UserList flag and let the tool generate a list for us. We'll supply the Password flag and one single password and then use the -OutFile flag to write our output to a file for later use.

Example 1: 

.. code-block:: console

    PS C:\htb> Import-Module .\DomainPasswordSpray.ps1
    PS C:\htb> Invoke-DomainPasswordSpray -Password Welcome1 -OutFile spray_success -ErrorAction SilentlyContinue


Example 2: 

Another option is to use the Windows version of :ref:`kerbrute`

Mitigations
************

1. Multi Factor authentication
2. Restricting access with a least privilege approach 
3. Separations of passwords across common accounts
4. Selecting good password, using a password manager with long passwords 

.. warning:: An aggressive password policy leaves you open to account lockouts that have to be manually reset. 

Detection 
***********

1.  Looking for a large number of locked out accounts in a short period. 
2.  Finding many instances of event ID `4625: An account failed to log on`
3.  Finding many instances of event ID `4771: Kerberose Pre-Authentication failed`


Other Considerations of password spray attacks 
**************************************************

By attacking applications that use Windows credentials ( such as O365, Outlook Web Exchange, Skype for business, RPD portals)


References
************
Detecting password spraying [https://www.hub.trimarcsecurity.com/post/trimarc-research-detecting-password-spraying-with-security-event-auditing]