############
DKIM
############
 (DomainKeys Identified Mail)

Date: 2024-11-29 18:42

Status:

Tags:

*****************
Description
*****************
An email authentication method designed to detect forged header fields and content

Enables receivers to check if email headers and content have been altered in transit

Emails can be tampered with during transit between servers making it difficult to detect alterations without extra security measures

Example: Email altered from $1000 request to $100,000 request

1. Sender's server "seals" email message by affixing a signature (DKIM)
2. Signature serves as an envelope seal, indicating the sender and authenticity of the message

If someone tries to tamper with the email, they must break the seal, making it detectable by the receiver

1. DKIM detects forged header fields and content in emails
2. Enables receivers to verify email authenticity and integrity
3. Helps prevent email tampering and forgery

*****************
References
*****************
