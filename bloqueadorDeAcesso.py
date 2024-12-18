import databaseManager
import time

# 10 segundos * quantidade de acessos negados em sequência
def checkUserCooldown(user):
    qtdAcessos = getAcessosNegados(user)
    cooldown = qtdAcessos * 10
    startOfTimeout = getUltimoAcessoNegado(user)
    if time.time() > cooldown + startOfTimeout:
        return 0
    else:
        return (cooldown + startOfTimeout) - time.time()

def incrementarAcessosNegados(user):
    databaseManager.incrementarAcessosNegados(user)

def resetarAcessosNegados(user):
    databaseManager.resetarAcessosNegados(user)

def getAcessosNegados(user):
    return databaseManager.getAcessosNegados(user)

def getUltimoAcessoNegado(user):
    return databaseManager.getultimoAcessoNegado(user)


def atualizarAcessosNegados(user):
    databaseManager.incrementarAcessosNegados(user)
