
################
# Martín René - @martinvilu
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import tp4eje1

def convertir_a_fahrrenheit(centigrados):
    fahr = (centigrados * 9/5) + 32
    return fahr

def convertir_a_centigrados(fahrenheit):
    centi = (fahrenheit - 32) * 5/9
    return centi

def prueba():
    try:
        temp_centi = tp4eje1.ingreso_entero('Ingrese temperatura en Celcius')
    except tp4eje1.IngresoIncorrecto as err:
        print(f'{err}')
    
    try:
        temp_fahr = tp4eje1.ingreso_entero('Ingrese temperatura en fahrenheit')
    except tp4eje1.IngresoIncorrecto as err:
        print(f'{err}')

    print(f'{temp_centi} grados a fahrenheit => {convertir_a_fahrrenheit(temp_centi)}')
    print(f'{temp_fahr} grados a centigrados => {convertir_a_centigrados(temp_centi)}')

if __name__ == '__main__':
    prueba()