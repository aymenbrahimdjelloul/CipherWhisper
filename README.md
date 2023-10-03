<h1 align="center">CipherWhisper</h1>
CipherWhisper is a Simple implementation of Caeser Cipher encryption algorithm with extra security improvements, and It is for learning purposes only 

<h1 align="center">Features</h1>

 - [x] Easy to use, CiphereWhisper provide the most easiest method to encrypt a Text
 - [x] Secure ! .. CipherWhisper provide a secure ciphers and impossible to crack cause of its 16 rounds that's provide unpredictable ciphers
 - [x] Good start to Learn cryptography ! .. It's just a strong & secure variant of the original Caesar cipher, so it's a good start to learn cryptography fundamentales

<h1 align="center">How It's work ?</h1>
<p align="ceneter">CipherWishper is a development and improvement for the basic Caesar Cipher, CipherWhipser designed to provide a secure and unpredictable ciphers.
CipherWhisper is a symmetric encryption algorithm it uses 128bit key lengthr</p>
<h3>Step 1 : Initialization</h3>

<p align="center">First of all CipherWhisper gets the encryption key or the password and padd it to the recommended key length which is 128-bit and generating a random IV also known as (Initialization Value), after that it create a key derivation list that contain sublists with random length token from the hexdigest of SHA-256 hash function of the padded encryption key and the generated IV, each sublist contain 16 shift key (Round number) to perform it in each round will applied to every character of the plaintext will encrypted</p>
<h3 algin="center">Step 2 : Encryption</h3>

<p>CipherWhisper will iterate through each character in the given plaintext and apply the shift keys in 16 round, after ciphering the plaintext is done the encrypt method will get a checksum of the original plaintext and return the final ciphered text with the IV and the checksum</p>
<h3>Decryption : </h3>
<p align="center">The decryption process is a reversing of the encryption, First of all the decrypt function will extract the IV and use it to generate key derivation list using the ciphertext IV and the given used key, after that it will perform a shift key using the generated key derivation list in reverse, after that it will check the authentication by comapring the extracted checksum from the ciphertext and the calculated checksum from the decrypted plaintext</p>

<h1 align="center">How to use ?</h1>

~~~
# Import CipherWhisper
from cipherwhisper import CipherWhisper

# Create CipherWhisper object
obj = CipherWhisper(password="0123456789")

# Encrypt a text
print(obj.encrypt("hello world!"))

# OUTPUT : 901b9454e2984618S@Oys:Y1sV h7509e5bda0c762d2

~~~

<h1 align="center">LICENSE</h1>

~~~
MIT License

Copyright (c) 2023 Aymen Brahim Djelloul

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

~~~
