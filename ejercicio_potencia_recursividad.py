print("*** Recursividad ***")

def potencia_numero(numero, potencia):
    if potencia == 0:
        return 1
    else:
        potencia_parcial =  numero * potencia_numero(numero, potencia - 1)
        print(potencia_parcial)
        return potencia_parcial

potencia_numero(2,5)