from datetime import datetime
from os import system
from time import sleep


cores = {red := "\033[31m", green := "\033[32m", yellow := "\033[33m", blue := "\033[34m", purple := "\033[35m", cyano := "\033[1;36m", endcor := "\033[m"}

dia = datetime.today().day
mes = datetime.today().month


def menu():

    while True:
        print(cyano+"-"*25, f"\n{'MENU':^25}")
        print("-"*25)
        menu = input("""[ D ]\tDepósito
[ S ]\tSaque
[ E ]\tExtrato
[ C ]\tCriar usuário
[ N ]\tCriar conta
[ L ]\tListar contas
[ F ]\tSair\n➥ """).lower().split()[0]
    
        if menu != "d" and menu != "s" and menu != "e" and menu != "f" and menu != "c" and menu != "n" and menu != "l":
            print(red + "ERROR: Opção inválida" + endcor)
            sleep(2)
            system("cls")
            continue
        else:
            return menu


def deposito(saldo, extrato, valor_deposito=float, /):
        
        if valor_deposito < 2:
            print("Operação falhou, valor inferior a R$2,00")
        
        else:
            saldo += valor_deposito
            extrato += f"Deposito R${f'{valor_deposito:.2f}':<10}{dia:>13}/{mes}\n"
            print(green + f"R${valor_deposito:.2f} depositado com sucesso.", endcor)
        
        return saldo, extrato 


def saque(*, saldo, extrato, num_saques=0, valor_saque=float):

    LIMITE_SAQUE_DIARIO = 3
    limite_saque = 500

    if valor_saque > saldo:
        print(red+"Operação falhou, saldo insuficiente", endcor)

    elif valor_saque < 2:
        print(red+ "Operação falhou, valor a baixo do mínimo de R$2,00", endcor)
    
    elif valor_saque > limite_saque:
        print(red+"Operação falhou, valor solicitado excede limite de saque único", endcor)

    elif LIMITE_SAQUE_DIARIO == num_saques:
        print(red+"Operação falhou, limite de saque diário excedido", endcor)
    
    else:
        saldo -= valor_saque
        num_saques += 1
        extrato += f"Saque R${f'{valor_saque:.2f}':<10}{dia:>16}/{mes}\n"
        print(green + f"R${valor_saque:.2f} sacado com sucesso" + endcor)

    return saldo, extrato, num_saques


def func_extrato(saldo, extrato):
        print(yellow+"Não foram realizado movimentações." if not extrato else yellow+f"{'-'*36}\nInformações\t\t\tData\n{'-'*36}\n"+extrato)
        print(green+f"\nSaldo Total: {saldo}")
        print(yellow+"-"*36)


def criar_usuario(users=list):

    dados_user = {"Nome": None, "Nascimento": None, "CPF": None, "Endereço": None}

    
    dados_user["Nome"] = input("Nome: ")
    dados_user["CPF"] = input("CPF: ")
    for c in range(len(users)):
        if users[c] == dados_user["CPF"]:
            return print(yellow+"CPF já cadastrado no sistema")
        else:
            continue

    dados_user["Nascimento"] = {"Dia": "", "Mês": "", "Ano": ""}
    print("Data de nascimento")
    for key, value in dados_user["Nascimento"].items():
        dados_user["Nascimento"][key] = input(f"\t{key}: ")
    
    dados_user["Endereço"] = {"Logradouro": "", "Bairro": "", "Cidade": "", "Estado": ""}
    print("Endereço")
    for key, value in dados_user["Endereço"].items():
        dados_user["Endereço"][key] = input(f"\t{key}: ")
    
    while True:
        if len(dados_user["CPF"]) != 11 or dados_user["CPF"].isnumeric() == False:
            system("cls")
            print(red+"ERROR: CPF inválido", endcor)
            sleep(2)
            dados_user["CPF"] = str(input("CPF: "))
        else:
            break 
    users.append(dados_user)
    
    return users 


def criar_conta(CPF, list_users=list):
    for c in range(len(list_users)):
        if list_users[c]["CPF"] == CPF:
            print(green+"Conta criada com sucesso.")
            return list_users[c]["Nome"]
        else:
            continue

    return print(yellow+"CPF não encontrado, volte ao menu e crie um usuario."), sleep(2)


def listar_users(contas):
    print("-"*36)
    for c in range(len(contas)):
        for key, value in contas[c].items():
            print(f"{key:<15}{value:>17}")
            if key == "Agência":
                print("\n")
                continue
    print("-"*36)


def main():
    saldo = 0
    num_saques = 0
    users = list()
    list_contas = list()
    num_conta = 0
    extrato = ""

    while True:
        home = menu()
        if home == "d":
            system("cls")
            Vdeposito = float(input("Valor de depósito: R$"))
            saldo, extrato = deposito(saldo, extrato, Vdeposito)

        elif home == "s":
            system("cls")
            Vsaque = float(input("Valor de saque: R$"))
            saldo, extrato, num_saques = saque(saldo=saldo, extrato=extrato, num_saques=num_saques, valor_saque=Vsaque)

        elif home == "e":
            system("cls")
            func_extrato(saldo, extrato)
            input(yellow+"Presiona enter para voltar.")
            system("cls")

        elif home == "c":
            system("cls")
            print("-"*45, f"\n{'DADOS CADASTRAIS':^45}")
            print("-"*45)
            users = criar_usuario(users)
            print(green+"Usuário criado com sucesso!")
            sleep(2)
            system("cls")
        
        elif home == "n":
            system("cls")
            num_conta += 1 
            cpf = input(green+"Digite seu CPF: ")
            nome = criar_conta(cpf, users)
            conta = {"Usuário": nome, "Número da conta": num_conta, "Agência": "001"}
            list_contas.append(conta)
            sleep(2)
            system("cls")

        elif home == "l":
            system("cls")
            listar_users(list_contas)
            input("Pessione enter para voltar")
            system("cls")

        elif home == "f":
            break

    return print("Volte sempre")


main()
