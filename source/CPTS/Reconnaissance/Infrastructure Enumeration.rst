Infrastructure Based Enumeration
*********************************

Status: draft

Date: 2024-11-09 14:48

Tags: 


Domain information
******************


The start of the enumeration is to see if there is a public website. 

1. Document what services/software they sell/promote.
2. Document the company structure


Looking at the SSL certificate can tell often help us with Sub-domains.
There is a good tool at crt.sh <https://crt.sh/ that allows
inspection of a certificate.

This information can be retrieved via the command line and formatted to
JSON with:

.. code-block::  console

   Temen@htb[/htb]$ curl -s https://crt.sh/\?q\=inlanefreight.com\&output\=json | jq .

If needed you can filter the sub-domain with:

.. code-block:: console


   Temen@htb[/htb]$ curl -s https://crt.sh/\?q\=inlanefreight.com\&output\=json | jq . | grep name | cut -d":" -f2 | grep -v "CN=" | cut -d'"' -f2 | awk '{gsub(/\\n/,"\n");}1;' | sort -u > subdomainlist

**Company Hosted Servers** To see which hosts have an IP address from
that list use this:

.. code-block:: console

   for i in $(cat subdomainlist);
      do host $i | grep "has address" | grep inlanefreight.com | cut -d" " -f1,4;
    done

Install Shodan command line tools with:

.. code-block:: shell

   sudo apt-get install python3-shodan
   shodan init <api key>

Shodan IP List

.. code-block:: console

   for i in $(cat subdomainlist);
      do host $i | grep "has address" | grep inlanefreight.com | cut -d" " -f4 >> ip-addresses.txt;
   done
   for i in $(cat ip-addresses.txt);
      do shodan host $i;
   done

Using ``dig`` to get DNS records

.. code-block:: console

   dig any inlanefreight.com


Cloud Resource Enumeration
*****************************

Listing of cloud resources can be found from 1. Using Google and
leveraging the inurl: and intext ``dorks`` to find blob storage hosted
in the cloud 2. Using the webpage source code to look for any references
pointing to cloud storage.


Online Tools to gather information about a domain
*************************************************


1. **Domain.Glass** A url that can provide a ton of information on a
   domain name.

2. GrayHatWarfare https://buckets.grayhatwarfare.com/ A URL that
   can find storage buckets for a domain.


Staff
**************

1. Searching LinkedIn and searching for Staff blogs to get an insight on
   the technology used.
2. Looking at job postings to see what skills are being requested
3. Searching Github for any public repositories
4. Looking at the staffs skill set to see how experienced they are.
