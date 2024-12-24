rpcclient
##############

Date: 2024-11-09 15:28

Status:

Description
**************

A tool to interact with MS-RPC services

Example:

.. code-block:: console

   rpcclient -U "%" 10.129.14.128

Once connected these commands can be run:

``srvinfo`` Server information.

``enumdomains`` Enumerate all domains that are deployed in the network.

``querydominfo`` Provides domain, server, and user information of deployed domains.

``netshareenumall`` Enumerates all available shares.

``netsharegetinfo <share>`` Provides information about a specific share.

``enumdomusers`` Enumerates all domain users.

.. code-block:: bash

   rpcclient $> enumdomusers

   user:[administrator] rid:[0x1f4]
   user:[guest] rid:[0x1f5]
   user:[krbtgt] rid:[0x1f6]
   user:[lab_adm] rid:[0x3e9]
   <SNIP>

``queryuser <RID>`` Provides information about a specific user.

``setuserinfo2`` user level ‘password’ Set the password of user with operating control

RPCClient User Enumeration By RID
**********************************

.. code-block:: bash

   queryuser 0x457

   User Name   :   htb-student
   Full Name   :   Htb Student
   Home Drive  :
   <SNIP>



Brute forcing RID’s
********************

You can use the above command in a loop:

.. code-block:: console



   for i in $(seq 500 1100);do rpcclient -N -U "" 10.129.14.128 -c "queryuser 0x$(printf '%x\n' $i)" | grep "User Name\|user_rid\|group_rid" && echo "";done

Or use the Impacket tool called samrdump.py:

.. code-block:: console

    samrdump.py 10.129.14.128

Example: Changing a users password that you have operational control
over

.. code-block:: console

   rpcclient $> setuserinfo2 adminuser 23 'ASDqwe123'

References
****************
https://academy.hackthebox.com/module/112/section/1067

Setting a password with limited capabilities
https://malicious.link/posts/2017/reset-ad-user-password-with-linux/

What does a level mean
https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-samr/6b0dff90-5ac0-429a-93aa-150334adabf6?redirectedfrom=MSDN
