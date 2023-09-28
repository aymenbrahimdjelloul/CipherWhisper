"""
@author : Aymen Brahim Djelloul
version : 1.0
date : 01.09.2023
LICENSE : MIT

"""

# IMPORTS
from sys import exit


class InvalidEncryptionKey(BaseException):

    def __str__(self):
        return "Your encryption key can't be used. \n       " \
               "Please use a key of 128 bit length and supported characters"


class AuthenticationNotGranted(BaseException):

    def __str__(self):
        return "Your key may be wrong or the encryption cipher is corrupted!"


if __name__ == "__main__":
    exit()
