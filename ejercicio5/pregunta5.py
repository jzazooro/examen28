import hashlib

def encriptar():
    contraseña=input("Que mensaje deseas mandar: ")
    contraseñaencriptada=hashlib.md5(contraseña.encode("utf-8")).hexdigest()
    print("su contraseña encriptada es: ", contraseñaencriptada[:8])