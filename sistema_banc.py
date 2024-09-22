import textwrap

def menu():
    menu = """\n
    ===============MENU===============
    [1]novo usuario
    [2]nova conta
    [3]depositar
    [4]sacar
    [5]extrato
    [9]listar usuarios
    [0]sair
    """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo+= valor
        extrato+= f"depósito: R$ {valor:.2f}"
        print("Depósito realizado!")
    else:
        print("erro: valor inválido")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, num_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = num_saques > limite_saques

    if excedeu_saldo:
        print("Erro: Você não possui saldo suficiente.")
    elif excedeu_limite:
        print("Erro: O valor informado excede o limite.")
    elif excedeu_saques:
        print("Erro: Quantidade máxima de saques excedidas.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}"
        num_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("Erro: Valor informado é inválido")

    return saldo, extrato

def exibir_extrato(saldo,/,*,extrato):
    print("==============EXTRATO===============")
    print("Não foram realizadas movimentações" if not extrato else extrato)
    print(f"Saldo: R${saldo:.2f}")
    print("====================================")

def criar_usuario(usuarios):
    cpf = input("Informe seu  CPF (apenas números): ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("Já existe um usuário com este CPF cadastrado.")
        return
    
    nome= input("informe seu nome completo: ")
    data_nasc = input("informe sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("informe seu endereço (logradouro,número, bairro, cidade/uf: )")
    usuarios.append({"nome": nome, "data_nasc":data_nasc,"cpf":cpf,"endereço":endereco})

    print("Usuário criado com sucesso!")

def filtrar_usuarios(cpf, usuarios):
    usuarios_filt = [usuario for usuario in usuarios if usuario ["cpf"]== cpf]
    return usuarios_filt[0] if usuarios_filt else None

def criar_conta (agencia, nr_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuarios(cpf,usuarios)

    if usuario:
        print("Contar criada com sucesso!")
        return{"agencia":agencia, "numero_da_conta":nr_conta, "usuario":usuario}
    print("Usuário não encontrado")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:{conta['agencia']}
            C/C:{conta['numero_da_conta']}
            Titular:{conta['usuario']['nome']}
            """
        
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    limite_saque = 3
    agencia = "0001"

    saldo = 0
    limite = 500
    extrato=""
    num_saques = 0
    usuarios =[]
    contas = []

    while True:
        opcao = menu()
        
        if opcao == "3":
            valor = float(input("informe o valor do depósito: "))

            saldo, extrato = depositar(saldo,valor,extrato)

        elif opcao == ("4"):
            valor = float(input("informe o valor que deseja sacar: "))
            
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato = extrato,
                limite=limite,
                num_saques = num_saques,
                limite_saques = limite_saque,
            )
        
        elif opcao==("5"):
            exibir_extrato(saldo,extrato=extrato)

        elif opcao== ("1"):
            criar_usuario(usuarios)
        
        elif opcao==("2"):
            numero_conta = len(contas) + 1
            conta = criar_conta(agencia, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao== ("9"):
            listar_contas(contas)
        
        elif  opcao==("0"):
            break
        else:
            print("Opção inválida, selecione novamente a operação.")
        
main()
