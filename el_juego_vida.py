def juego_vida(gente: list)->int:
    indice = 0
    vecinos = 0
    while indice != 99:

        if gente[indice+1] == 1:
            vecinos += 1
        if gente[indice-1] == 1:
            vecinos += 1
        if gente[indice+10] == 1:
            vecinos += 1
        if gente[indice-10] == 1:
            vecinos += 1
        if gente[indice-11] == 1:
            vecinos += 1
        if gente[indice]

        