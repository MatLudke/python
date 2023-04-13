pares = []
impares = []

for i in range(1, 16):
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print(f"Pares: {len(pares)}")
print(f"Ímpares: {len(impares)}")
