# Desafio Full Stack - 2021
### [Gabriel Gineste](https://github.com/GabrielGineste)

[![Python](https://www.python.org/static/favicon.ico)](https://www.python.org/)
[![Reactjs](https://pt-br.reactjs.org/favicon.ico)](https://pt-br.reactjs.org/)

Respostas para desafios de programação para a vaga de programador Junior.
- Para rodar.

## Questão 1
>Dado um array de números inteiros, retorne os ,índices dos dois números de forma que eles se somem a um alvo específico, Você pode assumir que cada entrada teria exatamente uma solução, e você não pode usar omesmo elemento duas vezes.

 - Minha solução foi uma versão modificada de um exercício parecido que fiz no livro "The Self‑Taught Programmer"
 

## Questão 2
> Um bracket é considerado qualquer um dos seguintes caracteres: (,), {,}, [ ou]. Dois brackets são considerados um par combinado se o bracket de abertura (isto é, (, [ou {) ocorre à esquerda de um bracket de fechamento (ou seja,),] ou} do mesmo tipo exato.Existem três tipos de pares de brackets: [],{}e(). Um par de brackets correspondente não é balanceado se o de abertura e o de fechamento não corresponderem entre si. Por exemplo, {[(])} não é balanceado por que o conteúdo entre {e}não é balanceado.O primeiro bracket inclui o de abertura, (,e o segundo inclui um bracket de fechamento desbalanceado,]. Dado sequencias de caracteres, determine se cada sequência de brackets é balanceada. Se uma string estiver balanceada, retorne SIM. Caso contrário, retorne NAO.

- O programa coloca o que recebe em uma "pilha" e vai analizar o próximo objeto, se for o que fecha aquele par ele remove o mesmo da pilha e vai para o próximo, e muda o status da resposta baseado em se tem ou não elementos restantes na pilha ao final da execução.

- Mude o código da variavel "checar" para testar outros resultados.

## Questão 3
> Digamos que você tenha um array para o qual o elemento i é o preço de uma determinada ação no dia i. Se você tivesse permissão para concluir no máximo uma transação (ou seja, comprar uma e vender uma ação),crie um algoritmo para encontrar o lucro máximo. Note que você não pode vender uma ação antes de comprar.

- O código anda pelo array e calcula o menor lucro e compara com o lucro atual calculado, apos passar pelo array apenas uma vez, ele retorna a maior diferenca encontrada.

## Questão 4
> Dados n inteiros não negativos representando um mapa de elevação onde a largura de cada barra é 1, calcule quanta água é capaz de reter após a chuva.

- Foi um problema realmente completo pra mim, passei algumas boas horas estudando ele na internet até não só ver a solução, mas ter conseguido entender ela. As fontes que me fizeram conseguir entender o aproach do problema foram https://www.youtube.com/watch?v=HmBbcDiJapY e também esse site : https://www.geeksforgeeks.org/trapping-rain-water/

- Por isso não vou postar aqui uma solução, já que absolutamente nada, nem uma ideia de como ter começado esse problema, veio de mim.