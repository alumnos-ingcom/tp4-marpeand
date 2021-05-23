################
# Martín René - @martinvilu
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import tp4eje1

def division_lenta(dividendo, divisor):
    if dividendo > 0 and divisor > 0:
        cociente = 0
        resto = dividendo

        while resto>divisor:
            resto -= divisor
            cociente+=1
    else:
        print('Los numeros ingresados no son validos')


    return cociente, resto

def prueba():
    try:
        dividendo = tp4eje1.ingreso_entero('Ingrese dividendo')
    except tp4eje1.IngresoIncorrecto as err:
        print(f'{err}')
    
    try:
        divisor = tp4eje1.ingreso_entero('Ingrese divisor')
    except tp4eje1.ingreso_entero as err:
        print(f'{err}')

    cociente, resto = division_lenta(dividendo,divisor)

    print(f'Cociente = {cociente}, resto =  {resto}')


if __name__== '__main__':
    prueba()