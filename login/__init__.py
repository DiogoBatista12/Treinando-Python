def login(usuarios):
    while  True:
        print("BEM VINDO AO LOGIN!!!")

        email = input("Digite seu e-mail: ").lower().strip()
        senha = input("Digite sua senha: ").strip()

        for i in usuarios:
            if(i["email"] == email and i["senha"] == senha):
                print("Usuário encontrado!")
                print(f"Sejá bem-vindo {i['nome']}")
                return i
        else:
            print("Usuário não encontrado!")
            op = input("Deseja tentar novamente ? sim/nao ").lower().strip()
            if(op == "sim"):
                continue
            elif(op == "nao" or op == "não"):
                break
            else:
                print("Digite apenas sim ou nao")
                continue

def verificar_logado(usuario_logado,usuarios):
    if usuario_logado:
        print("Você já está logado!")
        print(f"Esse é o seu usuário: {'nome'} e esse {'email'} é o seu email")
    else:
        return login(usuarios)
