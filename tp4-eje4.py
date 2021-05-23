################
# Martín René - @martinvilu
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import tp4eje1

def compara(numero, otro_numero):
    if numero < otro_numero:
        return -1
    elif numero > otro_numero:
        return 1
    else:
        return 0

def prueba():
    try:
        num_1 = tp4eje1.ingreso_entero('Ingrese un numero')
    except tp4eje1.IngresoIncorrecto as err:
        print(f'{err}')
    
    try:
        num_2 = tp4eje1.ingreso_entero('Ingrese otro numero')
    except tp4eje1.IngresoIncorrecto as err:
        print(f'{err}')

    print(compara(num_1,num_2))

if __name__ == '__main__':
    prueba()