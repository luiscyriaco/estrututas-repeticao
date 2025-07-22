""" 04. Faça um programa que, dada a sequência de Fibonacci(1,1,2,3,5,8,13...n), 
solicite um número inteiro ao usuário e mostre todos os valores da sequência da 
posição 1 até a posição informada pelo usuário. Por exemplo, se o usuário digitou 
o número 10, deverão ser gerados 10 números. Lembre-se de que existem limitações 
para armazenar valores em uma linguagem de programação.
"""

# Versão com comando "for"

# Imprime o nome do programa
print("Fibonacci\n")

# Solicita a quantidade de números da sequência ao usuário
quantidade = int(input("Quantos números da sequência de Fibonacci? "))

# Verifica a quantidade de números
if quantidade > 2:
    anterior = 1
    atual = 1    
    # Imprime os dois primeiros termos sem quebrar a linha
    print(f"{anterior}, {atual}", end="") 
  
    for i in range(3, quantidade + 1):
        proximo = anterior + atual
        anterior = atual
        atual = proximo
        print(f", {atual}", end="")
    print()
else:
    if quantidade == 2:
        print("1, 1")
    elif quantidade == 1:
        print("1")
    else:
        print("Valor informado é inválido para este exercício.")
