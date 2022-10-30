class Vehiculo:
    def __init__(self, nombre, largo, trip, pasajeros):
        self.nombre = nombre
        self.largo = largo
        self.trip = trip
        self.pasajeros = pasajeros

    def __str__(self):
        return "{}, {}, {}, {}".format(self.nombre, self.largo, self.trip, self.pasajeros)

    def get_largo(self):
        return self.largo

    def diccionario(self):
        diccionario = {"Nombre": self.nombre , "Largo": self.largo , "Tripulacion": self.trip , "Pasajeros": self.pasajeros}
        return diccionario

class Vehiculos:
    def __init__(self):
        self.naves = []

    def naves_append(self, nave):
        self.naves.append(nave)

    def get_Nombres(self, lista, key):
        lista2 = []
        for i in lista:
            for n in self.naves:
                if n[key] == i:
                    lista2.append(n["Nombre"])
        return lista2

    def lis_largo(self):
        lista = []
        for i in self.naves:
            lista.append(i["Largo"])
        lista.sort(reverse=True)
        return self.get_Nombres(lista, "Largo")
    
    def lis_nombre(self):
        lista = []
        for i in self.naves:
            lista.append(i["Nombre"])
        lista.sort()
        return lista

    def cantidad_pasajeros(self):
        lista = []
        for i in self.naves:
            lista.append(i["Pasajeros"])
        lista.sort()
        return self.get_Nombres(lista, 'Pasajeros')[0:5]

    def mayor_trip(self):
        lista = []
        for i in self.naves:
            lista.append(i["Tripulacion"])
        lista.sort()
        return self.get_Nombres(lista, "Tripulacion")[0:1]

    def at(self):
        naves_nombre = self.lis_nombre()
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

    def pasajeros_6_o_mas(self):
        lista = []
        for i in self.naves:
            if i ["Pasajeros"] >= 6:
                lista.append(i["Pasajeros"])
        return self.get_Nombres(lista, "Pasajeros")

    def naves_peq_grand(self):
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