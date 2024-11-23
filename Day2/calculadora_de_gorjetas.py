print("Bem vindo a calculadora de gorjetas")
conta = float(input("Qual é o preço total da conta?\nR$ "))
gorjeta = int(input("Quanto de gorjeta você gostaria de dar? 10, 12, ou 15?\n% "))
pessoa = int(input("Quantas pessoas iram dividir a conta?\n"))

porc_gorjeta = gorjeta / 100
gorjeta_total = conta * porc_gorjeta
total_conta = conta + gorjeta_total
conta_por_pessoa = total_conta / pessoa
quantidade_final = round(conta_por_pessoa, 2)

print(f"Qunatidade que cada pessoa deve pagar: R$ {quantidade_final}")
