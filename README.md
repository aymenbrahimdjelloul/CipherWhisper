# CipherWhisper
CipherWhisper is a Simple implementation of Caeser Cipher encryption algorithm with extra security improvements, and It is for learning purposes only 

<h1 align="ceneter">How It's work ?</h1>
<p align="ceneter">CipherWishper is a development and improvement for the basic Caesar Cipher, CipherWhipser designed to provide a secure and unpredictable ciphers.
CipherWhisper is a symmetric encryption algorithm it uses 128bit key lengthr</p>
<h3>Step 1 : Initialization</h3>
<p align="center">First of all CipherWhisper gets the encryption key or the password and padd it to the recommended key length which is 128-bit and generating a random IV also known as (Initialization Value), after that it create a key derivation list that contain sublists with random length token from the hexdigest of SHA-256 hash function of the padded encryption key and the generated IV, each sublist contain 16 shift key (Round number) to perform it in each round will applied to every character of the plaintext will encrypted</p>
<h3 algin="center">Step 2 : Encryption</h3>
