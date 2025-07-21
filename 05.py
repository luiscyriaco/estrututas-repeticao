""" 05. Faça um programa que solicite um valor ao usuário e verifique se esse valor é um número primo. Utilize uma estrutura de repetição na solução deste exercício."""

5.  Versão com comando “repita”.
 algoritmo “cap06exerc1805a”
 var
 numero, i : inteiro
 ehPrimo : logico
 inicio
 escreval(“Número Primo”)
 escreval(“”)
PRINCÍPIOS DE LÓGICA DE PROGRAMAÇÃO
 37
 escreva(“Infome um número para análise: “)
 leia(numero)
 se (numero > 1) entao
   ehPrimo <- VERDADEIRO
   i <- numero - 1
   repita
      se (numero%i = 0) entao
         ehPrimo <- FALSO
         interrompa
      fimse
      i <- i - 1
   ate (i = 1)
   se (ehPrimo) entao
      escreval(numero, “ é primo.”)
   senao
      escreval(numero, “ não é primo.”)
   fimse
 senao
   escreval(“Primos devem ser positivos e maiores do que um.”)
 f
 imse
 f
 imalgoritmo
 Versão com comando “enquanto”
 algoritmo “cap06exerc1805b”
 var
 numero, i : inteiro
 ehPrimo : logico
 inicio
 escreval(“Número Primo”)
 escreval(“”)
 escreva(“Infome um número para análise: “)
 leia(numero)
 se (numero > 1) entao
   ehPrimo <- VERDADEIRO
   i <- numero - 1
   enquanto (i > 1) faca
      se (numero%i = 0) entao
         ehPrimo <- FALSO
         interrompa
      fimse
      i <- i - 1
   fimenquanto
38
 RESPOSTAS DOS EXERCÍCIOS
   se (ehPrimo) entao
      escreval(numero, “ é primo.”)
   senao
      escreval(numero, “ não é primo.”)
   fimse
 senao
   escreval(“Primos devem ser positivos e maiores do que um.”)
 f
 imse
 f
 imalgoritmo
 Versão com comando “para”
 algoritmo “cap06exerc1805c”
 var
 numero, i : inteiro
 ehPrimo : logico
 inicio
 escreval(“Número Primo”)
 escreval(“”)
 escreva(“Infome um número para análise: “)
 leia(numero)
 se (numero > 1) entao
   ehPrimo <- VERDADEIRO
   para i de (numero - 1) ate 2 passo -1 faca
      se (numero%i = 0) entao
         ehPrimo <- FALSO
         interrompa
      fimse
   fimpara
   se (ehPrimo) entao
      escreval(numero, “ é primo.”)
   senao
      escreval(numero, “ não é primo.”)
   fimse
 senao
   escreval(“Primos devem ser positivos e maiores do que um.”)
 f
 imse
 f
 imalgoritm
