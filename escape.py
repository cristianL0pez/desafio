import math

radio = int(input("Ingrese el radio en Kilómetros:"))
gravedad = float(input("Ingrese la constante g: "))

radio = radio * 1000
ve = math.sqrt(2*gravedad*radio)



print(f"La velocidad de Escape es {ve:.1f} [m/s]")
