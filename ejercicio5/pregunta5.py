import hashlib

def encriptar():
    mensajesinencriptar = (b"Ayudame Obi Wan Kenobi, eres mi unica esperanza")
    mensajeencriptado = hashlib.sha256(mensajesinencriptar).hexdigest()
    print("El mensaje de la princesa Leia cifrado de forma hexadecimal es: ", mensajeencriptado[:8])
encriptar()