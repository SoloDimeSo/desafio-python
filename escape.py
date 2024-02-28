import math


radio =int(input("ingrese el radio en kilometros"))
gravedad = float(input("ingrese la constante g"))

radio_m = radio * 1000
ve = math.sqrt(2*gravedad*radio_m)


print(f"la velocidad de escape es {ve} [m/s]")