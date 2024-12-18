Hunting for Files
###################

Date: 2024-11-28 10:14

Status:

Description
*************
Looking for useful files to leverage to escalate privileges

Usage
*******

Example 1: On Linux looking for password protected files

.. code-block:: console

   for ext in $(echo ".xls .xls* .xltx .csv .od* .doc .doc* .pdf .pot .pot* .pp*");do echo -e "\nFile extension: " $ext; find / -name *$ext 2>/dev/null | grep -v "lib\|fonts\|share\|core" ;done

Example 2: Looking for SSH keys

.. code-block:: console

   grep -rnw "PRIVATE KEY" /* 2>/dev/null | grep ":1"

Cracking encryption on Files/Archives
******************************************

**Encrypted SSH Keys:**  These need a passphrase before use. They will
have the designation in the header "Proc-Type: 4, ENCRYPTED"

:ref:`john` has many utilities from converting a file to a hash that
can be cracked.

**Example 1:** Converting an encryptyed key top a hash

.. code-block:: console

   ssh2john.py SSH.private > ssh.hash

Then using John to crack the password
:ref:`john` Example 1 Cracking an SSH Key

John has hash extraction tools for all the popular programs that can
encrypt.

**Example 2:** OpenSSL can be used to encrypt an archive too. There is a
handy for loop to guess the password
:ref:`openssl` Guessing the password of the Openssl encrypted file

**Example 3:** Cracking :ref:`Bitlocker`

References
*************
https://academy.hackthebox.com/module/147/section/1322
