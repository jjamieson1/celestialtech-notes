Creating a secure upload server using Nginx
#################################################

Description
*************

Leaving Apache open to uploads can leave your own server vulnerable to
uploaded shells from other actors. Using Nginx is a good alternative to
prevent this:

Let’s setup a server for this.

Step 1: Create the directory

.. code-block:: console

   Temen@htb[/htb]$ sudo mkdir -p /var/www/uploads/SecretUploadDirectory

Step 2: Change ownership/permissions

.. code-block:: console

   Temen@htb[/htb]$ sudo chown -R www-data:www-data /var/www/uploads/SecretUploadDirectory

Step 3: Create the config file

.. code-block:: console

   # create and add the following to /etc/nginx/sites-available/upload.conf 
   'server {
       listen 9001;
       
       location /SecretUploadDirectory/ {
           root    /var/www/uploads;
           dav_methods PUT;
       }
   }
   ' 

Step 4: Symlink out site to the sites-enabled directory

.. code-block:: console

   Temen@htb[/htb]$ sudo ln -s /etc/nginx/sites-available/upload.conf /etc/nginx/sites-enabled/

Step 5: Enable Nginx

.. code-block:: console

   Temen@htb[/htb]$ sudo systemctl restart nginx.service

Step 6: Test putting a local file on the server

.. code-block:: console

    curl -T /etc/passwd http://localhost:9001/SecretUploadDirectory/users.txt
