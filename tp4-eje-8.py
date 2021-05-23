################
# Martín René - @martinvilu
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import tp4eje1

def ordenar_mayor_a_menor(uno, dos, tres):
    mayor_menor = [uno, dos, tres]
    mayor_menor.sort()
    tupla_mayor_menor = tuple(mayor_menor)
    return tupla_mayor_menor
            

def ordenar_menor_a_mayor(uno, dos, tres):
    menor_mayor = [uno,dos,tres]
    menor_mayor.reverse()
    tupla_menor_mayor = tuple(menor_mayor)
    return tupla_menor_mayor


def prueba():
    try:
        num1 = tp4eje1.ingreso_entero('Ingrese el primer numero')
    except tp4eje1.IngresoIncorrecto as err:
        print(f'{err}')
    try:
        num2 = tp4eje1.ingreso_entero('Ingrese el segundo numero')
    except tp4eje1.IngresoIncorrecto as err:
        print(f'{err}')
    try:
        num3 = tp4eje1.ingreso_entero('Ingrese el tercer numero')
    except tp4eje1.IngresoIncorrecto as err:
        print(f'{err}')
    

    mayor_menor = ordenar_mayor_a_menor(num1,num2,num3)
    menor_mayor = ordenar_menor_a_mayor(num1,num2,num3)

    print(f'Numeros ordenados de mayor a menor => {mayor_menor}')
    print(f'Numeros ordenados de menor a mayor => {menor_mayor}')

if __name__ == '__main__':
    prueba()