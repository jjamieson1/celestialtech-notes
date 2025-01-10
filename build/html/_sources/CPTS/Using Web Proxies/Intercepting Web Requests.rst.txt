Intercepting Web Requests
############################

Date: 2025-01-09 11:19:04

Status: #draft

Tags: :ref:`certified penetration tester`, :ref:`using web proxies`

----

Intercepting Requests
*************************

Once you enable the intercept requests in either Burp or Zap, the system will capture and display the 
request. 

Burp
======

- Forward continues the request/response

Zap
=====

- Step will continue the request onto the next response/request 
- Break will stop the request 
- Continue will allow the remainder of the request/responses to finish. 


Manipulating Intercepted Requests
**********************************

Requests can be editted for:

- SQL injections
- Command injections
- Upload bypass
- Authentication bypass
- XSS
- XXE
- Error handling
- Deserialization

References 
************

https://academy.hackthebox.com/module/110/section/1048