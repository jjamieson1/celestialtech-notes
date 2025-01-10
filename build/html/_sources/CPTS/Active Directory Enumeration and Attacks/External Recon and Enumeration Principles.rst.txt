External Recon and Enumeration Principles
#########################################

Date: 2024-12-30 10:20:20

Status: #new

Tags: :ref:`active directory enumeration attacks`

----


What are we looking for
***********************

**IP Space:**  What space are services hosted?  Cloud, premise etc..

**Domain information:**  Who admins the domain, what are the subdomains? What are the external services available?

**Schema Format:**  Email, username, account and password formats.  (build lists for brute forcing, password spraying)

**Data Disclosure:**  Publicly accessible files (pdf, doc xls etc).  Github and metadata.

**Breach Data:** Publicly released user names, password and other critical information. 

Where are we looking?
*********************

**ASN/IP Registrars:** IANA, arin when searching the Americas, RIPE for Europe. Also BGP Toolkit

**Domain Registrars:** DIG dnsenum, manual DNS records

**Social Media:** Linkedin, Facebook

**Public-Facing websites:** Company websites (about us, contact info)

**Cloud and Dev storage spaces:** Github, AWS S3, Azure blog Google search using dorks

**Breach Data Sources:** HaveIBeenPwned, Dehashed (https://www.dehashed.com/) 

Dorks
=======

Looking for files in Google ( fileType:pdf inurl:inlanefreight.com )

Looking for emails in Google ( intext:"@inlanfrieght.com" inurl:inlanefreight.com )


Username harvesting
*******************
using Linkedin2username (https://github.com/initstring/linkedin2username ) to scrape data from a companies presence.  This creates lists we can use.

Credential Hunting
******************

Dehashed (http://dehashed.com/) hunting for clear text credentials and password hashes from breaches.

.. code-block:: console 

    sudo python3 dehashed.py -q inlanefreight.local -p

    id : 5996447501
    email : roger.grimes@inlanefreight.local
    username : rgrimes
    password : Ilovefishing!
    hashed_password : 
    name : Roger Grimes
    vin : 
    address : 
    phone : 
    database_name : ModBSolutions


