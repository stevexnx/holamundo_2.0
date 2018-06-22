print("determinar pares")
contador3 = 0
contador = 0
contador1 = 0
veces = int(input("veces: "))
while 1 == 1:
    if veces != int(veces):
        print("fin del programa")
        break
    while contador3 < veces:
        contador3 += 1
        numero = int(input("introducir numero: "))
        if numero % 2 == 0:
            contador += 1
        else:
            contador1 += 1
        print(contador,"son pares")
        print(contador1,"son impares")
        if contador3 == veces:
            print("fin del programa XD")    