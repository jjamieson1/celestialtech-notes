princeprocessor
##################

PRINCE or PRobability INfinite Chained Elements

Description
*************

Creates word list by con-catting words from other lists

Installation
*************

.. code-block:: console

   Temen@htb[/htb]$ wget https://github.com/hashcat/princeprocessor/releases/download/v0.22/princeprocessor-0.22.7z
   Temen@htb[/htb]$ 7z x princeprocessor-0.22.7z
   Temen@htb[/htb]$ cd princeprocessor-0.22
   Temen@htb[/htb]$ ./pp64.bin -h

Usage
******

.. code-block:: console

   ./pp64.bin --pw-min=10 --pw-max=25 -o wordlist.txt < words
