import hashlib
import os
import filePopulation

def UserExists(userID):
    lines = filePopulation.byteOut('users')
    i = 0
    while (i < len(lines)):
        if (i == 0):
            i += 1
        if (i % 2 == 1):
            userName = lines[i].decode().replace('\n', '')
            if (userName == userID):
                return True
            i += 1

        else:
            i += 1

    return False

def GetUserEncrypt(userID):
    lines = filePopulation.byteOut('users')
    i = 0
    while (i < len(lines)):
        if (i == 0):
            i += 1
        if (i % 2 == 1):
            userName = lines[i].decode().replace('\n', '')
            if (userName == userID):
                return lines[i+1]
            i += 1

        else:
            i += 1


def GenerateKey(password):
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    storePrivate = salt + key
    return storePrivate

def WriteNewUser(userID, storePassword):
    filePopulation.byteIn('users', b'\n')
    filePopulation.byteIn('users', userID.encode())
    filePopulation.byteIn('users', b'\n')
    filePopulation.byteIn('users', storePassword)


def CreateUser(userID, password):
    storePassword = GenerateKey(password)
    WriteNewUser(userID, storePassword)

def IsValidSignIn(userID, password):
    
    if (UserExists(userID)):
        encrypt = GetUserEncrypt(userID)
        storageSalt = encrypt[:32]
        storageKey = encrypt[32:]
        newKey = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), storageSalt, 100000)
        if (newKey == storageKey):
            return True
        else:
            return False