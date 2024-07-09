print("\nCalculadora simples\n")
def calculo():
        num1 = float(input("Digite o primeiro numero: "))
        num2 = float(input("Digite o segundo numero: "))
        operacional = (input("""\nQual operação deseja realizar:\n 1 = soma\n 2 = subtração\n 3 = multiplicação\n 4 = Divisão 
 5 = Divisão inteira\n 6 = Resto da divisão\n 7 = Potenciação\n\n"""))
        for operacao in operacional:
          if operacao == "1":
            print(" \n A soma é:", num1 + num2)
          elif operacao == "2":
            print(" \n A subtração é:", num1 - num2)
          elif operacao == "3":
            print(" \n A multiplicação é:", num1 * num2)
          elif operacao == "4":
            print(" \n A divisão é:", num1 / num2)
          elif operacao == "5":
            print(" \n A divisão inteira é:", int(num1 // num2))
          elif operacao == "6":
            print(" \n O resto da divisão é:", num1 % num2)
          elif operacao == "7":
            print(" \n A potenciação é:", num1 ** num2)
        
        print(f"""\n \n O resultado de algumas operações é\n \n O resultado da soma é: {num1 + num2}
 O resultado da subtração é: {num1 - num2}\n O resultado da multiplicação é: {num1 * num2}
 O resultado da divisão é: {num1 / num2}\n O resultado da divisão inteira é: {int(num1 // num2)}
 O resultado do resto da divisão é: {num1 % num2}\n O resultado da potenciação é {num1 ** num2}\n""")
        print(" Vamos fazer outra operação?\n")
while True:
    calculo()
