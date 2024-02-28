p = int(input("ingrese el precio de subs: "))
u = int(input("ingrese la cantidad de usuarios: "))
gt = int(input("ingrese gasto total: "))
utilidades_anteriones = int(input("utilidades anteriones: "))




 
utilidades = p * u - gt
razon = utilidades_anteriones/utilidades

print(f"la razon de las utilidades del proyecto son {razon:.2f}")