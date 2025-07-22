""" 02. Faça um programa para fazer uma tabuada solicitando:
	- Tabuada de qual número?
	- Começar a tabuada com qual valor?
	- Fazer a tabuada até qual valor?
"""

# Versão com comando while

# imprimindo o nome do programa
print("Tabuada\n")
# solicitando número da tabuada ao usuário
numero = int(input("Tabuada de qual número? "))
# solicitando valor inicial da tabuada ao usuário
valorInicial = int(input("Começar a tabuada com qual valor? "))
# solicitando valor final da tabuada ao usuário
valorFinal = int(input("Fazer a tabuada até qual valor? "))
# iniciando variável de controle
i = valorInicial
while i <= valorFinal:
	print(f"{numero:3} × {i:3} = {numero * i}")
	i += 1
