#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install pycryptodome')


# In[4]:


from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

def encrypt_data(data, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(data.encode(), AES.block_size))
    return cipher.iv + ciphertext

def decrypt_data(encrypted_data, key):
    iv = encrypted_data[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(encrypted_data[16:]), AES.block_size)
    return plaintext.decode()

# Example Usage:
key = b'Sixteen byte key'  # Must be 16, 24, or 32 bytes
text = "Hello, secure world!"

encrypted_text = encrypt_data(text, key)
print(f"Encrypted Data: {encrypted_text}")

decrypted_text = decrypt_data(encrypted_text, key)
print(f"Decrypted Data: {decrypted_text}")


# In[ ]:




