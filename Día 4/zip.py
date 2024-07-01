nombres=["juampa","Liam","noel"]
edades=[28,50,54]
apodos=["goat","Frontman","The chief"]
fusion=list(zip(nombres,edades,apodos))
print(fusion)
for nombre,edad,apodo in fusion:
    print(f"{nombre} tiene {edad} años y le dicen {apodo}")