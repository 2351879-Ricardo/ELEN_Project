import hashlib
import os
import filePopulation

def UserExists(userID):
    lines = filePopulation.dataOut('users')
    userExists = False
    for line in lines:
        splitLine = line.split("-")
        if (splitLine[0] == userID):
            userExists = True
            break;
    return userExists

def GetUserEncrypt(userID):
    lines = filePopulation.dataOut('users')
    for thisLine in lines:
        print("Line Read")
        print(thisLine)
        splitLine = thisLine.split("-")
        if (splitLine[0] == userID):
            return splitLine[1]

    return "NO INFO"

def GenerateKey(password):
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    storePrivate = salt + key
    print("Store Private")
    print(storePrivate)
    return storePrivate

def WriteNewUser(userID, storePassword):
    userInfo = str(userID) + "-" + str(storePassword)
    filePopulation.dataIn('users', userInfo)    


def CreateUser(userID, password):
    storePassword = GenerateKey(password);
    WriteNewUser(userID, storePassword)

def IsValidSignIn(userID, password):
    print("tester")
    if (UserExists(userID)):
        encrypt = GetUserEncrypt(userID)
        print("Encrypt")
        print(encrypt)
        # Change encrypt to bytes
        storageSalt = encrypt[:32]
        print(storageSalt)
        storageKey = encrypt[32:]
        newKey = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), storageSalt, 100000)

        if (newKey == storageKey):
            return True
        else:
            return False

CreateUser("Test", "Test")
print(IsValidSignIn("Test", "Test"))
