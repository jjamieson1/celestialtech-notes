getnthash.py
############

Date: 2024-12-19 14:48:38

Status: 

Description
***********

This script will use an existing TGT to request a PAC for the current user using U2U.
When the TGT was obtained using PKINIT, the resulting PAC will contain the NT hash which can be
used for silver tickets and for backwards compatibility with other tooling.

References
**********
https://github.com/dirkjanm/PKINITtools/blob/master/getnthash.py