import criptografia
import databaseManager
import bloqueadorDeAcesso
from time import sleep


def autenticar(user, password, verbose = 0):
    userFound, hash, salt = databaseManager.getUserCredencials(user)
    if userFound:
        
        hashExpected = criptografia.strToSHA256(password, salt)

        cooldown = bloqueadorDeAcesso.checkUserCooldown(user)

        if cooldown > 0:
            if verbose > 0:
                print(f"Cooldown de: {cooldown:.2f} segundos")
            return False
        
        if hash == hashExpected:
            if verbose > 0:
                print("Authenticated")
            bloqueadorDeAcesso.resetarAcessosNegados(user)
            return True
        else:
            bloqueadorDeAcesso.incrementarAcessosNegados(user)
            if verbose > 0:
                print("Wrong password")
    else:
        if verbose > 0:
            print("User not found")
    return False

