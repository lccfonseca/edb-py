nome = input("Informe o seu nome: ")

altura = float(input("Informe a sua altura (m): "))
peso = float(input("Informe o seu peso (kg): "))

imc = peso / altura ** 2

print("O seu IMC é:", imc)

if (imc > 30):
    print("Você está obeso!")
elif (imc > 25):
    print("Acima do peso")
else:
    print("Peso normal")