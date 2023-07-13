from datetime import datetime

menu = """

[d] - Depositar
[s] - Saque
[e] - Extrato
[q] - Sair

=> """


dia = datetime.today().day
mes = datetime.today().month
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

        opcao = input(menu).lower().split()[0]

        if opcao == "d":
            deposito = float(input("Digite o valor de depósito: "))
            if deposito < 1:
                print("Valor inferior a R$1,00")
            else:
                saldo += deposito
                extrato += f"R${deposito:.2f} depositado dia {dia}/{mes}\n"
                print(f"Valor de R${deposito:.2f} depositado com sucesso.")

        elif opcao == "s":
            saque = float(input("Digite o valor que deseja sacar: "))
            if saque > 500:
                 print("Valor solicitado superior ao permitido.")
            elif saldo >= saque and LIMITE_SAQUES > 0:
                saldo -= saque
                print(f"Saque de R${saque} realizado com sucesso.")
                extrato += f"R${saque} sacado dia{dia}/{mes}\n"
                LIMITE_SAQUES -= 1
            else:
                print("Limite de saques diário excedido, volte amanhã.")

        elif opcao == "e":
            print("Extrato\n\n")
            print(extrato)

        elif opcao == "q":
            break

        else:
             print("Operação inválida, por favor selecione novamente a operação desejada.")
