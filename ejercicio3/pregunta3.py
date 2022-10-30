class Vehiculo:
    def __init__(self, nombre, largo, tripulacion, pasajeros):
        self.nombre = nombre
        self.largo = largo
        self.tripulacion = tripulacion
        self.pasajeros = pasajeros

    def __str__(self):
        return "{}, {}, {}, {}".format(self.nombre, self.largo, self.tripulacion, self.pasajeros)

    def obtenerlargo(self):
        return self.largo

    def diccionario(self):
        diccionario = {"Nombre": self.nombre , "Largo": self.largo , "Tripulacion": self.tripulacion , "Pasajeros": self.pasajeros}
        return diccionario

class Vehiculos:
    def __init__(self):
        self.naves = []

    def agregarvehiculos(self, nave):
        self.naves.append(nave)

    def obtenernombres(self, lista, key):
        lista2 = []
        for i in lista:
            for n in self.naves:
                if n[key] == i:
                    lista2.append(n["Nombre"])
        return lista2

    def funcionlongitud(self):
        lista = []
        for i in self.naves:
            lista.append(i["Largo"])
        lista.sort(reverse=True)
        return self.obtenernombres(lista, "Largo")
    
    def funcionnombre(self):
        lista = []
        for i in self.naves:
            lista.append(i["Nombre"])
        lista.sort()
        return lista

    def cantidaddepasajeros(self):
        lista = []
        for i in self.naves:
            lista.append(i["Pasajeros"])
        lista.sort()
        return self.obtenernombres(lista, 'Pasajeros')[0:5]

    def mayortripulacion(self):
        lista = []
        for i in self.naves:
            lista.append(i["Tripulacion"])
        lista.sort()
        return self.obtenernombres(lista, "Tripulacion")[0:1]

    def buscarat(self):
        naves_nombre = self.funcionnombre()
        lista_nombres = []
        for i in naves_nombre:
            if i[0:2] == "AT":
                lista_nombres.append(i)
            else:
                pass
        if len(lista_nombres) == 0:
            return None
        else:
            return lista_nombres

    def pasajerossuperioraseis(self):
        lista = []
        for i in self.naves:
            if i ["Pasajeros"] >= 6:
                lista.append(i["Pasajeros"])
        return self.obtenernombres(lista, "Pasajeros")

    def ordenardepeqagrand(self):
        lista = []
        for i in self.naves:
            lista.append(i["Largo"])
        lista.sort()
        for i in self.naves:
            if lista[0] == i["Largo"]:
                print(i)
            elif lista[len(lista)-1] == i["Largo"]:
                print(i)
            else:
                pass