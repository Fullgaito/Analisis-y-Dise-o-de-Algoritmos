"""Compara de a dos elementos y determina si el siguiente elemento es menor o no en caso de que si
los cambia de posicion y hace esto hasta que el vector quede ordenado"""
def burbuja(lista):
    ordenado = False
    while not ordenado:
        ordenado = True  # Se establece en True al inicio de cada iteración
        for i in range(len(lista) - 1):
            puntero1 = lista[i]
            puntero2 = lista[i + 1]
            if puntero2 < puntero1:
                puntero2, puntero1 = puntero1, puntero2
                lista[i] = puntero1
                lista[i + 1] = puntero2
                ordenado = False  # Si hay un intercambio, la lista aún no está ordenada
    return lista

print(burbuja([5, 3, 1, 4, 2,6,9,8,11,13,12]))  


            