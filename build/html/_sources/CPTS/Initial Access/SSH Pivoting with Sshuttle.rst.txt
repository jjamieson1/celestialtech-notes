SSH Pivoting with Sshuttle
##########################

Date: 2024-11-02 14:33

Status:

Tags: #Pivoting Around Obstacles


Description
***********

A tool written in python that removes the need to configure proxychains.  

Installation
************

.. code-block:: console

    sudo apt install sshuttle


Usage
*****

The -r option connects to the remote machine with a user/pass.  Then we need to specify the network or
IP that we wish to route too.

.. code-block:: console

    sudo sshuttle -r ubuntu@10.129.202.64 172.16.5.0/23 -v 


Example:  Using nmap through this tunnel

.. code-block:: console

    nmap -v -sV -p3389 172.16.5.19 -A -Pn

We can now use any tool directly without using proxychains.

References
**********
https://academy.hackthebox.com/module/158/section/1432