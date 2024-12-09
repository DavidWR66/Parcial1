
while True:#iniciamos el ciclo para que no se ingrese numeron negativos
    n= int(input("ingrese un valor entero de su eleccion"))

    if (n>=0):#verificamos que el numero sea positivo
        x=n*n#elevamos el numero al cuadrado
        break#cerramos el ciclo

    else:#en caso de que el numero sea negativo
        print("el numero ingresado no es valido")
        #se repite el ciclo
        
print("el cuadrado del numero ingresado es",x)