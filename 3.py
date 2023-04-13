ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

idade = ano_atual - ano_nascimento

print("Sua idade é:", idade)

if idade >= 18:
    print("Você pode votar.")
else:
    print("Você não pode votar.")
