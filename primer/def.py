def cod (n,m):
    cantidad = str(n)
    numero = str(m)
    contador = 0
    for valor in cantidad:
        if valor == numero:
            contador += 1
    return(contador)

print(cod(1111,1))