""" 02. Faça um programa para fazer uma tabuada solicitando:
	- Tabuada de qual número?
	- Começar a tabuada com qual valor?
	- Fazer a tabuada até qual valor?
"""

algoritmo “cap06exerc1802a”
 var
PRINCÍPIOS DE LÓGICA DE PROGRAMAÇÃO
 31
 i, numero, valorInicial, valorFinal : inteiro
 inicio
 escreval(“Tabuada”)
 escreval(“”)
 escreva(“Tabuada de qual número? “)
 leia(numero)
 escreva(“Começar a tabuada com qual valor? “)
 leia(valorInicial)
 escreva(“Fazer a tabuada até qual valor? “)
 leia(valorFinal)
 para i de valorInicial ate valorFinal faca
   escreval(numero:3, “ × “, i:3, “ = “, (numero*i))
 f
 impara
 f
 imalgoritmo
 Versão com comando “enquanto”
 algoritmo “cap06exerc1802b”
 var
 i, numero, valorInicial, valorFinal : inteiro
 inicio
 escreval(“Tabuada”)
 escreval(“”)
 escreva(“Tabuada de qual número? “)
 leia(numero)
 escreva(“Começar a tabuada com qual valor? “)
 leia(valorInicial)
 escreva(“Fazer a tabuada até qual valor? “)
 leia(valorFinal)
 i <- valorInicial
 enquanto (i <= valorFinal) faca
   escreval(numero:3, “ × “, i:3, “ = “, (numero*i))
   i <- i + 1
 f
 imenquanto
 f
 imalgoritmo
 Versão com comando “repita”
 algoritmo “cap06exerc1802c”
 var
 i, numero, valorInicial, valorFinal : inteiro
 inicio
 escreval(“Tabuada”)
 escreval(“”)
 escreva(“Tabuada de qual número? “)
32
 RESPOSTAS DOS EXERCÍCIOS
 leia(numero)
 escreva(“Começar a tabuada com qual valor? “)
 leia(valorInicial)
 escreva(“Fazer a tabuada até qual valor? “)
 leia(valorFinal)
 i <- valorInicial
 repita
   escreval(numero:3, “ × “, i:3, “ = “, (numero*i))
   i <- i + 1
 ate (i > valorFinal
