def deposito():
    global saldo
    global extrato
    valor_deposito = float(input("Digite o valor a ser depositado: "))
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
    else:
        print("Valor inválido, por favor digite um valor positivo !")
def saque():
    valor_saque = float(input("Digite o valor a ser sacado: "))
    if valor_saque <= 500 and numero_saques < LIMITE_SAQUES and valor_saque <= saldo:
            saldo -= valor_saque
            numero_saques += 1
            print(f"Você realizou o saque de R${valor_saque} e seu saldo atual é de {saldo}")
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
    elif numero_saques >= LIMITE_SAQUES:
            print("Você excedeu o limite de saques diário ! Volte amanhã")
    elif valor_saque > 500:
            print("O limite do valor sacável é de R$ 500, tente sacar um valor inferior")
    elif valor_saque > saldo:
            print("Você não possui saldo suficiente para realizar esta operação !")

def gerarextrato():
    if extrato == "":
            print("Não foram realizadas movimentações !")
    else:
            print(extrato)

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3



while True:

    opcao = input(menu)

    if opcao == "d":
        deposito()

    elif opcao == "s":
        saque()

    elif opcao == "e":
        gerarextrato()
    
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")