#Regrasamos una tupla mediante una función

print("*** Regresar una tupla de valores desde una función ***")

#Definición de funcion

def persona_mayusculas(nombre, apellido, edad):
    print(f"Esta función regresa varios valores (tupla)")
    return (nombre.upper(), apellido.upper(), edad)

#LLamamos a una función para asignar cada valor
#a cada variable usamos unpacking(desempaquetado)

nombre, apellido , edad = persona_mayusculas("Matías","Torres", 32)
print(f"Los datos de la Persona: nombre = {nombre}, apellido = {apellido}, edad = {edad}")