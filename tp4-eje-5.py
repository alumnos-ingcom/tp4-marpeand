################
# Martín René - @martinvilu
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import tp4eje1

def signo(numero):
    if numero > 0:
        return 1
    elif numero < 0:
        return -1
    else:
        return 0

def prueba():
    try:
        n = tp4eje1.ingreso_entero('Ingrese numero')
    except tp4eje1.IngresoIncorrecto as err:
        print(f'{err}')

    result = signo(n)
    if result == 1:
        print('el numero es positivo')
    elif result == -1:
        print('el numero es negativo')
    else:
        print('el numero es 0')

if __name__ == '__main__':
    prueba()