import os
from datetime import datetime
os.system("cls")

def menuPrincipal():
    while True:
        print("""Qual função de usuário deseja acessar?
        1 - Cadastrar
        2 - Efetuar login
        0 - SAIR
        """)
        try:
            opcao_usuario = input()
            match opcao_usuario:
                case "0":
                    quit()
                case "1":
                    os.system("cls")
                    cadastroUsuario()
                case "2":
                    os.system("cls")
                    menuLogin()
                case _:
                    os.system("cls")
                    print("Opção inválida. Tente novamente.")
        except Exception as e:
            os.system("cls")
            print(f"Ocorreu um erro:{e}")

def cadastroUsuario():
    ...
def efetuarLogin():
    ...

def menuLogin():
    while True:
        print("""Qual menu deseja acessar?
        1 - Conta
        2 - Veículo
        3 - Diagnóstico
        4 - Sair da Conta
        """)
        try:
            opcao_login = input()
            match opcao_login:
                case "1":
                    os.system("cls")
                    menuConta()
                case "2":
                    os.system("cls")
                    menuVeiculo()
                case "3":
                    os.system("cls")
                    menuDiagnostico()
                case "4":
                    os.system("cls")
                    menuPrincipal()
                case _:
                    print("Opção inválida. Tente novamente.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

def menuConta():
    while True:
        print("""Qual função deseja acessar?
        1 - Adicionar dados
        2 - Informações da minha conta
        3 - Atualizar dados pessoais
        4 - Redefinir senha
        5 - Voltar
        """)
        try:
            opcao_login = input()
            match opcao_login:
                case "1":
                    os.system("cls")
                    addDadosPessoais()
                case "2":
                    os.system("cls")
                    infoConta()
                case "3":
                    os.system("cls")
                    attDadosPessoais()
                case "4":
                    os.system("cls")
                    redefinirSenha()
                case "5":
                    os.system("cls")
                    menuLogin()
                case _:
                    print("Opção inválida. Tente novamente.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
def addDadosPessoais():
    ...
def infoConta():
    ...
def attDadosPessoais():
    ...
def redefinirSenha():
    ...

def menuVeiculo():
    while True:
        print("""Qual função deseja acessar?
        1 - Cadastrar veículo
        2 - Remover veículo
        3 - Informações dos meus veículos
        4 - Voltar
        """)
        try:
            opcao_veiculo = input()
            match opcao_veiculo:
                case "1":
                    os.system("cls")
                    cadastroVeiculo()
                case "2":
                    os.system("cls")
                    removerVeiculo()
                case "3":
                    os.system("cls")
                    infoVeiculos()
                case "4":
                    os.system("cls")
                    menuLogin()
                case _:
                    print("Opção inválida. Tente novamente.")
        except Exception as e:
            os.system("cls")
            print(f"Ocorreu um erro: {e}")

def cadastroVeiculo():
    ...
def removerVeiculo():
    ...
def infoVeiculos():
    ...

def menuDiagnostico():
    while True:
        print("""Qual função deseja acessar?
        1 - Realizar diagnóstico
        2 - Ver histórico
        3 - Voltar
        """)
        opcao_diag = input()
        match opcao_diag:
            case "1":
                os.system("cls")
                realizarDiagnostico()
            case "2":
                os.system("cls")
                historicoDiagnostico()
            case "3":
                os.system("cls")
                menuLogin()
def realizarDiagnostico():
    ...
def historicoDiagnostico():
    ...

menuPrincipal()