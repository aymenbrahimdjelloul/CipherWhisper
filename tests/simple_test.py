# This script implement the regular process to encrypt and decrypt
# Author : Aymen Brahim Djelloul

import sys
import os

# Add the 'src' directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Import the CipherWhisper algorithm
from cipherwhisper import CipherWhisper

# Define the encryption key and the text will process
KEY = "0123456789"
TEXT = "hello world!"

# Create the CipherWhisper object
obj = CipherWhisper(password=KEY)

# Encrypt the text
e = obj.encrypt(TEXT)

# Decrypt the text
d = obj.decrypt(e)

# Print out the result
print(f"Original Text : {TEXT}")
print(f"Encrypted Text : {e}")
print(f"Decrypted Text : {d}")
