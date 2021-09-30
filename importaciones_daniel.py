def orden_entrega(D: list)->list:

    lista_ordenada = D.copy()
    lista_ordenada.sort()
    indice = 0
    encontrado = False
    retorno = []

    print(lista_ordenada)

    for elemento in lista_ordenada:
        encontrado = False
        while encontrado == False:

            if elemento == D[indice]:

                retorno.append(indice)
                encontrado = True
                D[indice] = "a"
                indice = 0
            else:

                indice += 1

    return retorno

a = [2,3,7,4,2,3]

print(orden_entrega(a))







