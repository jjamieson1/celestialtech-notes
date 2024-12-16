nessus 
#######

Date: 2024-11-04 11:34

Status:

Tags:

Description
*************

Nessus is a remote security scanning tool, which scans a computer and
raises an alert if it discovers any vulnerabilities that malicious
hackers could use to gain access to any computer you have connected to a
network. It does this by running over 1200 checks on a given computer,
testing to see if any of these attacks could be used to break into the
computer or otherwise harm it.

Installation
**************

Step 1: Download

.. code-block:: console

   curl --request GET \
     --url 'https://www.tenable.com/downloads/api/v2/pages/nessus/files/Nessus-10.8.3-ubuntu1604_amd64.deb' \
     --output 'Nessus-10.8.3-ubuntu1604_amd64.deb'

Step 2: Install

.. code-block:: console

   sudo dpkg -i /tmp/Nessus-10.4.2-ubuntu1404_amd64.deb

Step 3: Configure to start as a service

.. code-block:: console

   sudo systemctl enable nessusd
   sudo systemctl start nessusd

Step 4: Verify it is reachable

.. code-block:: console

   curl --insecure https://localhost:8834/

References
*************
https://www.tenable.com/products/nessus/nessus-professional
