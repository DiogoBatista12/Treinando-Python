for i in range(1,11):
    print(i)

lista = ["Diogo", "David", "Danilo"];
for i in lista:
    print(i)

num = [1,2,3,4,5]
soma = 0

for n in num:
    soma += n;
print(soma)

for i in range(1,21):
    if (i % 2 == 0):
        print(i)

pergunta = int(input("Qual número você quer ver a tabuada ? "))
for i in range(1,11):
    operacao = i * pergunta
    print(f"{pergunta}x{i} = {operacao}")


nums = [65,2,56,89,3,4,9,7,14]
soma = 0
numeros = []
for i in nums:
    if (i > 10):
        soma +=1
        numeros.append(i)
        print(i)
print(f"são {soma} números maiores que 10, são eles: {numeros} ")


