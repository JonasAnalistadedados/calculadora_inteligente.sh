# Documentação para executar a Calculadora Inteligente
### Para executar a Calculadora Inteligente é preciso ter instalado o Python 3 no seu computador
### Caso você já tenha o Python 3 instalado no seu computador basta executar o arquivo "calculadora.py" para abrir a calculadora
### Caso não tenha o python3 instalado no seu computador você instalar utilizando o arquivo "calculadora.sh" 
### Abra o arquivo calculadora.sh se não iniciar direta a  instalação ou atualização do Python 3 você pode utilizar um terminal linux para executar os comandos do calculadora.sh
### Se não tiver o terminal Linux no seu computador você pode baixar a distribuição Ubuntu pelo Windows PowerShell utilizando como administrador os comandos:
### wsl --list --online
### wsl --install --distribution Ubuntu-22.04
### Agora o Ubuntu já foi instalado basta reiniciar seu computador pesquisar por Ubuntu na pesquisa do seu computador
### Abra o Ubuntu e digite o comando do arquivo calculadora.sh para instalar o Python 3 
### Agora você já consegue executar o arquivo da calculadora.py

# Explicação do código em Python da Calculadora Inteligente.
print("\nCalculadora Inteligente\n") # Titulo que coloquei na minha Calculadora
def calculo(): # Definindo a função Somar
        num1 = float(input("Digite o primeiro numero: ")) # Vai pedir ao usúario o primeiro numero
        num2 = float(input("\nDigite o segundo numero: "))  # Vai pedir ao usúario o segundo numero
        operacional = int(input("""\nQual operação deseja realizar:\n 1 = soma\n 2 = subtração\n 3 = multiplicação\n 4 = Divisão 
 5 = Divisão inteira\n 6 = Resto da divisão\n 7 = Potenciação\n\n""")) # Vai perguntar ao usúario qual operação ele deseja realizar
        if operacional == 1: # Se a opção for 1 executa a soma!
            print(" \n A soma é:", num1 + num2) # Vai mostrar na tela pro usúario a soma!
            print("\nVamos fazer outra operação?\n") # Após o resultado vai aparecer essa pergunta ...
        elif operacional == 2:    # Se a opção for 2 executa a subtração!
            print(" \n A subtração é:", num1 - num2)
            print("\nVamos fazer outra operação?\n") # Após o resultado vai aparecer essa pergunta ...
        elif operacional == 3:
            print(" \n A multiplicação é:", num1 * num2)
            print("\nVamos fazer outra operação?\n") # Após o resultado vai aparecer essa pergunta ...
        elif operacional == 4:
            print(" \n A divisão é:", num1 / num2)
            print("\nVamos fazer outra operação?\n") # Após o resultado vai aparecer essa pergunta ...
        elif operacional == 5:
            print(" \n A divisão inteira é:", int(num1 // num2))
            print("\nVamos fazer outra operação?\n") # Após o resultado vai aparecer essa pergunta ...
        elif operacional == 6:
            print(" \n O resto da divisão é:", num1 % num2)
            print("\nVamos fazer outra operação?\n") # Após o resultado vai aparecer essa pergunta ...
        elif operacional == 7:
            print(" \n A potenciação é:", num1 ** num2)
            print("\nVamos fazer outra operação?\n") # Após o resultado vai aparecer essa pergunta ...
        else:
            print("\nOpção inválida! Operacional incorreto! Tente novamente..\n") # Se o usúario digitar um numero acima de 7 aparece opção inválida..
          
        
while True:  # Vai executar o programa novamente 
    calculo()
    



