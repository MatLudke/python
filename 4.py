meses = {"janeiro": 1, "fevereiro": 2, "março": 3, "abril": 4, "maio": 5, "junho": 6,
         "julho": 7, "agosto": 8, "setembro": 9, "outubro": 10, "novembro": 11, "dezembro": 12}

mes = input("Digite o nome do mês: ").lower()

if mes in meses:
    print(meses[mes])
else:
    print("Mês inválido.")
