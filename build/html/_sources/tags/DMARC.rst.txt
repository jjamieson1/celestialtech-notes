############
DMARC
############


Date: 2024-11-29 18:42

Status:

Tags:

*****************
Description
*****************
Based on SPF and DKIM

1. Publish DMARC record in DNS

2. Email service provider checks email message against DMARC record

3. Depending on outcome, email is delivered, quarantined, or rejected

4. Email delivery reports sent to specified addresses periodically


Reporting Capabilities
=========================

* Provides visibility into email deliverability and protects against email spoofing/phishing

Takeaway
===========

* DMARC allows you to set a policy for handling unauthenticated emails:

+ No action

+ Send to spam

+ Reject


*****************
References
*****************