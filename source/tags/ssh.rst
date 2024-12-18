ssh
#####

Date: 2024-11-11 18:07

Status:

Configuration
******************
.. code-block:: console

   cat  /etc/ssh/sshd_config  | grep -v "#" | sed -r '/^\s*$/d'

Example 2: force password on connection

.. code-block:: console

   ssh -l test -o PreferredAuthentications=password -o PubkeyAuthentication=no hostname

Footprinting
**************

ssh-audit
===========
A tool to find out what algorithms are in use and the banner

Example: installing and using the tool

.. code-block:: console

    git clone https://github.com/jtesta/ssh-audit.git && cd ssh-audit
    ./ssh-audit.py 10.129.14.132

Example 2: Specifying the password to brute force

.. code-cblock:: console

   ssh -v cry0l1t3@10.129.14.132 -o PreferredAuthentications=password

References
***********
https://academy.hackthebox.com/module/112/section/1240
