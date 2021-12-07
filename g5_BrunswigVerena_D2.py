def suma(numeros):
    sumar = 0

    for numero in numeros: 
        sumar += numero

    return sumar

def prom(numeros):
    return suma(numeros)/len(numeros)

def imprimir(elementos):
    print("mayor: ", max(elementos))
    print("menor: ", min(elementos))
    print("suma: ", suma(elementos))
    print("promedio: ", prom(elementos))



