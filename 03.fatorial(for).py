""" 03. Faça um programa que solicite um valor ao usuário e calcule o fatorial desse número."""

# Versão com comando for
# imprimindo o nome do programa
print("Fatorial\n")
# solicitando número ao usuário
numero = int(input("Fatorial de qual número? "))
# verificando se o número é maior que 1
if numero > 1:
    fatorial = 1
    for i in range(numero, 1, -1):
        fatorial *= i
    print(f"{numero}! = {fatorial}")
else:
    if numero == 0 or numero == 1:
        print(f"{numero}! = 1")
    else:
        print("Não há cálculo fatorial para valores negativos.")
