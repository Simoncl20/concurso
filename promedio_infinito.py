def promedio_infinito(a: int, b: int)->float:

    promedio = (a+b) / 2
    contador = 0

    while contador < 1000:
        a = b
        b = promedio
        promedio = (a+b)/2
        contador += 1

    return promedio
