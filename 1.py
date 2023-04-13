preco = float(input("Digite o preço do item: "))
forma_pagamento = input(
    "Digite a forma de pagamento (A vista/3x/Mais de 3x): ")

if forma_pagamento == "A vista":
    preco_final = preco * 0.81
elif forma_pagamento == "3x":
    preco_final = preco
else:
    preco_final = preco * 1.12

print("O valor final do item é:", preco_final)
