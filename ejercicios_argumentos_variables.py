print("*** Varios Ejercicios con Argumentos Variables ***")

#Función sumar que acepta una tupla(*args)

def sumar(*args):
    total = 0
    for numero in args:
        total += numero
    return total
resultado = sumar(1,2,4,5,3)
print(f"Resultado de la Suma: {resultado}")