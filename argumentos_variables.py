print("*** Argumentos Variables en Java ***")
#Definimos una función la cual va a pedir argumentos posicionales
#Pero también va a tener la posibilidad de ingresar argumentos
#variables
def superheroe_superpoder(superheroe, nombre, *poderes):
    print(f"SuperHeroe: {superheroe} -> Nombre Real: {nombre} -> Poderes: {poderes}")
    for poder in poderes:
        print(f"Poder -{poder}")

superheroe_superpoder("SpiderMan", "Peter Parker", "Instinto Aracnido", "Telaraña")

#Volvemos a llamar a la función para comprobar que se pueden pasar
#una cantidad cualquiera de argumentos(incluso ninguno)
superheroe_superpoder("Batman", "Bruce Wayne", "Millonario", "Traje","Artefactos")
#¡¡¡¡Importante!!!!
#   *args debe pedirse al final de la peticion de argumentos
#   en la función, ya que como tenemos argumentos posicionales
#   nos dará un error por no pasarlos.

