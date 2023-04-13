num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
num4 = int(input("Digite o quarto número: "))

maior = max(num1, num2, num3, num4)

if maior == num1 == num2 == num3 == num4:
    print("Os números são iguais.")
else:
    print("O maior número é:", maior)
