Proxy Setup
###############

Date: 2025-01-09 11:10:10

Status: #draft 

Tags: :ref:`certified penetration tester`, :ref:`using web proxies`

----

Pre-configured Browser
*************************
 
 Both web proxies have built in browsers that you can start using right away

Plugins for Modern browsers
****************************

- Foxy Proxy (https://addons.mozilla.org/en-US/firefox/addon/foxyproxy-standard/)
  
Getting CA Certificates
***************************

When inspecting HTTPS traffic you will need to install the proxies CA cert. 

Burp
======

Once foxy proxy is installed, go to http://burp and choose the `CA Certificate` button on the top right 

Zap 
=====

To get ZAP's certificate, we can go to (Tools>Options>Network>Server Certificate), then click on Save:

Installing the CA Certificates
********************************

- In firefox browse to : about:preferences#privacy 
- Scroll to the bottom and select `View Certificates`
- Click on `Authorities`
- Click on `import` and select your certificate 
- Click `Trust this CA to identify websites` and `Trust this CA to identify websites`


References
*************

https://academy.hackthebox.com/module/110/section/1047