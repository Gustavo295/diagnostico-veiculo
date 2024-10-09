import os
from datetime import datetime
os.system("cls")

def menuUsuario():
    while True:
        print("""Qual função de usuário deseja acessar?
        1 - Cadastrar
        2 - Efetuar login
        3 - Voltar
        """)
        try:
            opcao_usuario = input()
            match opcao_usuario:
                case "1":
                    os.system("cls")
                    cadastroUsuario()
                case "2":
                    os.system("cls")
                    efetuarLogin()
                case "3":
                    menuPrincipal()
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
        print("""Qual função deseja acessar?
        1 - Adicionar dados
        2 - Informações da minha conta
        3 - Diagnósticos
        4 - Atualizar dados pessoais
        5 - Redefinir senha
        6 - Sair da Conta
        7 - Voltar
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
                    menuDiagnostico()
                case "4":
                    os.system("cls")
                    attDadosPessoais()
                case "5":
                    os.system("cls")
                    redefinirSenha()
                case "6":
                    os.system("cls")
                    sairConta()
                    menuUsuario()
                case "7":
                    menuPrincipal()
                case _:
                    print("Opção inválida. Tente novamente.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

def addDadosPessoais():
    ...
def infoConta():
    ...
def menuDiagnostico():
    ...
def attDadosPessoais():
    ...
def redefinirSenha():
    ...

def menuVeiculo():
    while True:
        print("""Qual função de veículo deseja acessar?
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
                    menuPrincipal()
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

menuPrincipal()