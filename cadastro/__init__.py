usuarios = []
id = 0
def cadastrar(usuarios):
    global id
    while True:
        print("VAMOS CADASTRAR SEU USUÁRIO!!!")

        nome = input("Digite seu nome: ").strip().lower()
        email = input("Digite seu email: ").strip().lower()
        senha = input("Digite sua senha: ").strip()
        senha2 = input("Confirme sua senha: ").strip()

        if (nome == "" or email == "" or senha == "" or senha2 == ""):
            print("Preencha todos os campos.")
            continue

        while len(nome) < 3 or not nome.isalpha():
            print("O nome deve ter pelo menos 3 caracteres e só pode conter letras!")
            nome = input("Digite seu nome: ").strip().lower()

        while "@" not in email or "." not in email:
            print("Seu email não possui @ ou .")
            email = input("Digite seu email: ").strip().lower()

        while senha != senha2:
            print("Senhas não coincidem")
            senha = input("Digite sua senha: ").strip()
            senha2 = input("Confirme sua senha: ").strip()

        print("USUÁRIO CADASTRADO COM SUCESSO!")

        id += 1
        usuario = {
            "id": id,
            "nome": nome,
            "email": email,
            "senha": senha
        }
        usuarios.append(usuario)

        pergunta = input("Deseja cadastrar mais alguém? ").lower().strip()
        if(pergunta == "sim"):
            continue
        elif(pergunta == "nao" or pergunta == "não"):
            break
        else:
            while pergunta != "sim" and pergunta != "nao" and pergunta != "não":
                print("Digite sim ou não!")
                pergunta = input("Deseja cadastrar mais alguém? ").lower().strip()
            if(pergunta == "sim" or pergunta == "nao" or pergunta == "não"):
                break










