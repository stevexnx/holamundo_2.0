print("numeros primos")
numero = input("introducir numero: ")
numero = int(numero)
x = numero - 1
if x % 2 == 0 and numero % 2 == 1:
        print("es primo")
else:
    print("no es primo")  

