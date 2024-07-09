# Para executar o código da "Calculadora Inteligente" primeiro execute o script "calculadora.sh"
# Ao executar o script "calculadora.sh" será atualizado ou instalado o python 3 
# Logo em seguida vai abrir o programa da Calculadora Inteligente 
# Pronto pode usar!

print("\nCalculadora Inteligente\n") # Titulo que coloquei na minha Calculadora
def calculo(): # Definindo a função Somar
        num1 = float(input("Digite o primeiro numero: ")) # Vai pedir ao usúario o primeiro numero
        num2 = float(input("Digite o segundo numero: "))  # Vai pedir ao usúario o segundo numero
        operacional = int(input("""\nQual operação deseja realizar:\n 1 = soma\n 2 = subtração\n 3 = multiplicação\n 4 = Divisão 
 5 = Divisão inteira\n 6 = Resto da divisão\n 7 = Potenciação\n\n""")) # Vai perguntar ao usúario qual operação ele deseja realizar
        if operacional == 1: # Se a opção for 1 executa a soma!
            print(" \n A soma é:", num1 + num2) # Vai mostrar na tela pro usúario a soma!
        elif operacional == 2:    # Se a opção for 2 executa a subtração!
            print(" \n A subtração é:", num1 - num2)
        elif operacional == 3:
            print(" \n A multiplicação é:", num1 * num2)
        elif operacional == 4:
            print(" \n A divisão é:", num1 / num2)
        elif operacional == 5:
            print(" \n A divisão inteira é:", int(num1 // num2))
        elif operacional == 6:
            print(" \n O resto da divisão é:", num1 % num2)
        elif operacional == 7:
            print(" \n A potenciação é:", num1 ** num2)
        else:
            print(" Opção inválida! Operacional incorreto! Tente novamente..") # Se o usúario digitar um numero acima de 7 aparece opção inválida..
print(" Vamos fazer outra operação?\n") # Após o resultado vai aparecer essa pergunta ...
while True:  # Vai executar o programa novamente 
    calculo()
    
