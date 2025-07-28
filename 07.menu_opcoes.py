""" 07. Faça um menu de opções de um programa com as seguintes regras:
    O usuário deve selecionar as opções de 0, 1, 2 ou 3. Outros valores são inválidos, e a opção deverá ser selecionada novamente.
    - Se a opção selecionada for 0, encerre o programa.
    - Se a opção selecionada for  1, execute a lógica do exercício 3.
    - Se a opção selecionada for  2, execute a lógica do exercício 4.
    - Se a opção selecionada for  3, execute a lógica do exercício 5.
"""
# iniciando varaiável de controle do loop
opcao = -1

# Loop para exibir o menu até que o usuário escolha a opção 0
while opcao != 0:
    print("\n________Menu de Opções________\n")
    print("-" * 30)
    print("0. Encerrar o programa")
    print("1. Calcular o fatorial de um número")
    print("2. Mostrar a sequência de Fibonacci")
    print("3. Verificar se um número é primo")
    print("-" * 30)
    
    # Solicita a opção do usuário dentro do loop
    opcao = int(input("Sua opção: "))
    print("-" * 30)
    # Verifica a opção escolhida pelo usuário
    if opcao == 0:
        print("Encerrando o programa...")
        
    elif opcao == 1:
        # Versão com comando while
        # imprimindo o nome do programa
        print("Fatorial\n")
        # solicitando número ao usuário
        numero = int(input("Fatorial de qual número? "))
        
        # verificando se o número é maior que 1
        if numero > 1:
            i = numero
            fatorial = 1
            while i > 1:
                fatorial *= i
                i -= 1
            print(f"{numero}! = {fatorial}")
        else:
            if numero == 0 or numero == 1:
                print(f"{numero}! = 1")
            else:
                print("Não há cálculo fatorial para valores negativos.")
    
    elif opcao == 2:
        # Versão com comando "while"
        # imprimindo o nome do programa
        print("Fibonacci\n")

        # solicitando a quantidade de números da sequência ao usuário
        quantidade = int(input("Quantos números da sequência de Fibonacci? "))

        # verificando se a quantidade é maior que 2
        if quantidade > 2:
            anterior = 1
            atual = 1
            i = 3
            print(anterior, ",", atual, end="")
            
            while i <= quantidade:
                proximo = anterior + atual
                anterior = atual
                atual = proximo
                print(", ", atual, end="")
                i += 1
            print()
        elif quantidade == 1:
            print("1")
        elif quantidade == 2:
            print("1, 1")
        else:
            print("Quantidade inválida. Por favor, digite um número positivo.")

    elif opcao == 3:
        # versão com comando "for"
        # Imprime o nome do programa
        print("Número Primo\n")
        # Solicita um número ao usuário
        numero = int(input("Informe um número para análise: "))
        
        # Verifica se o número é maior que 1
        if numero > 1:
            eh_primo = True
            # Verifica se o número é divisível por algum número de 2 até o número - 1
            for i in range(2, numero):
                if numero % i == 0:
                    eh_primo = False
                    break
            # Exibe se o número é primo ou não
            if eh_primo:
                print(f"{numero} é primo.")
            else:
                print(f"{numero} não é primo.")
        else:
            print("Primos devem ser positivos e maiores do que um.")
            
    else:
        print("Opção inválida, por favor, selecione uma opção válida.")
        print("Pressione Enter para continuar...")
        input()
