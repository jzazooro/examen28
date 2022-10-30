vehiculo1 = ['Halcon milenario', 30, 2, 40]
vehiculo2 = ['Estrella de la muerte', 1000000000, 2000000, 3000000000]
vehiculo3 = ['AT-AT', 119, 15, 300]
vehiculo4 = ['Sclavo 1', 15, 3, 20]
vehiculo5 = ['Destructor imperial', 1000, 200, 10000]
vehiculo6 = ['AT-ST', 14, 5, 6]

class nave:

    def __init__(self, nombre, largo, tripulacion, cantidaddepasajeros):
        self.nombre = nombre
        self.largo = largo
        self.tripulacion = tripulacion
        self.cantidaddepasajeros = cantidaddepasajeros

    def obtenerlargo(self):
        print(self.largo)

    def diccionario(self):
        diccionario = {'Nombre': self.nombre , 'Largo': self.largo, 'Tripulacion': self.tripulacion, 'Cantidad de pasajeros': self.cantidaddepasajeros}
        print(diccionario)

class naves:

    def __init__(self):
        self.naves=[]

    def obtenernombre(self, lista, key):
        lista2=[]
        for i in lista:
            for n in self.naves:
                if n[key] == i:
                    lista2.append(n['Nombre'])

    def obtenerlargo(self):
        lista3=[]
        for i in self.naves:
            lista3.append(i['Nombre'])
        lista3.sort()
        print(lista3)
    
    def obtenercantidaddepasajeros(self):
        lista4=[]
        for i in self.naves:
            lista4.append(i['Cantidad de pasajeros'])
        lista4.sort()
        print(self.obtenernombre(lista4, 'Cantidad de pasajeros')[0:5])

    def obtenermayortripulacion(self):
        lista5=[]
        for i in self.naves:
            lista5.append(i['Tripulacion'])
        lista5.sort()
        print(self.obtenernombre(lista5, 'Tripulacion')[0:1])
    


    








print("El halcon milenario tiene las siguientes caracteristicas: ", vehiculo1)
print("La estrella de la muerte tiene las siguientes caracteristicas: ", vehiculo2)

vehiculos = [vehiculo1, vehiculo2, vehiculo3, vehiculo4, vehiculo5, vehiculo6]
escuadron = naves()
for i in vehiculos:
    escuadron.navesagregar(i.diccionario())