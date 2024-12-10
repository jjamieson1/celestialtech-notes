############
fail2ban
############


Date: 2024-11-29 18:42

Status:

Tags:

*****************
Description
*****************

******************
Installation
******************

.. code-block:: console

    sudo apt update && sudo apt install fail2ban

***************
configuration
***************

.. code-block:: console

    sudo vi /etc/fail2ban/jail.d/custom.conf 


    [DEFAULT] 
    bantime = 1d 
    findtime = 1d 
    ignoreip = 127.0.0.1/8 192.168.86.0/24
    maxretry = 1 
    banaction = ufw 
    banaction_allports = ufw


*****************
Usage
*****************

.. code-block:: console

    # Enable the service
    sudo systemctl enable fail2ban

    # Monitor
    sudo fail2ban-client status

*****************
References
*****************
