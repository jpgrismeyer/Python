cadena=",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
cadena2=cadena.lstrip('",:_#')
print(cadena2)

frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(3,"Naranja")
print(frutas)

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados=marcas_tv.isdisjoint(marcas_smartphones)
if conjuntos_aislados== True:
    print("Son aislados")
else:
    print("no son aislados")