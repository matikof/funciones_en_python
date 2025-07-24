print("*** Varios Ejercicios con Argumentos Variables ***")
#Función sumar que acepta una tupla(*args)
def sumar(*args):
    total = 0
    for numero in args:
        total += numero
    return total
resultado = sumar(1,2,4,5,3)
print(f"Resultado de la Suma: {resultado}")

print("--- Ejemplo con **kwargs ---")
def imprimir_detalle_persona(**kwargs):
    print("\nDetalle Persona:")
    #Al usar .items() devolvemos una tupla
    for llave, valor in kwargs.items():
        print(f"{llave}:{valor}")

imprimir_detalle_persona(nombre="Matías", edad = 32, ciudad = "Moreno")

#funcion par
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
#Con esto solo dejamos ejecutar esto desde este mismo archivo
#y no desde uno externo
if __name__ == "__main__":
    numero = int(input("Proporciona un valor númerico: "))
    print(f"Es un número par? {es_par(numero)}")
