saldo_atual = float(input("Informe o saldo atual: "))
print("Saldo atual de", saldo_atual) 


valor_deposito = float(input("\nInforme o valor a depositar: "))
saldo_atual = float(saldo_atual + valor_deposito)
print("Valor depositado! \nSaldo atual de", saldo_atual)


valor_retirada = float(input("\nInforme o valor a retirar: "))
saldo_atual = float(saldo_atual - valor_retirada)
print("Valor retirado! \nSaldo atual de", saldo_atual)