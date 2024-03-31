"""Se empieza con el segundo elemento y se busca comparar ese elemento seleccionado con los elementos
que estan al lado izquierdo y si es menor se intercambia de posicion"""

def insercion(lista):
    for i in range(1,len(lista)):
        puntero=lista[i]
        for j in range(0,i):
            if puntero<lista[j]:
                lista[i],lista[j]=lista[j],lista[i]
    return lista
print(insercion([5,3,1,4,2,9,7]))
