################
# Martín René - @martinvilu
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import tp4eje1

def suma_lenta(numero, otro_numero):
    suma = numero
    if otro_numero < 0:
        for _ in range(0,otro_numero,-1):
            suma-=1
    else:
        for _ in range(0,otro_numero):
            suma+=1

    return suma

def prueba():
    try:
        num1 = tp4eje1.ingreso_entero('Ingrese numero 1')
    except tp4eje1.IngresoIncorrecto as err:
        print(f'{err}')
    try:
        num2 = tp4eje1.ingreso_entero('Ingrese numero 2')
    except tp4eje1.IngresoIncorrecto as err:
        print(f'{err}')
    
    print(suma_lenta(num1,num2))

if __name__ == '__main__':
    prueba()