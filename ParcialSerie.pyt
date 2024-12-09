
n= int(input("ingrese un valor entero de su eleccion"))

while (n>1):#iniciamos el ciclo para que se termine en 1

    if((n%2)==0):#si el numero es impar se realiza la operacion y se imprime
        n=n/2
        print(n)
    else:#si el nimero es impar se realiza la seguna operacion y se imprime
        n=(n*3)+1
        print(n)
    #mientras ninguna de las operaciones realizadas de 1 el ciclo se repite