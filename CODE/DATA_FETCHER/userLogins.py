import hashlib
import os
import pickle
import filePopulation

def UserExists(userID):
    lines = filePopulation.dataOut('users')
    userExists = False
    for line in lines:
        splitLine = line.split("#")
        if (splitLine[0] == userID):
            userExists = True
            break;
    return userExists

def GetUserEncrypt(userID):
    lines = filePopulation.dataOut('users')
    i = 0
    for thisLine in lines:
        splitLine = thisLine.split("#")
        if (splitLine[0] == userID):
            return thisLine

    return "NO INFO"

def GenerateKey(password):
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    storePrivate = salt + key
    print(storePrivate)
    return storePrivate

def WriteNewUser(userID, storePassword, carInfo):
    userInfo = str(userID) + "#" + str(storePassword) + "#" + str(carInfo)
    filePopulation.dataIn('users', userInfo)    


def CreateUser(userID, password, carInfo):
    storePassword = GenerateKey(password);
    WriteNewUser(userID, storePassword, carInfo)

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

CreateUser("Test", "Test", "Test")