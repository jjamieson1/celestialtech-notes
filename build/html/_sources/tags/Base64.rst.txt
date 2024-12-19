Base64
#######


File integrity
****************

To verify a file has not changed after encoding it on system1 and
decoding it on system2 is to use :ref:`md5sum <md5sum>`

| Example:
| To get the sum from you public key

.. code-block:: console

   fatmex@locahost% md5sum id_rsa

   4e301756a07ded0a2dd6953abf015278  id_rsa

Then encode the key to base64

.. code-block:: console

   fatmex@locahost% cat id_rsa |base64 -w 0;echo

   LS0tLS1CRUdJT..>>snip>>...BLRVktLS0tLQo

Then the base64 encoded string can be copied to a Windows host

.. code-block:: console


   [IO.File]::WriteAllBytes("C:\Users\Public\id_rsa", [Convert]::FromBase64String("LS0tLS1CRUdJT..>>snip>>...BLRVktLS0tLQo")

Then you can verify it with the file integrity with

.. code-block:: console

   PS C:\htb> Get-FileHash C:\Users\Public\id_rsa -Algorithm md5

   Algorithm       Hash                                                                   Path
   ---------       ----                                                                   ----
   MD5             4E301756A07DED0A2DD6953ABF015278                                       C:\Users\Public\id_rsa

As you can see the md5 sum is the same, and the file has not mutated.
 [1]_

Encoding on Windows
********************

Using :ref:`powershell <powershell>` you can encode a file with:

.. code-block:: console

   PS C:\htb> [ConverPS C:\htb> [Convert]::ToBase64String((Get-Content -path "C:\Windows\system32\drivers\etc\hosts" -Encoding byte))t]::ToBase64String((Get-Content -path "C:\Windows\system32\drivers\etc\hosts" -Encoding byte))

and get the MD5 sum with:

.. code-block:: console

   PS C:\htb> Get-FileHash "C:\WindoPS C:\htb> Get-FileHash "C:\Windows\system32\drivers\etc\hosts" -Algorithm MD5 | select Hashws\system32\drivers\etc\hosts" -Algorithm MD5 | select Hash

Decoding with Linux
********************
This can be decoded on Linux with :

.. code-block:: console

   Temen@htb[/htb]$ echo IyBDb3B5cmlnaHQgKGMpIDE5OTMtMjAwOSBNaWNyb3NvZnQgQ29ycC4NCiMNCiMgVGhpcyBpcyBhIHNhbXBsZSBIT1NUUyBmaWxlIHVzZWQgYnkgTWljcm9zb2Z0IFRDUC9JUCBmb3IgV2luZG93cy4NCiMNCiMgVGhpcyBmaWxlIGNvbnRhaW5zIHRoZSBtYXBwaW5ncyBvZiBJUCBhZGRyZXNzZXMgdG8gaG9zdCBuYW1lcy4gRWFjaA0KIyBlbnRyeSBzaG91bGQgYmUga2VwdCBvbiBhbiBpbmRpdmlkdWFsIGxpbmUuIFRoZSBJUCBhZGRyZXNzIHNob3VsZA0KIyBiZSBwbGFjZWQgaW4gdGhlIGZpcnN0IGNvbHVtbiBmb2xsb3dlZCBieSB0aGUgY29ycmVzcG9uZGluZyBob3N0IG5hbWUuDQojIFRoZSBJUCBhZGRyZXNzIGFuZCB0aGUgaG9zdCBuYW1lIHNob3VsZCBiZSBzZXBhcmF0ZWQgYnkgYXQgbGVhc3Qgb25lDQojIHNwYWNlLg0KIw0KIyBBZGRpdGlvbmFsbHksIGNvbW1lbnRzIChzdWNoIGFzIHRoZXNlKSBtYXkgYmUgaW5zZXJ0ZWQgb24gaW5kaXZpZHVhbA0KIyBsaW5lcyBvciBmb2xsb3dpbmcgdGhlIG1hY2hpbmUgbmFtZSBkZW5vdGVkIGJ5IGEgJyMnIHN5bWJvbC4NCiMNCiMgRm9yIGV4YW1wbGU6DQojDQojICAgICAgMTAyLjU0Ljk0Ljk3ICAgICByaGluby5hY21lLmNvbSAgICAgICAgICAjIHNvdXJjZSBzZXJ2ZXINCiMgICAgICAgMzguMjUuNjMuMTAgICAgIHguYWNtZS5jb20gICAgICAgICAgICAgICMgeCBjbGllbnQgaG9zdA0KDQojIGxvY2FsaG9zdCBuYW1lIHJlc29sdXRpb24gaXMgaGFuZGxlZCB3aXRoaW4gRE5TIGl0c2VsZi4NCiMJMTI3LjAuMC4xICAgICAgIGxvY2FsaG9zdA0KIwk6OjEgICAgICAgICAgICAgbG9jYWxob3N0DQo= | base64 -d > hosts

and verify the integrity with :

.. code-block:: console

   md5sum hosts 

.. [1]
   The windows shell has a limit of 8192K
