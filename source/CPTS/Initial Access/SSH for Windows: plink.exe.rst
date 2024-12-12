SSH for Windows: plink.exe
##########################

Date: 

Status: 

Tags: #Pivoting Around Obstacles

Date: 2024-11-02 14:33


A Windows SSH tools that is part of Putty.  This is often installed on Windows servers for management.  
plink.exe can also be used as a SOCKS proxy and forward ports. 

Example 1:  Starting plink.exe

.. code-block:: console

    plink -ssh -D 9050 ubuntu@10.129.15.50

proxifier
*********
This is another tool that can be used to start a SOCKS tunnel via the SSH session created above.  


References
**********
https://academy.hackthebox.com/module/158/section/1431

