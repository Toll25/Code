from Crypto.Cipher import AES

def decrypt_aes(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

# Example usage:
ciphertext = b'\x92\x83\xa3@\xfa\x85\x9c\x1e\x11\x85\xa6)\xc7(\xa5'
key = b'ThisIsASecretKey'
plaintext = decrypt_aes(ciphertext, key)
print("Decrypted plaintext:", plaintext.decode())
