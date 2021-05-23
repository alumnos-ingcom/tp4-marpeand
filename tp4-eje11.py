################
# Martín René - @martinvilu
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def palindromo(palabra):
    longitud = len(palabra)
    palindromos = 0
    x = 0
    

    for i in reversed(range(0,longitud)):
        if palabra[i] == palabra[x]:
            palindromos += 1
        x+=1
    
    if palindromos == longitud:
        return True
    else:
        return False


def prueba():
    texto = str(input('Ingrese palabra: '))
    print(palindromo(texto))

if __name__ == '__main__':
    prueba()