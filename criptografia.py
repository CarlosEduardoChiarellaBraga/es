import hashlib
import random
import string

def generate_salt(length=16):
    salt = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return salt

def strToSHA256(password, salt):
    salted_password = salt.encode('utf-8') + password.encode('utf-8')
    sha256_hash = hashlib.sha256()
    sha256_hash.update(salted_password)
    hex_hash = sha256_hash.hexdigest()

    return hex_hash
