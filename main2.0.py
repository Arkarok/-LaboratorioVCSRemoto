import math

print("Calcular una potencia de un numero b y una raiz de un numero d")

b=int(input("Digita un numero, Por favor: "))
d=int(input("Digita un numero, Por favor: "))

potencia=pow(b,2)
print("La potencia es " + str(potencia))

raiz=math.sqrt(d)
print("La raiz es " + str(raiz))

print("Se ha calculado con exito")