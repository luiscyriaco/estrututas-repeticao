""" 04. Faça um programa que, dada a sequência de Fibonacci(1,1,2,3,5,8,13...n), solicite um número inteiro ao usuário e mostre todos os valores da sequência da posição 1 até a posição informada pelo usuário. Por exemplo, se o usuário digitou o número 10, deverão ser gerados 10 números. Lembre-se de que existem limitações para armazenar valores em uma linguagem de programação."""

 Versão com comando “repita”.
 algoritmo “cap06exerc1804a”
 var
 i, quantidade, anterior, atual, proximo : inteiro
 inicio
 escreval(“Fibonacci”)
 escreval(“”)
 escreva(“Quantos números da sequência de Fibonacci? “)
 leia(quantidade)
 se (quantidade > 2) entao
   anterior <- 1
   atual <- 1
   i <- 3
   escreva(anterior, “, “, atual)
   repita
      proximo <- anterior + atual
      anterior <- atual
      atual <- proximo
      escreva(“, “, atual)
      i <- i + 1
   ate (i > quantidade)
PRINCÍPIOS DE LÓGICA DE PROGRAMAÇÃO
 35
 senao
   escolha (quantidade)
   caso 2
      escreval(“1, 1”)
   caso 1
      escreval(“1”)
   outrocaso
 escreval(“Valor informado é inválido para este exercício.”)
   fimescolha
 f
 imse
 f
 imalgoritmo
 Versão com comando “enquanto”
 algoritmo “cap06exerc1804b”
 var
 i, quantidade, anterior, atual, proximo : inteiro
 inicio
 escreval(“Fibonacci”)
 escreval(“”)
 escreva(“Quantos números da sequência de Fibonacci? “)
 leia(quantidade)
 se (quantidade > 2) entao
   anterior <- 1
   atual <- 1
   i <- 3
   escreva(anterior, “, “, atual)
   enquanto (i <= quantidade) faca
      proximo <- anterior + atual
      anterior <- atual
      atual <- proximo
      escreva(“, “, atual)
      i <- i + 1
   fimenquanto
 senao
   escolha (quantidade)
   caso 2
      escreval(“1, 1”)
   caso 1
      escreval(“1”)
   outrocaso
 escreval(“Valor informado é inválido para este exercício.”)
   fimescolha
 f
 imse
 f
 imalgoritmo
36
 RESPOSTAS DOS EXERCÍCIOS
 Versão com comando “para”
 algoritmo “cap06exerc1804c”
 var
 i, quantidade, anterior, atual, proximo : inteiro
 inicio
 escreval(“Fibonacci”)
 escreval(“”)
 escreva(“Quantos números da sequência de Fibonacci? “)
 leia(quantidade)
 se (quantidade > 2) entao
   anterior <- 1
   atual <- 1
   escreva(anterior, “, “, atual)
   para i de 3 ate quantidade faca
      proximo <- anterior + atual
      anterior <- atual
      atual <- proximo
      escreva(“, “, atual)
      i <- i + 1
   fimpara
 senao
   escolha (quantidade)
   caso 2
      escreval(“1, 1”)
   caso 1
      escreval(“1”)
   outrocaso
 escreval(“Valor informado é inválido para este exercício.”)
   fimescolha
 f
 imse
 f
 imalgoritmo
