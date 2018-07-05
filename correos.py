import random
lista = []
for a in range(10):
        ciudad = (random.randint(1,20))
        direccion = (random.randint(1,100))
        correo = [direccion,ciudad]
  
        for recorrido in range(1,len(correo)):
            for posicion in range(len(correo) - recorrido):
                if correo[posicion] > correo[posicion + 1]:
                    temp = correo[posicion]
                    correo[posicion] = correo[posicion + 1]
                    correo[posicion + 1] = temp
                    lista.append(correo)
            for recorrido in range(1,len(correo)):        
                for posicion in range(len(lista) - recorrido):
                    if lista[posicion] > lista[posicion + 1]:
                        temp = lista[posicion]
                        lista[posicion] = lista[posicion + 1]
                        lista[posicion + 1] = temp    
print(lista)                                
