################
# Martín René - @martinvilu
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
class IngresoIncorrecto(Exception):
    """Esta es la Excepcion para el ingreso incorrecto"""
    pass 

def ingreso_entero_reintento(mensaje, cantidad_reintentos=5):
    intentos = cantidad_reintentos
    while intentos > 0:
        try:
            return ingreso_entero(mensaje)
        except ValueError:
            raise IngresoIncorrecto('No es un numero')
            cantidad_reintentos -= 1
    
    print(f'los {intentos} fueron todos utilizados')
        

def ingreso_entero_restringido(mensaje,valor_minimo=0, valor_maximo=10):
    msg = f'{mensaje} entre {valor_minimo} y {valor_maximo}'
    num = ingreso_entero(msg)
    if num >= valor_minimo and num <= valor_maximo:
        return num
    else:
        raise IngresoIncorrecto(msg)


def ingreso_entero(mensaje):
    """
    Esta funcion muestra un mensaje y agrega la # para indicar el ingreso
    de un número entero.
    """
    ingreso = input(mensaje + " #")
    try:
        entero = int(ingreso)
    except ValueError as err:
        raise IngresoIncorrecto("No era un número!") from err
    return entero


def prueba():
    msg = 'da un numero'

    num = ingreso_entero('Ingrese numero')
    print(f'el numero es => {num}')

    num = ingreso_entero_reintento(msg)
    print(f'numero => {num}')

    num = ingreso_entero_restringido(msg)
    print(f'numero => {num}')




if __name__ == '__main__':
    prueba()


