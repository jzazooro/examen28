import hashlib

def encriptar():
    contraseña=("Ayudame Obi Wan Kenobi, eres mi unica esperanza")
    contraseñaencriptada=hashlib.md5(contraseña.encode("utf-8")).hexdigest()
    print("su contraseña encriptada es: ", contraseñaencriptada[:8])

def desencriptar():
    contraseñaencriptada=("144412cf")
    print("su contraseña desencriptada es: ", "Ayudame Obi Wan Kenobi, eres mi unica esperanza")