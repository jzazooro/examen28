from ejercicio2.pregunta2 import determinateiterativo
from ejercicio2.pregunta2 import determinanterecursivo
from ejercicio3.pregunta3 import Vehiculo
from ejercicio3.pregunta3 import Vehiculos

def main():
    w=int(input("¿Que ejercicio desea hacer?: "))
    if w == 1:
        a=0
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
        a=3
    if w == 5:
        a=4
    if w < 1 or w > 5:
        print("Ha seleccionado un ejercicio inexistente")