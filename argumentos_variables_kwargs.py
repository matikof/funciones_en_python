print("*** Argumentos Variables Kwargs ***")

def superheroe_superpoderes(nombre, *args, **kwargs):
    print(f"Nombre: {nombre}, Poderes(tupla): {args}, Mas Info: {kwargs}")

#Ingresamos
superheroe_superpoderes("SpiderMan", "Sentido Aracnido","Telaraña", nombre_real = "Peter Parker", pareja = "Mary Jane")