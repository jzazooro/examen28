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