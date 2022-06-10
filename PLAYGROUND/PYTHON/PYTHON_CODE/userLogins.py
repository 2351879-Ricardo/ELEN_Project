# version 0.3.1
# Author: R. Costa-Tre
# Last endited: R. Costa-Tre (10 June 2022)

import hashlib
import os
import filePopulation

# Return True/False depending if UserID exists in log
def UserExists(userID):
    # Read in database of users (text file)
    lines = filePopulation.byteOut('users')

    i = 0

    # Checks if there are any users in the database already
    if (len(lines) == 0):
        return False

    # Checks each user entry for corresponding userID
    while (i < len(lines)):
        if (i == 0):
            i += 1
        if (i % 2 == 1):
            userName = lines[i].decode().replace('\n', '')
            if (userName == userID):
                return True
            i += 1

        # Purely incremental. 
        # This line contains the encrypted password.
        else:
            i += 1

    # Returns False if UserID doesn't already exist
    return False

def GetUserEncrypt(userID):
    # Read in database of users (text file)
    lines = filePopulation.byteOut('users')

    i = 0
    # Searches for userID among entries
    while (i < len(lines)):
        if (i == 0):
            i += 1
        if (i % 2 == 1):
            userName = lines[i].decode().replace('\n', '')
            if (userName == userID):
                return lines[i+1]
            i += 1

        # Purely incremental. 
        # This line contains the encrypted password.
        else:
            i += 1

# Generates encrypted password for new user
def GenerateKey(password):
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    storePrivate = salt + key
    return storePrivate

# Writes new user to database
def WriteNewUser(userID, storePassword):
    filePopulation.byteIn('users', b'\n')
    filePopulation.byteIn('users', userID.encode())
    filePopulation.byteIn('users', b'\n')
    filePopulation.byteIn('users', storePassword)


def CreateUser(userID, password):
    storePassword = GenerateKey(password)
    WriteNewUser(userID, storePassword)

# Checks if information for sign in is correct
def IsValidSignIn(userID, password):
    # Checks if userID exists in the database
    if (UserExists(userID)):
        # Get the encrypted password
        encrypt = GetUserEncrypt(userID)

        # Seperate the password key and the salt used for its generation
        storageSalt = encrypt[:32]
        storageKey = encrypt[32:]

        # Encrypts the attempted password using the exisiting salt
        newKey = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), storageSalt, 100000)

        # Checks if the password is actually correct
        if (newKey == storageKey):
            return True
        else:
            return False  
    
    # Returns False on invalid UserID
    return False
