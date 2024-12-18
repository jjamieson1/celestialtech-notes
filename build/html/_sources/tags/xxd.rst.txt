xxd
###

Description
***************
Decodes a hex string back to ASCII

Usage
*******
Encode

.. code-block:: console

   Temen@htb[/htb]$ echo https://www.hackthebox.eu/ | xxd -p

Decode

.. code-block:: console

   Temen@htb[/htb]$ echo 68747470733a2f2f7777772e6861636b746865626f782e65752f0a | xxd -p -r
