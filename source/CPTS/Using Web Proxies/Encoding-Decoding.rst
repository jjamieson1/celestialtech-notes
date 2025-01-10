Encoding-Decoding
###################

Date: 2025-01-09 14:12:39

Status: #draft

Tags: :ref:`certified penetration tester`, :ref:`using web proxies`

----

Description
**************

Sometimes the input/output may require encoding or decoding. 

URL Encoding 
**************

- To encode URL text in burp repeater, select the text and choose `Convert Selection>URL>URL encode key characters` (or CTRL+U)
- Zap will encode requests for us in the backend 


.. note:: There are other types of URL-encoding, like Full URL-Encoding or Unicode URL encoding, which may also be helpful for requests with many special characters.
    
URL Decoding
**************

The following are some of the other types of encoders supported by both tools:

- HTML
- Unicode
- Base64
- ASCII hex

