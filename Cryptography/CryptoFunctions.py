"""
CryptoFunctions.py

Version 2.2

This file contains the implementation of functions designed to provide
cryptograpy utility using OpenSSL commands. Both AES and RSA support
string cryptography. In addition, AES also include regular file crypto.

Actually it includes the following algorithms:

- RSA encryption
- RSA signature
- AES encryption
- AES encryption (system files)

Changelog:

- v2.2: Changed randomString function for a python implementation.


openssl genrsa -out key.pem 4096
openssl rsa -in key.pem -pubout -out pub-key.pem

"""

import subprocess
import base64
import random
import string

DEFAULT_PUB_KEY = "pub-key.pem"
DEFAULT_KEY = "key.pem"


def RSAencrypt(plaintext, keyfile=DEFAULT_PUB_KEY):
	"""
	Encrypt a string with RSA.
	"""
	p = subprocess.Popen(["openssl","rsautl","-encrypt","-pubin","-inkey",keyfile],stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	out, err = p.communicate(plaintext)
	return base64.b64encode(out)


def RSAdecrypt(ciphertext, keyfile=DEFAULT_KEY):
	"""
	Decrypt a string with RSA.
	"""
	ciphertext = base64.b64decode(ciphertext)
	p = subprocess.Popen(["openssl","rsautl","-decrypt","-inkey",keyfile], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	out, err = p.communicate(ciphertext)
	return out


def RSAsign(string, keyfile=DEFAULT_KEY):
	"""
	Sign a string with RSA.
	"""
	p = subprocess.Popen(["openssl","rsautl","-sign","-inkey",keyfile],stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	out, err = p.communicate(string)
	return base64.b64encode(out)


def RSAverify(signedString, keyfile=DEFAULT_PUB_KEY):
	"""
	Verify a signed string with RSA.
	"""

	signedString = base64.b64decode(signedString)
	p = subprocess.Popen(["openssl","rsautl","-verify","-pubin","-inkey",keyfile], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	out, err = p.communicate(signedString)
	return out


def AESencrypt(plaintext, key):
	"""
	Encrypt a string with AES-256-CBC.
	"""
	p = subprocess.Popen(["openssl","aes-256-cbc","-base64","-k",key], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	out, err = p.communicate(plaintext)
	return out


def AESdecrypt(ciphertext, key):
	"""
	Decrypt a string with AES-256-CBC.
	"""
	p = subprocess.Popen(["openssl","aes-256-cbc","-base64","-d","-k",key], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	out, err = p.communicate(ciphertext)
	return out


def AESfileEncrypt(inputFile, outputFile, key):
	"""
	Encrypt a file with AES-256-CBC.
	"""
	p = subprocess.call(["openssl","aes-256-cbc","-base64","-k",key,"-in",inputFile,"-out",outputFile])
	return p


def AESfileDecrypt(inputFile, outputFile, key):
	"""
	Decrypt a file with AES-256-CBC.
	"""
	p = subprocess.call(["openssl","aes-256-cbc","-base64","-d","-k",key,"-in",inputFile,"-out",outputFile])
	return p

def randomString(size):
	"""
	Generate a random string.
	"""
	out = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(size))
	#p = subprocess.Popen(["openssl","rand","-base64",str(size)], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	#out, err = p.communicate()
	return out #[:size]

