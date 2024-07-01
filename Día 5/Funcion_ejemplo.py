precios_cafe=[("Capuchino",1.5),("Expresso",1.2),("Moka",1.9)]

def cafe_mas_caro(lista_precios):
    precio_mayor=0
    cafe_mas_caro=""
    for nombre,precio in lista_precios:
        if precio>precio_mayor:
            precio_mayor=precio
            cafe_mas_caro=nombre
        else:
            pass
    return (cafe_mas_caro,precio_mayor)
print(cafe_mas_caro(precios_cafe))