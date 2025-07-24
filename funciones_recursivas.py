print("*** Primer Ejemplo de funcion recursiva ***")

def funcion_recursiva(num):
    if num == 1:
        print(num)
    else:
        #Al imprimir el numero antes de volver a llamar a la funcion
        print(num)#Vamos a obtener 5-4-3-2-1
        funcion_recursiva(num -1)
funcion_recursiva(5)

def funcion_recursiva_dos(num):
    if num == 1:
        print(num)
    else:
        #Acá pasa algo distinto porque estamos llamando a la funcion
        funcion_recursiva_dos(num -1)#antes de imprimir el num entonces
        print(num)#este print queda a la espera y es como si fuese
        #en reversa porque el primer caso a imprimir va a ser el 1
        #o sea la salida va a ser 1-2-3-4-5

funcion_recursiva_dos(5)