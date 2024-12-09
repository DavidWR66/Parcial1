
año=2022#Datos iniciales

a=25000000#Datos iniciales

b=18900000#Datos iniciales

while(a>b):#inicio del ciclo que se terminara cuando 
           #la pobacion de b sea mayor que la poblacion de a
    b= int(b+(b*0.03))#crecimiento de la poblacion B

    a= int(a+(a*0.02))#crecimiento de la poblacion A

    año= año + 1#contador para saber en que año estamos

print ("la poblacion de A=",a)#resultados de la prueba
print ("la poblacion de B=",b)#resultados de la prueba
print ("En el año",año)#resultados de la prueba