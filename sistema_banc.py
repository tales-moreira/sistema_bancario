menu = '''
    [1] DEPOSITAR
    [2] SACAR
    [3] EXTRATO
    [0] SAIR

'''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 2


while True:
      
    opcao=input(menu)

    if opcao == "1":
        valor=float(input("insira o valor a do depósito:"))

        if valor > 0:
            saldo += valor
            extrato += f"depósito: R${valor:.2f}\n"
        else: print("O valor informado não pode ser depositado")

    elif opcao == "2":
        valor=float(input("insira o valor a do saque:"))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques > limite_saques

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor >= 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
            print("\n================ EXTRATO ================")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}\n")
            print("==========================================")

    elif opcao == "0":
            break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")