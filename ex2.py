rep = "s"
while rep == "s":
    n = int(input("Digite um numero: "))
    div = n % 2
    if n > 0:
        if n%2==0:
            print ("Par e Positivo")
        else:
            print ("Impar e Positivo")
    else:
        if n%2==0:
         print ("Par e Negativo")
        else:
            print ("Impar e Negativo")
    rep = input("Digite s para continuar!")






