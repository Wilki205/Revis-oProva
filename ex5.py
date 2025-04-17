peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura*altura)
print (f"{imc:.2f}")
if imc < 18.5:
    print ("Abaixo do peso!")
elif imc >18.5 and imc < 24.9:
    print ("Peso ideal, Parabens")
elif imc >25.0 and imc < 29.9:
    print ("Levemente acima do peso")
elif imc >30.0 and imc < 34.9:
    print ("obesidade")
elif imc >35.0 and imc < 39.9:
    print ("obesidade severa")
elif imc > 40.0:
    print("Obsidade morbida")

