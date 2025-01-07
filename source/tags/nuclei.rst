nuclei
########

Date: 2025-01-06 18:10:55

Tags: 

Description
************

Nuclei is a modern, high-performance vulnerability scanner that leverages simple YAML-based templates. It empowers you to design custom vulnerability detection scenarios that mimic real-world conditions, leading to zero false positives.


Installation
***************

.. code-block:: bash

    go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest


Usage
******

.. code-block:: bash

    nuclei -target 192.168.1.0/24

Check out the documentation for more examples at: https://docs.projectdiscovery.io/templates/introduction

References
************

https://github.com/projectdiscovery/nuclei