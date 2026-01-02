from cadastro import *
from login import *
from logout import *
usuario_logado = None
num = 0
while num == 0:

    print("BEM-VINDO PARA O GERENCIAMENTO DE USUÁRIOS")
    print("1 - CADASTRO")
    print("2 - LOGIN")
    print("3 - LOGOUT")
    print("4 - LISTAR")
    print("5 - SAIR")

    operacao = input("Qual opção você deseja ? ").strip()
    if(operacao == ""):
        print("Escolha alguma das opções")
    elif(operacao == "1"):
        cadastrar(usuarios);
    elif (operacao == "2"):
        usuario_logado = (verificar_logado(usuario_logado,usuarios))
    elif (operacao == "3"):
        usuario_logado = logout(usuario_logado)
    elif (operacao == "4"):
        print(usuarios)
    elif (operacao == "5"):
        print("Programa encerrado")
        num += 1
