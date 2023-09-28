"""
This code or file is part of 'CipherWhisper' project
copyright (c) 2023, Aymen Brahim Djelloul, All rights reserved.
use of this source code is governed by MIT License that can be found on the project folder.

@author : Aymen Brahim Djelloul
version : 1.0
date : 01.09.2023
LICENSE : MIT

    // Cipher Whisper is a simple algorithm to encrypt text for educational purposes

    // Cipher Whisper Algorithm steps:

    STEP 1: initializing

        1- Generate random iv value
        2- Assign the final key encryption after adding the iv value and padding
        3- Generate key derivation using the encryption key (32bit)
        4- Generate a Shift rows key according to the encryption key

    STEP 2: Apply the encryption
        5- Encrypt the given text using the key derivation keys in 16 round
        6- Shift rows in the cipher by 4 characters using a unique shift key calculated in the init step

    STEP 3: Final step
        7- calculate a checksum for the encrypted text
        8- return the encryption result with iv value and checksum


    // Example of CipherWhisper encryption:

        ENCRYPTED TEXT = fs9df6sd9as2de5po5up12u5qa24h9qg70ds204kw4fl2k5k2135ld3t5ie4j4l1
        EXPLANATION    = [   IV Value   ][            Encrypted Text          ][checksum hash]


"""

# IMPORTS
import sys
import random
from hashlib import sha256
from secrets import token_hex
from exceptions import *


class CipherWhisper:

    # DEFINE VARIABLES
    AUTHOR = "Aymen Brahim Djelloul"
    VERSION = 1.0
    __KEY_LENGTH = 128
    __ROUNDS = 16
    __CHARS = ''.join([chr(i) for i in range(32, 127)])
    __CHARS_LENGTH = len(__CHARS)

    def __init__(self, password: str):

        # Define variable
        self.__key = None
        # Check is a valid key
        if not self.__is_valid_key(password): raise InvalidEncryptionKey()

        # Generate iv value
        self.__iv_value: str = self.__generate_iv_value()

        # Pad the key
        self.__key: str = f"{self.__iv_value}{self.__key_padding(password)}"

        # Generate key derivation keys
        self.__derivation_keys: list = self.__generate_key_derivation()

    def encrypt(self, plaintext: str) -> str:
        """
        This method will encrypt the given Plaintext

        :param plaintext: Plaintext will encrypt
        :return: The encrypted Plaintext
        """

        # First Define empty variable for encrypted text
        cipher: str = ""
        key_derivation_len: int = len(self.__derivation_keys)

        # Start ENCRYPTION
        # // STEP 1
        inner_list_index = 0
        # print(self.__CHARS)
        # print(key_derivation_len)
        for char in plaintext:

            char_index: int = self.__CHARS.index(char)

            for key in self.__derivation_keys[inner_list_index]:
                char_index: int = (char_index + key) % self.__CHARS_LENGTH
                # DEBUG
                # print(f"transferred to {self.__CHARS[char_index]} using {key} index")

            cipher = cipher + self.__CHARS[char_index]

            # Increase the inner list index
            inner_list_index += 1
            # print(inner_list_index)

            if inner_list_index == key_derivation_len:
                inner_list_index = 0

        # Calculate the CRC32 checksum for the plaintext
        integrity_checksum = self.__generate_integrity_checksum(plaintext)

        # Clear memory
        del plaintext, char, key, char_index,

        # Return the encrypted plaintext
        return f"{self.__iv_value}{cipher}{integrity_checksum}"

    def decrypt(self, cipher: str) -> str:
        """
        This method will decrypt the given cipher

        :param cipher:
        :return: The Original Plaintext from cipher
        """

        # First Define empty variable for encrypted text
        plaintext: str = ""

        # print(cipher)
        # Get the iv value
        iv_value = self.__get_iv_value(cipher)
        # print(iv_value)
        # Get the checksum hash
        checksum_hash: str = cipher[len(cipher) - 16:len(cipher)]

        # update the iv value
        self.__key = f"{iv_value}{self.__key[16:len(self.__key)]}"

        # Get the new key derivation
        key_derivation: list = self.__generate_key_derivation()
        # print(key_derivation)
        key_derivation_len: int = len(key_derivation)

        # Adjust the cipher string
        cipher: str = cipher[16:len(cipher) - 16]
        # print(checksum_hash)
        # Start DECRYPTION
        # // STEP 1
        inner_list_index: int = 0
        # print(self.__CHARS)
        for char in cipher:

            char_index: int = self.__CHARS.index(char)

            for key in key_derivation[inner_list_index]:
                char_index: int = char_index - key
                # DEBUG
                # print(f"transferred to {self.__CHARS[char_index]} using {key} index")

            plaintext: str = plaintext + self.__CHARS[char_index % self.__CHARS_LENGTH]

            # Increase the inner list index
            inner_list_index += 1

            if inner_list_index == key_derivation_len:
                inner_list_index = 0

        # print(plaintext)
        # Check the authentication
        if not self.__check_authentication(plaintext, checksum_hash):
            raise AuthenticationNotGranted

        # Return the Original plaintext
        return plaintext

    @staticmethod
    def __is_valid_key(key: str) -> bool:
        """ This method will check if the given key encryption valid"""
        return True if key.isascii() and 32 < len(key) * 8 <= 128 else False

    @staticmethod
    def __generate_iv_value(iv_length: int = 8) -> str:
        """ This method will generate a random iv value"""
        return token_hex(iv_length)

    def __key_padding(self, key: str) -> str:
        """ This method will pad the given key"""

        padding_length = (self.__KEY_LENGTH // 8) - len(key)
        padded_key = key + 'XY' * padding_length
        return padded_key

    def __generate_key_derivation(self) -> list:
        """ This method will generate a key derivation tuple according to the encryption key used"""

        # Get the unique id of the key
        key_id: int = int(sha256(self.__key.encode("UTF-8")).hexdigest(), 16)
        # Get the length of the sublist in key derivation list
        key_derivation_len: int = int(key_id * 16 % 2000)

        # seed the key id to random module
        random.seed(key_id)

        # Generate the key derivation sublist using random module
        key_derivation: list = [[random.randint(0, 99) for _ in range(self.__ROUNDS)]
                                for sublist in range(key_derivation_len)]
        # Clear memory
        del key_id, key_derivation_len

        return key_derivation

    @staticmethod
    def __generate_shuffle_key(key: str) -> int:
        """ This method will generate the shift rows key"""
        return int(sha1(key).hexdigest(), 16)

    @staticmethod
    def __generate_integrity_checksum(plaintext: str) -> str:
        """ This method will calculate a checksum with sha256 algorithm for the given data"""
        return sha256(plaintext.encode("UTF-8")).hexdigest()[:16]

    @staticmethod
    def __get_iv_value(cipher: str) -> str:
        """ This method will extract the iv value from the cipher text"""
        return cipher[:16]

    @staticmethod
    def __get_checksum(cipher: str) -> str:
        """ This method will extract the checksum from the cipher text"""
        return cipher[len(cipher):len(cipher) - 16]

    @staticmethod
    def __check_authentication(decrypted_text: str, encryption_checksum: str) -> bool:
        """ This method will check the authentication of the decryption key"""
        return True if sha256(decrypted_text.encode("UTF-8")).hexdigest()[:16] == encryption_checksum else False

    def version(self, version_float: bool = False) -> str | float:
        """ This method will return the current software version"""
        return str(self.VERSION) if version_float else self.VERSION

    def copyright(self) -> str:
        """ This method will return the copyright string"""
        return f"{self.AUTHOR}"


if __name__ == "__main__":
    sys.exit()
