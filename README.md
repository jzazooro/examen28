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
from ejercicio1.pregunta1 import torredehanoi
from ejercicio2.pregunta2 import determinateiterativo
from ejercicio2.pregunta2 import determinanterecursivo
from ejercicio3.pregunta3 import Vehiculo
from ejercicio3.pregunta3 import Vehiculos
from ejercicio5.pregunta5 import encriptar

def main():
    
    w=int(input("¿Que ejercicio desea hacer?: "))
    
    if w == 1:
        
        def main1():
            k=int(input("¿cuantos discos desea que haya? Deben ser entre 1 y 11, si no, se hara con 11 discos. Asi evitamos desborde la pila: "))
            if k >= 1 and k <= 11:
                torredehanoi(k)
            else:
                torredehanoi(11)

        main1()

    if w == 2:

        def main2():
            
            a=float(input("Seleccione el elemento 1x1 de la matriz: "))
            b=float(input("Seleccione el elemento 1x2 de la matriz: "))
            c=float(input("Seleccione el elemento 1x3 de la matriz: "))
            d=float(input("Seleccione el elemento 2x1 de la matriz: "))
            e=float(input("Seleccione el elemento 2x2 de la matriz: "))
            f=float(input("Seleccione el elemento 2x3 de la matriz: "))
            g=float(input("Seleccione el elemento 3x1 de la matriz: "))
            h=float(input("Seleccione el elemento 3x2 de la matriz: "))
            i=float(input("Seleccione el elemento 3x3 de la matriz: "))
            matriz=[[a, b, c], [d, e, f], [g, h, i]]
            determinateiterativo(a, b, c, d, e, f, g, h, i)
            determinanterecursivo(matriz, 0, 0)
        main2()
        
    if w == 3:

        def main3():
    
            vehiculo1 = Vehiculo("Halcon milenario", 30, 2, 40)
            vehiculo2 = Vehiculo("Estrella de la muerte", 1000000000, 2000000, 3)
            vehiculo3 = Vehiculo("AT-AT", 119, 15, 300)
            vehiculo4 = Vehiculo("Sclavo 1", 15, 3, 200)
            vehiculo5 = Vehiculo("Destructor imperial", 1000, 200, 10000)
            vehiculo6 = Vehiculo("AT-ST", 14, 5, 6)
            vehiculo7 = Vehiculo("Canonera LAAT ", 51, 61, 82)
            vehiculo8 = Vehiculo("Ala X", 7, 1, 1)
            vehiculo9 = Vehiculo("Ala A", 6, 2, 2)
            vehiculo10 = Vehiculo("Caza tie", 5, 1, 2)

            
            print("La informacion del halcon milenario es: ", vehiculo1)
            print("La informacion de la estrella de la muerte es: ", vehiculo2)
            
            listadevehiculos= [vehiculo1, vehiculo2, vehiculo3, vehiculo4, vehiculo5, vehiculo6, vehiculo7, vehiculo8, vehiculo9, vehiculo10]
            garage = Vehiculos()
            for i in listadevehiculos:
                garage.agregarvehiculos(i.diccionario())
            
            print("Las cinco naves con mas cantidad de pasajeros son: ", garage.cantidaddepasajeros())
            print("El vehiculo que necesita menos tripulacion es: ", garage.mayortripulacion())
            print("Los vehiculos que empiezan por AT son: ", garage.buscarat())
            print("Los vehiculos que pueden llevar 6 o mas pasajeros son: ", garage.pasajerossuperioraseis())
            print("Los vehiculos ordenados de peques a grandes son: ", garage.ordenardepeqagrand())
    
        main3()

    if w == 4:
    
        print("Lo siento mucho, no he conseguido resolver este ejercicio")
    
    if w == 5:
    
        def main5():
    
            encriptar()

        main5()
    
    if w < 1 or w > 5:
    
        print("Ha seleccionado un ejercicio inexistente")
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
