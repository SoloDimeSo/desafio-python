
p = int(input("ingrese el precio de subs: "))
u = int(input("ingrese el precio de usuarios: "))
gt = int(input("ingrese gasto total: "))
utilidadesanteriores = int(input("utilidades anteriores: "))

utilidades = p * u - gt
razon = utilidadesanteriores/utilidades 

print(f" las utilidades del proyecto son {utilidades}")