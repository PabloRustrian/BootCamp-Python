import math

altura= float(input("Ingresa tu altura en metros: "))
peso= float(input("Ingresa tu peso en kilogramos: "))

# IMC = Indice de masa corporal 
IMC = round(peso/math.pow(altura,2),2)

print("Tu Indice de Masa Corporal es: " + str(IMC))