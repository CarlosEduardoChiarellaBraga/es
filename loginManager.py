import autenticador


def loginManager(user, password):
    return autenticador.autenticar(user, password, 1)
    

