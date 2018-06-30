import random as direccion
diccionario = {}
contador = 0
ciudades = ("Santiago","Bonao","La vega","Santo Domigo","San Francisco","La Romana","San Cristóbal","Higuey","Moca","Cotuí","Jarabacoa","Monte Plata","Nagua","Tamboril","Mao","San Pedro de Macorís","Boca chica","Esperanza","Sosúa","Constanza")
for n in range(10):
    valor = direccion.randint(1,100000)
    correo = ciudades[direccion.randint(0,19)],(valor)
    for c in range(1,10):
        diccionario[] = valor
        contador += 1
print(diccionario[2])
#print(ciudades[10])    
     
