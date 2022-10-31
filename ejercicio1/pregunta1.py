class torredehanoi:

    def __init__(self):
        print("empieza el ejercicio")

    def hanoi(self, discos, torredeorigen=1, torreauxiliar=2, torrededestino=3):
        if discos == 1:
            print("va de la", torredeorigen, "a la", torrededestino)
        else:
            self.hanoi(discos-1, torredeorigen, torreauxiliar, torrededestino)
            print("va de la", torredeorigen, "a la", torrededestino)
            self.hanoi(discos-1, torredeorigen, torreauxiliar, torrededestino)
