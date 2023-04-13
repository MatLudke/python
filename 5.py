dias_semana = {1: "Domingo", 2: "Segunda-feira", 3: "Terça-feira", 4: "Quarta-feira",
               5: "Quinta-feira", 6: "Sexta-feira", 7: "Sábado"}

dia = int(input("Digite um número (1-7): "))

if dia in dias_semana:
    print(dias_semana[dia])
else:
    print("Número inválido.")
