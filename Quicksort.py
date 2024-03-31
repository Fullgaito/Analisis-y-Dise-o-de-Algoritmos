def particion(lista):
    pivote=lista[0]
    izq=[]
    der=[]
    for i in range(1,len(lista)):
        if pivote>lista[i]:
            izq.append(lista[i])
        else:
            der.append(lista[i])
    return izq,pivote,der
def quicksort(lista):
    if len(lista)==1 or len(lista)==0:
        return lista
    else:
        izq,pivote,der=particion(lista)
        return quicksort(izq)+[pivote]+quicksort(der)
print(particion([3,5,1,4,2]))
print(quicksort([3,5,1,4,2]))