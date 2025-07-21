""" 07. Faça um menu de opções de um programa com as seguintes regras:
	O usuário deve selecionar as opções de 0, 1, 2 ou 3. Outros valores são inválidos, e a opção deverá ser selecionada novamente.
	- Se a opção selecionada for 0, encerre o programa.
	- Se a opção selecionada for  1, execute a lógica do exercício 3.
	- Se a opção selecionada for  2, execute a lógica do exercício 4.
	- Se a opção selecionada for  3, execute a lógica do exercício 5.
"""

 var
 opcao, i, numero, fatorial, quantidade, anterior, atual, 
proximo : inteiro
 ehPrimo : logico
PRINCÍPIOS DE LÓGICA DE PROGRAMAÇÃO
 41
 aguarde : caracter
 inicio
 repita
   limpatela
   escreval(“Menu de Opções”)
   escreval(“”)
   escreval(“0. Encerrar o programa”)
   escreval(“1. Calcular o fatorial de um número”)
   escreval(“2. Mostrar a sequência de Fibonacci”)
   escreval(“3. Verificar se um número é primo”)
   escreva(“Sua opção: “)
   leia(opcao)
   escolha (opcao)
   caso 0
      escreval(“”)
      escreva(“Encerrando o programa...”)
   caso 1
      limpatela
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
            escreval(“Não há cálculo fatorial para valores 
negativos.”)
         fimescolha
      fimse
   caso 2
42
 RESPOSTAS DOS EXERCÍCIOS
      limpatela
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
            escreval(“Valor informado é inválido para este 
exercício.”)
         fimescolha
      fimse
   caso 3
      limpatela
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
PRINCÍPIOS DE LÓGICA DE PROGRAMAÇÃO
 43
            i <- i - 1
         fimenquanto
         se (ehPrimo) entao
            escreval(numero, “ é primo.”)
         senao
            escreval(numero, “ não é primo.”)
         fimse
      senao
         escreval(“Primos devem ser positivos e maiores do que 
um.”)
      fimse
   outrocaso
      escreval(“Opção inválida”)
   fimescolha
   escreval(“”)
   escreval(“Tecle <ENTER> para continuar”)
   leia(aguarde)
 ate (opcao = 0)
 f
 imalgoritmo
