""" 01. Em que ano, contando a partir do ano atual, um pé de abacate fica mais alto 
do que um pé de manga? O pé de manga tem 1,50m e cresce 2 centímentros por ano, e o 
pé de abacate tem 1,10m e cresce 3 centímetros por ano. Faça um programa para responder 
essa pergunta, utilizando uma estrutura de repetição.
"""

# Versão com comando “for”
# imprimindo o nome do programa
print("Controle de crescimento de plantas")
# iniciando as variáveis
manga = 1.5
abacate = 1.1
# solicitando ano ao usuário
ano = int(input("Ano atual: "))

for i in range(ano, 100):  # Considerando um limite de 100 anos
    if manga > abacate:
        break
    manga += 0.02   # Crescimento do pé de manga
    abacate += 0.03 # Crescimento do pé de abacate  
    ano += 1
print(f"Em {ano} o pé de manga terá {manga:.2f} e o pé de abacate terá {abacate:.2f}")
