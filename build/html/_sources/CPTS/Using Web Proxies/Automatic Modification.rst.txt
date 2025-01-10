Automatic Modification
##########################

Date: 2025-01-09 13:51:55

Status: #draft

Tags: :ref:`certified penetration tester`, :ref:`using web proxies`

----

Description 
**************

There may be use cases where you want to automate certain filtering/modifying. 

Automatic Request Modification
********************************

Burp Match and Replace 
=========================

Replacing the user agent with a custom string on all requests. We can go to `(Proxy>Options>Match and Replace)` and click on Add 

.. image:: img/burp_match_replace_user_agent_1.jpg


Zap Replacer 
==============

In Zap ctrl+R or clicking the replacer in the options menu 

.. image:: img/zap_match_replace_user_agent_1.jpg

Automatic Response Modification
********************************

navigate to `Proxy>Options>Match and Replace` in Burp and this time select Response Boy in the type set. 

.. image:: img/burp_match_replace_response_1.jpg

References
***********

https://academy.hackthebox.com/module/110/section/1050