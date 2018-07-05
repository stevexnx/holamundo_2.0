import random
lista = []
ciudades = []
dire = []
contador = 1
contador2 = 1
for a in range(20):
        ciudad = (random.randint(1,20))
        direccion = (random.randint(1,1000000))
        #correo = [direccion,ciudad]
        ciudades.append(ciudad)
        dire.append(direccion)
        #dire.append(ciudades)
        for recorrido in range(1,len(ciudades)):
            for posicion in range(len(ciudades) - recorrido):
                if ciudades[posicion] > ciudades[posicion + 1]:
                    temp = ciudades[posicion]
                    ciudades[posicion] = ciudades[posicion + 1]
                    ciudades[posicion + 1] = temp
                    
            for recorrido in range(1,len(ciudades)):        
                for posicion in range(len(dire) - recorrido):
                    if dire[posicion] > dire[posicion + 1]:
                        temp = dire[posicion]
                        dire[posicion] = dire[posicion + 1]
                        dire[posicion + 1] = temp                                             
for i in range(19):                        
    correo = ciudades[contador],dire[contador]   
    print(correo)
    contador += 1
                       
