def potencia(base,exponente):
    return base**exponente

def usd_a_eur(dolar):
    return dolar*.9
dolares=5000
print(usd_a_eur(dolares))

def invertir_palabra(palabra):
    palabra2=""
    for letra in range(len(palabra)-1,-1,-1):

        palabra2+=palabra[letra]
        #print(palabra{letra})
    return palabra2.upper()
palabra="Neuquen"
print(invertir_palabra(palabra))

