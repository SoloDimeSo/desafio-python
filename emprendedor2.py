p = int(input("ingrese el precio de subs: "))
u = int(input("ingrese el precio de usuarios: "))
up = int(input("ingrese el precio de usuarios premiun: "))
gt = int(input("ingrese gasto total: "))


preciopremiun =  1.5 * p

up *= preciopremiun

utilidades = p * u + up - gt

print(f" las utilidades del proyecto son {utilidades}")