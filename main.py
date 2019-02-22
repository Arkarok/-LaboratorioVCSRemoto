 
print("Calcular el producto de dos numeros enteros")

a=int(input("Digita un numero, Por favor: "))
c=int(input("Digita un numero, Por favor: "))

producto=a*c

producto_de_a=a*2

print(producto)

print(producto_de_a)

print("Se ha calculado con exito")

import math

print("Calcular una potencia de un numero b y una raiz de un numero d")

b=int(input("Digita un numero, Por favor: "))
d=int(input("Digita un numero, Por favor: "))

potencia=pow(b,2)

print("La potencia es " + str(potencia))

raiz=math.sqrt(d)

print("La raiz es " + str(raiz))

print("Se ha calculado con exito")

print("Funcion Cuadratica")

import math

a=int(input('Ingrese el valor de a '))

if a==0:
    print('El valor de "a" no puede ser cero ')
    print('reingrese el valor de "a" ')
    
    a=int(input('Ingrese el valor de a: '))
b=int(input('Ingrese el valor de b: '))
c=int(input('Ingrese el valor de c: '))

x1=(-b+(b**2-4*a*c)**(1/2))/(2*a)
x2=(-b-(b**2-4*a*c)**(1/2))/(2*a)

print(x1)
print(x2)

print("Se ha calculado con exito")



