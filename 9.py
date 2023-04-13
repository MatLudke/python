import random

numero_computador = random.randint(1, 10)
numero_usuario = int(input("Digite um número de 1 a 10: "))

if numero_usuario == numero_computador:
    print(
        f"Parabéns! Você acertou! O número escolhido pelo computador foi {numero_computador}.")
else:
    print(
        f"Você errou! O número escolhido pelo computador foi {numero_computador}.")
