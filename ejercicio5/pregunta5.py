import hashlib

def encriptar():
    contraseña=("Ayudame Obi Wan Kenobi, eres mi unica esperanza")
    contraseñaencriptada=hashlib.md5(contraseña.encode("utf-8")).hexdigest()
    print(contraseñaencriptada[:8])