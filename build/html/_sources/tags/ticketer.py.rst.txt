ticketer.py
###########


Date: 2024-12-19 14:55:55

Status: 

Tags:

Description
***********
This script will create TGT/TGS tickets from scratch or based on a template (legally requested from the KDC)
allowing you to customize some of the parameters set inside the PAC_LOGON_INFO structure, in particular the
groups, extrasids, etc.
Tickets duration is fixed to 10 years from now (although you can manually change it)

References
**********
https://github.com/fortra/impacket/blob/master/examples/ticketer.py