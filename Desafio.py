clientes = []
contas = []

def deposito(saldo, valor_deposito, extrato,/):
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
    else:
        print("Valor inválido, por favor digite um valor positivo !")
    
    return saldo, extrato

def saque(*, saldo, valor_saque, extrato, LIMITE_SAQUES, numero_saques):
    if valor_saque <= 500 and numero_saques < LIMITE_SAQUES and valor_saque <= saldo:
        saldo -= valor_saque
        numero_saques += 1
        print(f"Você realizou o saque de R${valor_saque} e seu saldo atual é de R${saldo}")
        extrato += f"Saque: R$ {valor_saque:.2f}\n"
    elif numero_saques >= LIMITE_SAQUES:
        print("Você excedeu o limite de saques diário ! Volte amanhã")
    elif valor_saque > 500:
        print("O limite do valor sacável é de R$ 500, tente sacar um valor inferior")
    elif valor_saque > saldo:
        print("Você não possui saldo suficiente para realizar esta operação !")
    
    return saldo, extrato, numero_saques

def gerarextrato():
    if extrato == "":
            print("Não foram realizadas movimentações !")
    else:
            print(extrato)

def filtrar(cpf, clientes):
    usuario_filtrado = [usuario for usuario in clientes if usuario["cpf"] == cpf]
    return usuario_filtrado[0] if usuario_filtrado else None


def novocliente(nome, data_nascimento, cpf, endereco):
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            print("CPF já está sendo utilizado por outro cliente.")
            return None
    
    # Separando o endereço
    endereco_parts = endereco.split(',')
    if len(endereco_parts) != 3:
        print("Formato do endereço inválido.")
        return None

    logradouro, bairro, cidade_estado = endereco_parts
    endereco_formatado = f"{logradouro.strip()} - {bairro.strip()} - {cidade_estado.strip()}"

    cliente = {"nome_cliente": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco_formatado}
    clientes.append(cliente)
    return cliente
def novaconta(agencia, numero_conta, clientes):
    cpf = input("Digite o cpf do cliente: ")
    cliente = filtrar(cpf, clientes)

    if cliente:
        print("Conta criada com sucesso !")
        return {'agencia': agencia, 'numero_conta': numero_conta, 'cliente': cliente}
    print("Usuário não encontrado")

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[c] Cadastrar Cliente
[nc] Nova Conta
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
AGENCIA = '0001'



while True:

    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("Digite o valor a ser depositado: "))
        saldo, extrato = deposito(saldo, valor_deposito, extrato)

    elif opcao == "s":
        valor_saque = float(input("Digite o valor a ser sacado: "))
        saldo, extrato, numero_saques = saque(saldo=saldo, valor_saque=valor_saque, extrato=extrato, LIMITE_SAQUES=LIMITE_SAQUES, numero_saques=numero_saques)


    elif opcao == "e":
        gerarextrato()

    elif opcao == "c":
        nome = input("Digite o nome do cliente: ")
        data = input("Digite a data de nascimento do cliente: ")
        cpf = input("Digite o cpf do cliente: ")
        endereco = input("Digite o endereço do cliente: ")
        novocliente(nome, data, cpf, endereco)
    
    elif opcao == "nc":
        numero = len(contas) + 1
        conta = novaconta(AGENCIA, numero, clientes)

        if conta:
            contas.append(conta)
    
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")