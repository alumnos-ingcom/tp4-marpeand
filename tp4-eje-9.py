################
# Martín René - @martinvilu
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import tp4eje1

def es_primo(numero):
    for x in range(2,numero):
        if numero % x == 0:
            pass

    return True


def prueba():
    try:
        num = tp4eje1.ingreso_entero('Ingrese numero')
    except tp4eje1.IngresoIncorrecto as err:
        print(f'{err}')
    print(es_primo(num))

if __name__ == '__main__':
    prueba()