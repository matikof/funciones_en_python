#Alcance de variables en Python
print("*** Alcance de variables en Python ***")

#Declaramos una variable Global
contador_global = 0
#Definimos una función para trabajar con los alcances
def incrementar_contador():
    #Definimos el contador local a la función
    contador_local = 0
    #Indicamos que vamos a trabajar con una variable global
    global contador_global
    #Ahora incrementamos la variable global en 1
    contador_global += 1
    #Hacemos lo mismo con la variable local
    contador_local += 1
    #Imprimimos ambos valores para ver como trabajan
    print(f"Valor de la Variable Local: {contador_local}")
    print(f"Valor de la Variable Global: {contador_global}")

#LLamamos a la función varias veces
incrementar_contador()#variable_local = 1, variable_global = 1
incrementar_contador()#variable_local = 1, variable_global = 2
incrementar_contador()#variable_local = 1, variable_global = 3
#Incluso con esta podemos mantar a imprimir la variable_global
#con el nuevo valor de forma externa de la funcion
print(f"Valor final de la Variable Global: {contador_global}")


