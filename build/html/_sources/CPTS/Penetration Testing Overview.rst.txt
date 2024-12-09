Penetration Testing Overview
################################

Status: draft

Date: 2024-11-09 14:48

Tags: 

Information Security (Infosec) Overview
***************************************

This domain covers many areas such as:

* Network and Infrastructure security
* Application Security
* Security Testing
* Systems auditing
* Business continuity planning
* Digital Forensics
* Incident detection and response


Risk Management Process
***********************

1. Identifing the risk
2. Analyze the risk
3. Evaluate the risk
4. Dealing with the risk
5. Monitor the risk
  
  
  .. mermaid:: mmd/risk-management-process.mmd


Red Team 
************
Test the defences and identifies risk in the organization

Blue Team
*************
Create defenses, and mitigation strategy of risk

Project Folder Structure
************************
On an engagement, a repeatable folder structure is recommended.

.. code-block::

    jjamieso@fatmex:~$ tree projects/
    projects/
    └── CompanyName
        ├── EPT
        │   ├── evidence
        │   │   ├── credentials
        │   │   ├── data
        │   │   └── screenshots
        │   ├── logs
        │   ├── scans
        │   ├── scope
        │   └── tools
        └── IPT
            ├── evidence
            │   ├── credentials
            │   ├── data
            │   └── screenshots
            ├── logs
            ├── scans
            ├── scope
            └── tools


References
************
https://academy.hackthebox.com/module/77/section/721