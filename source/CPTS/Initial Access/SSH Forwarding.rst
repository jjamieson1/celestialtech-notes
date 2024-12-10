################
SSH Forwarding
################

*****************
Description
*****************
After scanning a host, we notice that the Mysql port is closed, and is only accessible from the localhost.  By leveraging our access to SSH we can forward requests via an SSH tunnel.

Example 1:  Creating a tunnel with local port access
.. code-block:: bash
   
   ssh -L 1234:localhost:3306 ubuntu@10.129.202.64

Connect to the port with Mysql:

.. code-block:: console

   mysql -u root -p -P 1234

==============================
Forwarding Multiple Ports
==============================

Example:  Forwarding ports 3306 and 80 back to 1234, 8080

.. code-block:: console

   ssh -L 1234:localhost:3306 -L 8080:localhost:80 ubuntu@10.129.202.64

