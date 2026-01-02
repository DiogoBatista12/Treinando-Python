def logout(usuario_logado):
    if usuario_logado is None:
        print("Você precisa estar logado")
        return None
    else:
        print(f"Usuário {usuario_logado['nome']} foi deslogado")
        return None