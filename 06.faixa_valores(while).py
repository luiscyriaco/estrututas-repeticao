""" 06. Faça um programa que leia uma quantidade desconhecida de números e conte quantos 
deles estão nos seguintes intervalos: [0-25.9],[26-50.9], [51-75.9] e [76 - 100]. A entrada 
de dados deve terminar quando for lido um número negativo.
"""
# imprimindo nome do programa
print('\n_____________Faixa de valores_____________\n')
print('-' * 40)
# imprimindo descrição do programa
print('cntA contabiliza os valores entre 0 e 25.9')
print('cntB contabiliza os valores entre 26 e 50.9')
print('cntC contabiliza os valores entre 51 e 75.9')
print('cntD contabiliza os valores entre 76 e 100')
print('-' * 40)
# inicializando variáveis
numero = 0.0
cntA = 0
cntB = 0
cntC = 0
cntD = 0
# loop para ler os números e contar os intervalos
while numero >= 0:
   numero = float(input('Informe um valor entre 0.0 e 100.0: '))
   
   if numero != -1:
      if numero >= 0 and numero <= 25.9:
         cntA += 1
      elif numero >= 26 and numero <= 50.9:
         cntB += 1
      elif numero >= 51 and numero <= 75.9:
         cntC += 1
      elif numero >= 76 and numero <= 100:
         cntD += 1

# imprimindo os resultados acumulados
print('-' * 40)
print('Resultados acumulados')
print('-' * 40)
print(f'[ 0 -  25.9], "{cntA}", valores informados.')
print(f'[26 -  50.9], "{cntB}", valores informados.')
print(f'[51 -  75.9], "{cntC}", valores informados.')
print(f'[76 - 100.0], "{cntD}", valores informados.')
print('-' * 40)
