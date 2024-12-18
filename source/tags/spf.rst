spf
####

**SPF (Sender Policy Framework) Summary**

Background
*************

-  Business domain: business.com
-  Email delivery server IP address: 192.168.0.1
-  Scam email server IP address: 1.2.3.4

SPF Record
*************

-  Published in DNS as ``v=spf1 ip4:192.168.0.1 -all``

   -  Only emails from IP address 192.168.0.1 can pass SPF check
   -  All other emails will fail SPF check

How SPF Works
******************

-  Email delivery service connects to recipient’s mailbox server
-  Server extracts domain name from envelope “from” address
   (business.com)
-  Server checks connecting host’s IP address against business.com’s SPF
   record
-  If listed, SPF check passes; otherwise, fails
-  Scam email server at 1.2.3.4 will never pass SPF check due to
   non-matching IP address

Key Takeaways
***************

-  SPF record is a whitelist of legitimate IP addresses
-  Only emails from whitelisted IP addresses can pass SPF check
-  SPF authentication result used for DMARC authentication later
