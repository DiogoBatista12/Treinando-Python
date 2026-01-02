from funcoes import *
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
        'login()'
    elif (operacao == "3"):
        'logout()'
    elif (operacao == "4"):
        print(usuarios)
    elif (operacao == "5"):
        print("Programa encerrado")
        num += 1
