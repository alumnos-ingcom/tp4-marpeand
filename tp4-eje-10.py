################
# Martín René - @martinvilu
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import tp4eje1
def factor_primo(numero):
    numeros = []

    for i in range(2,numero):
        while numero % i == 0:
            numeros.append(i)
            numero/=i
    
    return tuple(numeros)

def prueba():
    try:
        num = tp4eje1.ingreso_entero('Ingrese numero')
    except tp4eje1.IngresoIncorrecto as err:
        print(f'{err}')
    print(factor_primo(num))

if __name__ == '__main__':
    prueba()