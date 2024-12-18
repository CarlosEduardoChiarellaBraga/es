import loginManager
import register
import databaseManager

# usuários criados ao usar o populateDatabase:
# user1: "username_1" senha: "1234"
# user2: "username_2" senha: "1234"

databaseManager.populateDatabase()
 
while True:
    menu = -1
    try: 
        menu = int(input("""
        Selecione uma opção:
            [0] Sair
            [1] Realizar login
            [2] Registrar novo user
            [3] Ver database
            """))
    except:
        print("Digite um número válido")
    if menu == 0:
        break
    if menu == 1:
        user = input("User: ")
        password = input("Password: ")
        loginManager.loginManager(user, password)
    if menu == 2:
        user = input("User: ")
        password = input("Password: ")
        register.register(user, password)

    if menu == 3:
        databaseManager.printDatabase()
