Incident Handling Process.rst
#############################

Date: 2024-10-19 09:13

Status: #cyber

Cyber Kill Chain
******************

Attack Life Cycle
===================

7 stages

-  Recon
-  Weaponize
-  Deliver
-  Exploit
-  Install
-  C&C
-  Action

Incident Handling Process
==============================

Defined by NIST, there are 4 stages.

-  **Preparation**. ( Training, hardening, documenting and policy)
-  **Detection and Analysis**
-  **Containment, Eradication and Recovery**
-  **Post Incident Activity**

Have a “Jump Bag” ready

Preparation Part 1
=====================

-  Clear Policies and documentation

-  Forensic tools ### Preparation part 2

-  :ref:`DMARC <DMARC>` built on top of :ref:`SPF <SPF>` and :ref:`DKIM <DKIM>`

-  will help protect against Phishing

-  End Point hardening (&EDR)

-  Network Protection

   -  802.1x filtering
   -  IDS
   -  Network segmentation and firewalls

-  Privilege Identity Management / MFA / Passwords

-  Vulnerability Scanning

-  User awareness training

-  Active Directory Security Assessment

-  Purple Team exercises

Detection and Analyses Part 1
==============================

-  Detection processes at all levels of the organization
-  Initial Investigation - document everything, refer to
   documentation/diagrams
-  Keep a log of events in order in this form:

   -  \|\ ``Date``\ \|\ ``Time of the event``\ \|\ ``hostname``\ \|\ ``event description``\ \|\ ``data source``

-  Identify severity and `extent <extent>`__ questions
-  Incident confidentiality and communication

Detection and Analyses Part 2
================================

-  Investigation

   -  Creation and usage of indicators of compromise (IOC)
   -  Identification of new leads and impacted systems
   -  Data collection and analysis from the new leads and impacted
      systems

-  Initial investigation data
-  Creation and usage of IOC’s (OpenIOC and Yara are a couple tools)
-  Identification Of New Leads & Impacted Systems
-  Data Collection & Analysis From The New Leads & Impacted Systems

Containment, Eradication, & Recovery Stage
============================================

-  Isolating systems
-  reversing malicious account creates

Post-Incident Activity Stage
=============================

-  Reporting

   -  What happened and when?
   -  Performance of the team dealing with the incident in regard to
      plans, playbooks, policies, and procedures
   -  Did the business provide the necessary information and respond
      promptly to aid in handling the incident in an efficient manner?
      What can be improved?
   -  What actions have been implemented to contain and eradicate the
      incident?
   -  What preventive measures should be put in place to prevent similar
      incidents in the future?
   -  What tools and resources are needed to detect and analyze similar
      incidents in the future?

References
***************
