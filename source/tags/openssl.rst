openssl
############

Date: 2024-11-28 10:48

Status:


Using OpenSSL
**************

:ref:`Using OpenSSL to send and receive files`
===================================================

Guessing the password of the Openssl encrypted file
======================================================

Example 1.

.. code-block:: console

   for i in $(cat rockyou.txt);do openssl enc -aes-256-cbc -d -in GZIP.gzip -k $i 2>/dev/null| tar xz;done

References
************

