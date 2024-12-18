Symmetrical Encryption
########################

Uses the same key to encrypt and decrypt

Example: XOR, AES, DES, 3DES, Blowfish Vulnerable to: Frequency
Analysis, Padding oracle attack

from pwn import xor xor(“p@ssword” , “secret”)

The p@ssword text is encrypted with the key “secret”
