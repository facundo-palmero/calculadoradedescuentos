precio_original = float(input("ingrese el precio original del producto: "))
categoria = input("ingrese su categoria: ")
if categoria == "oro":
   descuento = precio_original * 0.30
elif categoria == "plata":
   descuento = precio_original * 0.20
elif categoria == "bronce":
   descuento = precio_original * 0.10
else:
   descuento = 0
   print("categoria no valida")
precio_final = precio_original - descuento
print("el precio final con descuento es: ",precio_final)
