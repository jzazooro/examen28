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

    def agregarnaves(self, nave):
        self.naves.append(nave)

    def obtenernombre(self, lista2, key):
        lista2=[]
        for i in lista2:
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
        print(lista4[0:5])

    def obtenermayortripulacion(self):
        lista5=[]
        for i in self.naves:
            lista5.append(i['Tripulacion'])
        lista5.sort()
        print(lista5[0:1])

    def bucarat(self):
        nombres= self.obtenernombre()
        lista6=[]
        for i in nombres:
            if i[0:2] == 'AT':
                lista6.append(i)
            else:
                pass
        print(lista6)

    def masdeseispasajeros(self):
        lista7=[]
        for i in self.naves:
            if i ['Cantidad de pasajeros'] >=6:
                lista7.append(i['Cantidad de pasajeros'])
        print(lista7)

    def depequeñoagrande(self):
        lista8=[]
        for i in self.naves:
            lista8.append(i['Largp'])
        lista8.sort()
        for i in self.naves:
            if lista8[0] == i['Largo']:
                print(i)
            elif lista8[len(lista8)-1] == i['Largo']:
                print(i)
            else:
                pass

def main3():

    vehiculo1 = ['Halcon milenario', 30, 2, 40]
    vehiculo2 = ['Estrella de la muerte', 1000000000, 2000000, 3000000000]
    vehiculo3 = ['AT-AT', 119, 15, 300]
    vehiculo4 = ['Sclavo 1', 15, 3, 20]
    vehiculo5 = ['Destructor imperial', 1000, 200, 10000]
    vehiculo6 = ['AT-ST', 14, 5, 6]

    print(vehiculo1)
    print(vehiculo2)

    ejercito = naves()
    
    print(ejercito.obtenercantidaddepasajeros())
    print(ejercito.obtenermayortripulacion())
    print(ejercito.bucarat())
    print(ejercito.masdeseispasajeros())
    print(ejercito.depequeñoagrande())
main3()