try:
    nome = input("Digite seu nome: ")
    altura = float(input("Digite sua altura: "))
    peso = float(input("Digite seu peso: "))

    imc = peso / (altura * altura)

    if imc < 18.5:
        print("Abaixo do peso")
    elif imc < 24.9:
        print("Peso normal")
    elif imc < 29.9:
        print("Sobrepeso")
    elif imc < 34.9:
        print("Obesidade Grau I")
    elif imc < 39.9:
        print("Obesidade Grau II")
    else:
        print("Obesidade Grau III (morbida)")

except:
    print("Valor digitado incorreto, Tente novamente")