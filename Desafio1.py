def calc():
    print("[+] Adição")
    print("[-] Subtração")
    print("[/] Divisão")
    print("[*] Multiplicação")

    operacao = str(input("Digite  operador: "))

    if operacao == "+":
        resul = num1 + num2
        print(f"Resultado: {resul}\n")
    elif operacao == "-":
        resul = num1 - num2
        print(f"Resultado: {resul}\n")
    elif operacao == "/":
        resul = num1 / num2
        print(f"Resultado: {resul}\n")
    elif operacao == "*":
        resul = num1 * num2
        print(f"Resultado: {resul}\n")

sair = "x"

while sair == "x":
    num1 = int(input("Digite o numero 1: "))
    num2 = int(input("Digite o numero 2: "))
    calc()

    sair = str(input("Digite X para sair ou Enter para Continuar! "))
    if sair == "X" or sair == 'x':
        sair = ""
        print("Encerrado")
    else:
        sair = "x"
