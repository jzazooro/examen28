# examen28

El enlace al repositorio de GitHub de este proyecto es el siguiente: [GitHub](https://github.com/jzazooro/examen28.git)

He realizado los siguientes 5 ejercicios propuestos en el examen

El codigo creado para realizar este examen es el siguiente:

### main:

```
from lanzador import main

if __name__ == '__main__':
    main()
```

### lanzador:

```

```

### ejercicio 1:

```
def torredehanoi(discos, torredeorigen=1, torreauxiliar=2, torrededestino=3):
    if discos == 1:
        print("va de la ", torredeorigen, "a la", torrededestino)
    else:
        torredehanoi(discos-1, torredeorigen, torrededestino, torreauxiliar)
        print("va de la ", torredeorigen, "a la", torrededestino)
        torredehanoi(discos-1, torreauxiliar, torredeorigen, torrededestino)
    return
```


### ejercicio 2:

```
def determinateiterativo():
    a=float(input("Seleccione el elemento 1x1 de la matriz: "))
    b=float(input("Seleccione el elemento 1x2 de la matriz: "))
    c=float(input("Seleccione el elemento 1x3 de la matriz: "))
    d=float(input("Seleccione el elemento 2x1 de la matriz: "))
    e=float(input("Seleccione el elemento 2x2 de la matriz: "))
    f=float(input("Seleccione el elemento 2x3 de la matriz: "))
    g=float(input("Seleccione el elemento 3x1 de la matriz: "))
    h=float(input("Seleccione el elemento 3x2 de la matriz: "))
    i=float(input("Seleccione el elemento 3x3 de la matriz: "))
    determinante = a*e*i + d*h*c + b*f*g - c*e*g -b*d*i - a*f*h
    matriz=[[a, b, c], [d, e, f], [g, h, i]]
    print("El determinate de su matriz es: ", determinante)




def determinanterecursivo(matriz, i, parametro):
    if i == 0:
        parametro = matriz[0][0]*matriz[1][1]*matriz[2][2]+parametro
        determinanterecursivo(matriz, i+1, parametro)
    if i == 1:
        parametro = matriz[2][0]*matriz[1][2]*matriz[0][1]+parametro
        determinanterecursivo(matriz, i+1, parametro)
    if i == 2:
        parametro = matriz[1][0]*matriz[2][1]*matriz[0][2]+parametro
        determinanterecursivo(matriz, i+1, parametro)
    if i == 3:
        parametro = parametro-matriz[0][2]*matriz[1][1]*matriz[2][0]
        determinanterecursivo(matriz, i+1, parametro)
    if i == 4:
        parametro = parametro-matriz[0][1]*matriz[1][0]*matriz[2][2]
        determinanterecursivo(matriz, i+1, parametro)
    if i == 5:
        parametro = parametro-matriz[0][0]*matriz[2][1]*matriz[1][2]
        print("El determinante de su matriz es: ", parametro)
```

### ejercicio 3:

```
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
```

### ejercicio 4:

```

```

### ejercicio 5:

```

```
