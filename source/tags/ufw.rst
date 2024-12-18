ufw
#####

Date: 2024-11-25 09:22

Status:


uncomplicated firewall

Details
***********

Usage
*************

Example 1: install and Enable service

.. code-block:: console

   sudo apt install ufw
   sudo ufw enable

Example 2: List named services

.. code-block:: console

   sudo ufw app list

Example 3: Open https to the world

.. code-block:: console

   sudo ufw allow 'Apache Secure'

Example 4: Show firewall rules

.. code-block:: console

   sudo ufw status

Example 5: Allow from network

.. code-block:: console

   sudo ufw allow from 192.168.86.0/24 to any port 22
   sudo ufw limit 22/tcp comment 'Allow 6 connections over 30 seconds'

Ultra Secure on a server
**************************

.. code-block:: console

   sudo ufw default deny incoming
   sudo ufw default deny outgoing
   sudo ufw allow in 443/tcp
   sudo ufw allow out 80/tcp
   sudo ufw allow out 443/tcp
   sudo ufw allow in 22/tcp
   sudo ufw allow out 53/udp
   sudo ufw enable

References
***************
https://scalastic.io/en/ufw-fail2ban-nginx/#step-3-understanding-how-fail2ban-works
