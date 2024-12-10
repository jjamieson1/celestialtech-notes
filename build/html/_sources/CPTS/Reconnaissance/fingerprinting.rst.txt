#################
fingerprinting
#################


2024-11-17 08:02

Status:

Tags: `Certified Penetration Tester <Certified Penetration Tester>`__
`Information Gathering <Information Gathering>`__

*****************
Description
*****************

The identification of systems and technology through various means.

-  Targeted attacks: By knowing the technologies you can fine tune your
   attack.

-  Identifying Misconfigurations: Fingerprinting can identify outdated,
   vulnerable software.

-  Prioritizing targets: targeting systems that may be vulnerable.

-  Building comprehensive profile: finger prints add to the over all
   picture of the targets infrastructure.

*****************
Techniques
*****************

-  Banner grabbing

-  Analyzing HTTP headers (x-powered-by header)

-  probing for unique responses

-  Analyzing page content.

*********************
Host Identification
*********************
By using ping you can identify a OS by how it responds to ping.

Example 1: Pinging a windows host

.. code-block:: console

   ping 192.168.86.12
   PING 192.168.86.12 (192.168.86.12) 56(84) bytes of data.
   64 bytes from 192.168.86.12: icmp_seq=1 ttl=128 time=0.216 ms
   64 bytes from 192.168.86.12: icmp_seq=2 ttl=128 time=0.252 ms
   64 bytes from 192.168.86.12: icmp_seq=3 ttl=128 time=0.142 ms

Example 2: Pinging a MacOSX host

.. code-block:: console

   ping 192.168.86.161
   PING 192.168.86.161 (192.168.86.161) 56(84) bytes of data.
   64 bytes from 192.168.86.161: icmp_seq=1 ttl=32 time=92.8 ms
   64 bytes from 192.168.86.161: icmp_seq=2 ttl=32 time=724 ms
   64 bytes from 192.168.86.161: icmp_seq=3 ttl=32 time=753 ms
   64 bytes from 192.168.86.161: icmp_seq=4 ttl=32 time=565 ms

The TTL can help us identify an OS. Here is a `table of
codes <https://subinsb.com/default-device-ttl-values/>`__

*******************
Tools
*******************

`wappalyzer <wappalyzer>`__

`BuiltWith <BuiltWith>`__

`whatweb <whatweb>`__

`nmap <nmap>`__

`netcraft <netcraft>`__

`wafw00f <wafw00f>`__

`nikto <nikto>`__

*******************
References
*******************
https://academy.hackthebox.com/module/144/section/3075
