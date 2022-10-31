def torredehanoi(discos, torredeorigen=1, torreauxiliar=2, torrededestino=3):
    if discos == 1:
        print("va de la ", torredeorigen, "a la", torrededestino)
    else:
        torredehanoi(discos-1, torredeorigen, torrededestino, torreauxiliar)
        print("va de la ", torredeorigen, "a la", torrededestino)
        torredehanoi(discos-1, torreauxiliar, torredeorigen, torrededestino)
    return