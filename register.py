import databaseManager
import criptografia

def register(username, password):
    salt = criptografia.generate_salt()
    hashedPassword = criptografia.strToSHA256(password, salt)
    status = databaseManager.addUser(username, hashedPassword, salt)
    if status == False:
        print("Username is already being used")
        return False
    else:
        print("User registered")
        return True
