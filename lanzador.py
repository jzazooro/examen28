from ejercicio2.pregunta2 import determinateiterativo
from ejercicio2.pregunta2 import determinanterecursivo

def main():
    w=int(input("¿Que ejercicio desea hacer?: "))
    if w == 1:
        a=0
    if w == 2:

        def main2():
            determinateiterativo()
            
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
            determinanterecursivo(matriz, 0, 0)
        main2()
        
    if w == 3:
        a=2
    if w == 4:
        a=3
    if w == 5:
        a=4
    if w < 1 or w > 5:
        print("Ha seleccionado un ejercicio inexistente")