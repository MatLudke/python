soma = 0
quantidade_pares = 0

for i in range(2, 101, 2):
    soma += i
    quantidade_pares += 1

print(f"Soma dos pares: {soma}")
print(f"Quantidade de pares encontrados: {quantidade_pares}")
