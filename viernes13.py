import datetime as d

def dia(dia: int, mes: int, anio: int)->str:

    fecha =  d.date(anio,mes,dia)
    dia = fecha.weekday()
    semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    return semana[dia]

print(dia(31,12,2021))