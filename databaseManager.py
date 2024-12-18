import sqlite3
import time

def populateDatabase():
    conn = sqlite3.connect('bd.db')

    cursor = conn.cursor()

    cursor.execute('''
        DROP TABLE clientes
                   ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL UNIQUE,
            hash STRING,
            salt STRING,
            AcessosNegados INTEGER,
            ultimoAcessoNegado DOUBLE
        )
    ''')

    cursor.execute('''
        INSERT INTO clientes (nome, hash, salt, AcessosNegados, ultimoAcessoNegado) VALUES
        ('username_1', '5820943308355214f587fcee000b6b3ae97ac4f55ee4d774420eb34743303dab', 'Mvrxodvgke4hXNCw',0, 0.0),
        ('username_2', 'b85a3557421aade29d6e7256f04d913c63869dd62d9e224bc864ae752064a9d3', 'Y4D148bGTL5pTJfV',0, 0.0)
    ''')

    conn.commit()
    conn.close()

def printDatabase():
    conn = sqlite3.connect('bd.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM clientes')

    users = cursor.fetchall()

    conn.close()
    print("(ID, 'USERNAME', 'HASHED_PASSWORD', 'SALT', 'AcessosNegados', 'ultimoAcessoNegado'):")
    for user in users:
        print(user)

def getUserCredencials(username):
    conn = sqlite3.connect('bd.db')

    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM clientes WHERE clientes.nome == \'{username}\'')

    user = cursor.fetchall()

    if not user:
        return False, 0, 0

    conn.close()
    return True, user[0][2], user[0][3]

def checkUserExists(username):
    conn = sqlite3.connect('bd.db')

    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM clientes WHERE clientes.nome == \'{username}\'')

    user = cursor.fetchall()

    conn.close()

    if user:
        return True
    return False

def addUser(username, hashedPassword, salt):
    if checkUserExists(username):
        return False
    else:
        conn = sqlite3.connect('bd.db')

        cursor = conn.cursor()
        cursor.execute(f'''
                INSERT INTO clientes (nome, hash, salt, AcessosNegados, ultimoAcessoNegado) VALUES
                ('{username}', '{hashedPassword}', '{salt}', 0, 0.0)
            ''')

        conn.commit()
        conn.close()

        return True

def incrementarAcessosNegados(user):
    conn = sqlite3.connect('bd.db')

    cursor = conn.cursor()

    cursor.execute(f'''
        UPDATE clientes SET AcessosNegados = AcessosNegados + 1, ultimoAcessoNegado = {time.time()} WHERE nome == '{user}'
    ''')

    conn.commit()
    conn.close()

def resetarAcessosNegados(user):
    conn = sqlite3.connect('bd.db')

    cursor = conn.cursor()

    cursor.execute(f'''
        UPDATE clientes SET AcessosNegados = 0 WHERE nome == '{user}'
    ''')

    conn.commit()
    conn.close()

def getAcessosNegados(user):
    conn = sqlite3.connect('bd.db')

    cursor = conn.cursor()

    cursor.execute(f'''
        SELECT AcessosNegados FROM clientes WHERE nome == '{user}'
    ''')

    AcessosNegados = cursor.fetchall()
    
    conn.commit()
    conn.close()

    return AcessosNegados[0][0]

def getultimoAcessoNegado(user):
    conn = sqlite3.connect('bd.db')

    cursor = conn.cursor()

    cursor.execute(f'''
        SELECT ultimoAcessoNegado FROM clientes WHERE nome == '{user}'
    ''')

    ultimoAcessoNegado = cursor.fetchall()
    
    conn.commit()
    conn.close()

    return ultimoAcessoNegado[0][0]

