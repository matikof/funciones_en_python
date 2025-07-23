print("*** Funcion con argumentos por nombre ***")
#Esto se hace cuando pasamos valores a una funcion
#y ahi especificamos que tipo de variable vamos a pasar en lugar
#de simplemente usar la posición

def imprimir_persona(nombre , apellido, edad):
    print(f"Persona: Nombre = {nombre}, Apellido = {apellido}, Edad ={edad}")

#Primero llamamos a la funcion usando el metodo normal por posicion
imprimir_persona("Matías", "Torres", 32)
#Ahora llamamos a la funcion usando argumento por nombres.
imprimir_persona(edad=40, nombre="Jose", apellido="jijo")


def imprimir_personas_dos(nombre, apellido = "", edad = ""):
    print(f"Persona: Nombre = {nombre}, Apellido = {apellido}, Edad = {edad}")

