subbrute
##########

Date: 2024-11-30 13:17

Status:

Installation
**************

.. code-block:: console

   git clone https://github.com/TheRook/subbrute.git >> /dev/null 2>&1

Usage
******

Example 1: Adding a domain and brute forcing the subs

.. code-block:: console

   cd subbrute
   echo "ns1.inlanefreight.com" > ./resolvers.txt
   ./subbrute inlanefreight.com -s ./names.txt -r ./resolvers.txt

References
************
https://academy.hackthebox.com/module/116/section/1512
