################
# Martín René - @martinvilu
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
def minimo(lista):
    min = 0
    for i in lista:
        if i < min:
            min = i
    
    return min

def maximo(lista):
    max = 0
    for x in lista:
        if x > max:
            max = x
    
    return max


def prueba():
    lista = [2,-6,-3,-11,4,6,8,5,2,4,6,7,15,34,65,123,89,43,234]

    print(f'numero maximo en la lista => {maximo(lista)}')
    print(f'numero minimo en la lista => {minimo(lista)}')


if __name__=='__main__':
    prueba()