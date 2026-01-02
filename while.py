
soma = 0
numero = 1
while numero != 0:
    print(soma)
    entrada = input("Digite um número para somar e 0 para parar: ")
    if (entrada == ""):
        print("Você não digitou nada")
        continue
    else:
        numero = int(entrada)
        soma += numero
print(f"Soma total: {soma}")


