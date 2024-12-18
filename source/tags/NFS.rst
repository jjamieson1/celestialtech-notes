NFS
####

Date: 2024-11-09 16:24

Status:

Configuration
***************

The shares are defined in the /etc/exports file

**Note**: NFSv4 can use authenitcation methods, which NFSv4< use GID/UID
mappings

Example: To create a file share on an NFS server

.. code-block:: console

   echo '/mnt/nfs  10.129.14.0/24(sync,no_subtree_check)' >> /etc/exports
   systemctl restart nfs-kernel-server 
   exportfs

   /mnt/nfs        10.129.14.0/24

Enumerating NFS
****************

Example 1: using Nmap

.. code-block:: console

   sudo nmap 10.129.14.128 -p111,2049 -sV -sC

Example 2: Using an NFS Script

.. code-block:: console

   sudo nmap --script nfs* 10.129.14.128 -sV -p111,2049

Example 3: Listing shares on a NFS server

.. code-block:: console

   showmount -e 10.129.14.128

Example 4: Once the shares are known, mount the share on a local mount
point

.. code-block:: console

   mkdir target-NFS
   sudo mount -t nfs 10.129.14.128:/ ./target-NFS/ -o nolock
   cd target-NFS

Once done, unmount the share with:

.. code-block:: console

   cd /
   sudo umount /target-NFS

References
**********
https://academy.hackthebox.com/module/112/section/1068
