nmap
#####

Date: 2024-11-09 14:48

Status:

nmap Description
*****************

Versatile network scanner that can be used for various reconnaissance
tasks, including service and OS fingerprinting. ## Features Can be used
with scripts (NSE) to perform more specialised fingerprinting.

nmap Options
**************

Returning RST flag means the port is closed. target port responds with
an ``SYN-ACK`` packet and closed if it responds with an ``RST``\ packet.

Example 1: OS Host detection

.. code-block:: console


   sudo nmap -v -O 192.168.86.39

Example 2: Banner Grab to Enumerate Ports

.. code-block:: console

   sudo nmap -v 192.168.86.39 --script banner.nse

Example 3: You can update the nmap database with:

.. code-block:: console

   sudo nmap --script-updatedb

nmap Ping Sweep
****************
.. code-block:: console

   nmap -sn 10.0.0.0/24

Adding –script-trace to the nmap command will show which scripts are
running during the scan

nmap Checking for a SMTP open-relay
*************************************

.. code-block:: console

    nmap -p25 -Pn --script smtp-open-relay 10.10.11.213

References
****************
https://academy.hackthebox.com/module/144/section/3075
