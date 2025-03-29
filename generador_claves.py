import random

def generar_clave(longitud):
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    clave = "".join(random.choice(caracteres) for _ in range(longitud))
    return clave

print(generar_clave(12))
