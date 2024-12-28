snaffler
########

Date: 2024-12-19 14:27:41

Status:

Tags:

Description
***********

Snaffler is a tool for pentesters and red teamers to help find delicious candy needles (creds mostly, but it's flexible) in a bunch of horrible boring haystacks (a massive Windows/AD environment).

It might also be useful for other people doing other stuff, but it is explicitly NOT meant to be an "audit" tool.

.. note:: Snaffler requires that it be run from a domain-joined host or in a domain-user context.

Usage 
******

Example: 

.. code-block:: powershell

    Snaffler.exe -s -d inlanefreight.local -o snaffler.log -v data


References
**********
https://github.com/SnaffCon/Snaffler