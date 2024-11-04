import os
import oracledb
import pandas as pd
from colorama import init, Fore, Style
from datetime import datetime
os.system("cls")
init(autoreset=True)

def conectar():
    try:
        conn = oracledb.connect(
            user="rm555010",
            password="290506",
            dsn="oracle.fiap.com.br:1521/ORCL"
        )
        return conn
    except Exception as e:
        print(Fore.RED + f"Erro ao conectar: {e}")
        return None

def menuPrincipal():
    while True:
        print(Fore.LIGHTCYAN_EX + "Qual função de usuário deseja acessar?" + 
    Fore.LIGHTBLUE_EX + """
    1 - Realizar Diagnóstico
    2 - Listar Diagnósticos
    0 - SAIR
        """)
        try:
            opcao_usuario = input()
            match opcao_usuario:
                case "0":
                    quit()
                case "1":
                    os.system("cls")
                    realizarDiagnostico()
                case "2":
                    os.system("cls")
                    menuListar()
                case _:
                    os.system("cls")
                    print("Opção inválida. Tente novamente.")
        except Exception as e:
            os.system("cls")
            print(Fore.RED + f"Ocorreu um erro:{e}")

def menuListar() -> None:
    conn = conectar()
    while True:
        print(Fore.LIGHTCYAN_EX + "Qual função deseja acessar?" +
    Fore.LIGHTBLUE_EX + """
    1 - Listar tudo
    2 - Filtrar
    0 - VOLTAR
        """)
        try:
            opcao_list = input()
            match opcao_list:
                case "1":
                    os.system("cls")
                    listarTudo(conn)
                case "2":
                    os.system("cls")
                    filtrarProblemas(conn)
                case "0":
                    os.system("cls")
                    menuPrincipal()
                case _:
                    os.system("cls")
                    print("Opção inválida. Tente novamente")
        except Exception as e:
            os.system("cls")
            print(f"Ocorreu um erro: {e}")

def filtrarProblemas(conn) -> None:
    while True:
        print(Fore.LIGHTCYAN_EX + "Deseja filtrar por qual tipo de problema?" +
    Fore.LIGHTBLUE_EX + """
    1 - Elétrico
    2 - Hidráulico
    3 - Mecânico    
    0 - VOLTAR
        """)
        try:
            opcao_problema = input()
            cursor = conn.cursor()
            match opcao_problema:
                case "1":
                    cursor.execute("SELECT tipo_problema, problema_veiculo, solucao FROM T_DIAGNOSTICO WHERE tipo_problema = 'Elétrico'")
                case "2":
                    cursor.execute("SELECT tipo_problema, problema_veiculo, solucao FROM T_DIAGNOSTICO WHERE tipo_problema = 'Hidráulico'")
                case "3":
                    cursor.execute("SELECT tipo_problema, problema_veiculo, solucao FROM T_DIAGNOSTICO WHERE tipo_problema = 'Mecânico'")
                case "0":
                    menuListar()
                case _:
                    os.system("cls")
                    print(Fore.LIGHTRED_EX + "Opção inválida. Tente novamente!")
            colunas = [desc[0] for desc in cursor.description]
            dados = cursor.fetchall()
            df = pd.DataFrame(dados, columns=colunas)
            df = df.rename(columns={
        "TIPO_PROBLEMA": "Tipo do Problema",
        "PROBLEMA_VEICULO": "Problema do Veículo",
        "SOLUCAO": "Solução"
        })
            if df.empty:
                print(Fore.YELLOW + "Nenhum registro encontrado.")
            else:
                print(df.to_string(index=False))
                print()
        except Exception as e:
            print(Fore.RED + f"Erro ao listar registros: {e}")
            
def listarTudo(conn) -> None:
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT tipo_problema, problema_veiculo, solucao FROM T_DIAGNOSTICO")
        colunas = [desc[0] for desc in cursor.description]
        dados = cursor.fetchall()
        df = pd.DataFrame(dados, columns=colunas)
        df = df.rename(columns={
    "TIPO_PROBLEMA": "Tipo do Problema",
    "PROBLEMA_VEICULO": "Problema do Veículo",
    "SOLUCAO": "Solução"
    })
        if df.empty:
            print(Fore.YELLOW + "Nenhum registro encontrado.")
        else:
            print(df.to_string(index=False))
            print()
    except Exception as e:
        print(Fore.RED + f"Erro ao listar registros: {e}")
    
def realizarDiagnostico():
    ...

menuPrincipal()