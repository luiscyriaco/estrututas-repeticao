""" 04. Faça um programa que, dada a sequência de Fibonacci(1,1,2,3,5,8,13...n), 
solicite um número inteiro ao usuário e mostre todos os valores da sequência da 
posição 1 até a posição informada pelo usuário. Por exemplo, se o usuário digitou 
o número 10, deverão ser gerados 10 números. Lembre-se de que existem limitações 
para armazenar valores em uma linguagem de programação.
"""

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
elif quantidade == 1:
    print("1")
elif quantidade == 2:
    print("1, 1")
else:
    print("Quantidade inválida. Por favor, digite um número positivo.")
