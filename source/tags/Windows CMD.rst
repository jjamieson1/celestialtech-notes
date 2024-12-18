Windows CMD
###########

Date: 2024-11-28 22:03

Status:


Windows CMD
===========

Common commands
---------------

+------------------------------------------+---------------------------+
| DIR                                      | List contents of the      |
|                                          | current directory         |
+==========================================+===========================+
| ``net use n: \\\10.10.10.10\Finance``    | Mount a network drive     |
+------------------------------------------+---------------------------+
| ``net use n:\\\10.10                     | mount a drive with        |
| .10.10\Finance /user:jamie password123`` | account                   |
+------------------------------------------+---------------------------+
| ``dir n:\*cred* /s /b``                  | list files with cred      |
+------------------------------------------+---------------------------+
| ``findstr /s /i cred n:\*.*``            | Find in files the string  |
|                                          | cred                      |
+------------------------------------------+---------------------------+

References
==========

https://academy.hackthebox.com/module/116/section/1140
