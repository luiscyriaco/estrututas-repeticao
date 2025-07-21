""" 06. Faça um programa que leia uma quantidade desconhecida de números e conte quantos deles estão nos seguintes intervalos: [0-25.9],[26-50.9], [51-75.9] e [76 - 100]. A entrada de dados deve terminar quando for lido um número negativo."""

6.  Versão com comando “repita”.
 algoritmo “cap06exerc1806a”
 var
PRINCÍPIOS DE LÓGICA DE PROGRAMAÇÃO
 39
 // cntA contabiliza os valores entre 0 e 25.9
 // cntB contabiliza os valores entre 26 e 50.9
 // cntC contabiliza os valores entre 51 e 75.9
 // cntD contabiliza os valores entre 76 e 100
 numero, cntA, cntB, cntC, cntD: inteiro
 inicio
 escreval(“Faixa de valores”)
 escreval(“”)
 repita
   escreva(“Informe um valor entre 0.0 e 100.0: “)
   leia(numero)
   // Se o valor estiver entre os valores pertimidos
   se (numero <> -1) entao
      se (numero >= 0) e (numero <= 25.9) entao
         cntA <- cntA + 1
      senao
         se (numero >= 26) e (numero <= 50.9) entao
            cntB <- cntB + 1
         senao
            se (numero >= 51) e (numero <= 75.9) entao
               cntC <- cntC + 1
            senao
               se (numero <= 100) entao
                  cntD <- cntD + 1
               fimse
            fimse
         fimse
      fimse
   fimse
 ate (numero < 0)
 limpatela
 escreval(“Resultados acumulados”)
 escreval(“”)
 escreval(“[ 0 -  25.9] “, cntA:3, “ valores informados.”)
 escreval(“[26 -  50.9] “, cntB:3, “ valores informados.”)
 escreval(“[51 -  75.9] “, cntC:3, “ valores informados.”)
 escreval(“[76 - 100.0] “, cntD:3, “ valores informados.”)
 f
 imalgoritmo
 Versão com comando “enquanto”
 algoritmo “cap06exerc1806b”
 var
 // cntA contabiliza os valores entre 0 e 25.9
 // cntB contabiliza os valores entre 26 e 50.9
40
 RESPOSTAS DOS EXERCÍCIOS
 // cntC contabiliza os valores entre 51 e 75.9
 // cntD contabiliza os valores entre 76 e 100
 numero, cntA, cntB, cntC, cntD: inteiro
 inicio
 escreval(“Faixa de valores”)
 escreval(“”)
 enquanto (numero >= 0) faca
   escreva(“Informe um valor entre 0.0 e 100.0: “)
   leia(numero)
   // Se o valor estiver entre os valores pertimidos
   se(numero <> -1) entao
      se (numero >= 0) e (numero <= 25.9) entao
         cntA <- cntA + 1
      senao
         se (numero >= 26) e (numero <= 50.9) entao
            cntB <- cntB + 1
         senao
            se (numero >= 51) e (numero <= 75.9) entao
               cntC <- cntC + 1
            senao
               se (numero <= 100) entao
                  cntD <- cntD + 1
               fimse
            fimse
         fimse
      fimse
   fimse
 f
 imenquanto
 limpatela
 escreval(“Resultados acumulados”)
 escreval(“”)
 escreval(“[ 0 -  25.9] “, cntA:3, “ valores informados.”)
 escreval(“[26 -  50.9] “, cntB:3, “ valores informados.”)
 escreval(“[51 -  75.9] “, cntC:3, “ valores informados.”)
 escreval(“[76 - 100.0] “, cntD:3, “ valores informados.”)
 f
 imalgoritm
