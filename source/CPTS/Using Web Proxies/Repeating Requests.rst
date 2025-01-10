Repeating Requests
###################

Date: 2025-01-09 14:01:22

Status: #draft 

Tags: :ref:`certified penetration tester`, :ref:`using web proxies`

----


Description 
***************

Manually manipulating the request can be time consuming on repeat requests.  Thankfully this can be automated.

Proxy History
**************
Both Burp and Zap keep a history and history can be replayed. 

Repeating Requests
********************

Burp Repeating
================

Locate a request and invoke `CTRL+R` to send it to the repeater tab.  Inspect/modify the request and hit send. 

Zap Repeating
===============

Find your request and right click choosing `Open/Resend with Request Editor`.  Inspect/modify the request and hit send. 

References
***********

https://academy.hackthebox.com/module/110/section/1051