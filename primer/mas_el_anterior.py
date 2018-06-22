while 1 == 1:
    print("determinar mayores")
    numero1 = input("escriba un numero: ")
    numero2 = input("escriba un numero mayor a "+numero1 + ": ")
    if numero1 < numero2:
        print(numero1," fue el menor y el mayor fue ",numero2 )
        print("programa terminado")
    while numero2 < numero1:     
        print(numero2," no es mayor a ",numero1)
        numero2 = input("intente de nuevo: ")
        if numero2 > numero1:
            print(numero1," fue el menor y el mayor fue ",numero2 )
            print("programa terminado")
        
