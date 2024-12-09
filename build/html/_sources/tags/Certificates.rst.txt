###############
Certificates
###############

DAte: 2024-11-17 07:21

Status:

Tags: 

***************************************
Certificate Transparency logs (CT)
***************************************

Append only logs that record the issuance of SSL certificates. Security
researchers monitor these to identify suspicious activity.

If a certificate issuer fails to follow rules, they are revoked.

CT logs use a Merkle tree cryptographic structure.

***************************************
Searching CT logs
***************************************

Example 1: using curl at the crt.sh web site

.. code-block:: 

   curl -s "https://crt.sh/?q=facebook.com&output=json" | jq -r '.[]
    | select(.name_value | contains("dev")) | .name_value' | sort -u


*************
References
*************
https://academy.hackthebox.com/module/144/section/1258
