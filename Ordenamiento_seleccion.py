def seleccion(lista):
    for i in range(len(lista)-1):
        menor=i
        for j in range(i+1,len(lista)):
            if lista[j]<lista[menor]:
                menor=j
        temp=lista[menor]
        lista[menor]=lista[i]
        lista[i]=temp
    return lista
print(seleccion([5,7,3,1,4,2,6]))