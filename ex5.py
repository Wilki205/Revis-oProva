peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura*altura)
print (f"{imc:.2f}")
if imc < 18.5:
    print ("Abaixo do peso!")
elif 18.5 < imc < 24.9:
    print ("Peso ideal, Parabens")
elif 25.0 < imc < 29.9:
    print ("Levemente acima do peso")
elif 30.0 < imc < 34.9:
    print ("obesidade")
elif 35.0 < imc < 39.9:
    print ("obesidade severa")
elif imc > 40.0:
    print("Obsidade morbida")

