""" 03. Faça um programa que solicite um valor ao usuário e calcule o fatorial desse número."""

 3.  Versão com comando “enquanto”.
 algoritmo “cap06exerc1803a”
 var
 i, numero, fatorial : inteiro
 inicio
 escreval(“Fatorial”)
 escreval(“”)
 escreva(“Fatorial de qual número? “)
 leia(numero)
 se (numero > 1) entao
   i <- numero
   fatorial <- 1
   enquanto (i > 1) faca
      fatorial <- fatorial * i
      i <- i - 1
   fimenquanto
   escreval(numero, “! = “, fatorial)
 senao
   escolha numero
   caso 0
      escreval(numero, “! = 1”)
   caso 1
      escreval(numero, “! = 1”)
   outrocaso
 escreval(“Não há cálculo fatorial para valores negativos.”)
   fimescolha
PRINCÍPIOS DE LÓGICA DE PROGRAMAÇÃO
 33
 f
 imse
 f
 imalgoritmo
 Versão com comando “repita”
 algoritmo “cap06exerc1803b”
 var
 i, numero, fatorial : inteiro
 inicio
 escreval(“Fatorial”)
 escreval(“”)
 escreva(“Fatorial de qual número? “)
 leia(numero)
 se (numero > 1) entao
   i <- numero
   fatorial <- 1
   repita
      fatorial <- fatorial * i
      i <- i - 1
   ate (i = 1)
   escreval(numero, “! = “, fatorial)
 senao
   escolha numero
   caso 0
      escreval(numero, “! = 1”)
   caso 1
      escreval(numero, “! = 1”)
   outrocaso
 escreval(“Não há cálculo fatorial para valores negativos.”)
   fimescolha
 f
 imse
 f
 imalgoritmo
 Versão com comando “para”
 algoritmo “cap06exerc1803c”
 var
 i, numero, fatorial : inteiro
 inicio
 escreval(“Fatorial”)
 escreval(“”)
 escreva(“Fatorial de qual número? “)
 leia(numero)
 se (numero > 1) entao
34
 RESPOSTAS DOS EXERCÍCIOS
   fatorial <- 1
   para i de numero ate 2 passo -1 faca
      fatorial <- fatorial * i
      i <- i - 1
   fimpara
   escreval(numero, “! = “, fatorial)
 senao
   escolha numero
   caso 0
      escreval(numero, “! = 1”)
   caso 1
      escreval(numero, “! = 1”)
   outrocaso
 escreval(“Não há cálculo fatorial para valores negativos.”)
   fimescolha
 f
 imse
 f
 imalgoritmo
