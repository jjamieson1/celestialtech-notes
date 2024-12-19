responder
##########

Date: 2024-11-21 11:02

Status:

Description
***************

This package contains Responder/MultiRelay, an LLMNR, NBT-NS and MDNS
poisoner. It will answer to specific NBT-NS (NetBIOS Name Service)
queries based on their name suffix
(see: http://support.microsoft.com/kb/163409).
By default, the tool will only answer to File Server Service request,
which is for SMB.

The concept behind this is to target your answers, and be stealthier on
the network. This also helps to ensure that you don’t break legitimate
NBT-NS behavior. You can set the -r option via command line if you want
to answer to the Workstation Service request name suffix.

Installation
**************

.. code-block:: console

   git clone https://github.com/lgandx/Responder

Configuration
**************

.. code-block:: console

   cat Responder.conf

Usage
*********

.. code-block:: console

   pyenv activate htb
   python responder -I {network iface}

-I to specify the network interface.

References
***********
https://pentestlab.blog/2017/12/13/smb-share-scf-file-attacks/
https://www.kali.org/tools/responder/
