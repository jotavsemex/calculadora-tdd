# Trabalho de Métodos Ágeis - Calculadora de Notas em Python

Esse repositório foi criado para a atividade integradora da matéria de Métodos Ágeis do professor Lucca (FAG). O objetivo principal foi desenvolver uma calculadora de notas usando os conceitos de TDD (escrever os testes antes do código) e aplicar o padrão de commits combinados em aula (Conventional Commits).

## Alunos
* Integrante 1: joao victor santos fernandes
* Integrante 2: welison costa da silva

## O que foi feito no projeto
A gente implementou as funções para calcular a média ponderada das notas de um aluno e validar a situação dele de acordo com os critérios da matéria:
* Média Ponderada: A terceira nota tem peso 2 (`(N1 + N2 + 2*N3) / 4`).
* Situações: Aprovado (nota maior ou igual a 7), Recuperação (entre 4 e 6.9) e Reprovado (abaixo de 4).
* Validação: O sistema não aceita notas menores que 0 ou maiores que 10, disparando um erro (`ValueError`).

## Retrospectiva
Como pedido na atividade, convesanos sobre como foi trabalhar usando TDD e em dupla:

Start: Começar a planejar e rabiscar a lógica das funções juntos antes de ir direto para o código. Isso ajudou a alinhar o que cada teste precisa validar antes de começar a dar erro.
Stop: Parar de tentar adiantar o código de produção sem antes criar o teste que falha. No começo a gente esqueceu e quase começamos a escrever a função direto, o que quebra a regra do TDD.
Continue: Continuamos revezando quem digita o código (piloto) e quem fica dando as ideias e revisando (copiloto). Deixou o trabalho bem mais dinâmico e evitou que a gente cometesse erros Bestas.

## Aviso
Fizemos tudo no meu notebook por que o Welison esta sem.