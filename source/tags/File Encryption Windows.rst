############################
File Encryption Windows
############################


Date: 2024-11-29 18:42

Status:

Tags:

Description
*****************


Command line examples to encrypt text

.. code-block:: console

   Invoke-AESEncryption -Mode Encrypt -Key "p@ssword" -Text "Secret Text"

To decrypt the text use :

.. code-block:: console

   Invoke-AESEncryption -Mode Decrypt -Key "p@ssword" -Text 
   "LtxcRelxrDLrDB9rBD6JrfX/czKjZ2CUJkrg++kAMfs"
