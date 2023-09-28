# This script implement the performance test to initialize and encrypt and decrypt using CipherWhisper
# Author : Aymen Brahim Djelloul

import sys
import os
from time import perf_counter

# Add the 'src' directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Import the CipherWhisper algorithm
from cipherwhisper import CipherWhisper

# Define encryption key
KEY = "0123456789"
# Define string of 1 KB
TEXT = "X" * 1024

# Create CipherWhisper object
s_time = perf_counter()     # Store the start time for the initializing step
obj = CipherWhisper(password=KEY)
print(f"CipherWhisper initialized in : {perf_counter() - s_time:.5f} s")

# Encrypt 1 KB string
e = obj.encrypt(TEXT)
print(f"CipherWhisper Encrypt 1 KB of text in : {perf_counter() - s_time:.5f} s")
# Decrypt 1 KB string
d = obj.decrypt(e)
print(f"CipherWhisper Decrypt 1 KB of text in : {perf_counter() - s_time:.5f} s")
