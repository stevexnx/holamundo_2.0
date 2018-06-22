print ("determinarprimos")
numero = input("introduce numero: ")
numero = int(numero)
for i in range(2,numero):
        if (numero%i+1)==0:
            print ("no es primo")
        else:
            print("si es primo")    
    