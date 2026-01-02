def nome_da_funcao(parametro):
    "return resultado"

def calculadora(operacao,num1,num2):
    if(operacao == "soma"):
        return num1 + num2
    elif(operacao == "sub"):
        return num1 - num2
    elif(operacao == "mult"):
        return num1 * num2
    elif(operacao == "div"):
        return num1 / num2
    else:
        return "Essa operação não existe"

print(calculadora("soma",12,24))
print(calculadora("mult",12,24))
print(calculadora("div",24,2))
print(calculadora("sub",25,12))

