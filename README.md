# Desafio Codeforces — Mentoria Codificadas | Além do Código

 
## Sobre este repositório

 
Este repositório contém minha resolução para o desafio de programação proposto na mentoria, utilizando problemas da plataforma [Codeforces](https://codeforces.com/) com auxílio de Inteligência Artificial.

 
---

 
## Problemas escolhidos

 
| # | Nome do problema | Link | Dificuldade |
|---|-----------------|------|-------------|
| 1 | 4A - Watermelon | [Ver no Codeforces](https://codeforces.com/contest/4/my) | 800 |
| 2 | 230A - Dragons | [Ver no Codeforces](https://codeforces.com/contest/230/my) | 1000 |


---

 
### Problema 1 — [4A - Watermelon]

 
### O que o problema pede?
< 4A - Watermelon do Codeforces consiste em verificar se o peso \(w\) é um número par maior que 2. -->

 
### Como eu resolvi?
< Pede ajuda a IA para me explicar o que pedi e o contexto geral para entender o que fazer e entender o que se pede. -->

 
### Código
```python
# w = int(input())

if w > 2 and w % 2 == 0:
    print("YES")
else:
    print("NO")


```
---

 
### Problema 2 — [230A Dragons]

 
### O que o problema pede?
< Um jogo de Rpg , a finalidade e derrotar todos os inimigos sem morrer , mas para isso preciso ir derrotando o mais fraco e ganhar força para ir prosseguindo ate derrotar todos.>

 
### Como eu resolvi?
< 1 - Passo = Analisar as regras do jogo.>

< 2 - Passo = Objetivo é derrotar todos os inimigos e a cada Vitoria aumentar o poder.>


### Código
```python
s, n = map(int, input().split())

dragoes = []
for _ in range(n):
    x, y = map(int, input().split())
    dragoes.append((x, y))

dragoes.sort()

venceu = True
for x, y in dragoes:
    if s > x:
        s += y
    else:
        venceu = False
        break

if venceu:
    print("YES")
else:
    print("NO")


```
 ---

 
## IA utilizada


**Qual IA você usou?**
< ChatGPT, Google IA >

 
**Como a IA te ajudou?**


Como Sou leiga e estou em processo de apreendizado desta linguagem pede ajuda pra me explicar quais os codigo usar e qual a função de cada  , motivo para usar e como utilizar , resumindo ela esta me ensinando.

 
---

 
## Reflexão

 
### Dificuldades encontradas


< -- To com muita dificuldade ainda ,não é simplesmente diritar e entender o motivo ração e logica para tais comandos, meu problemas maior ainda esta sendo este , transformar algo em comandos e texto em numero e inseri-los .-->

 
### O que aprendi
<--  Olha aprende a destrinchar o texto e aprestar atenção no que pede e não perder tempo em textos grande , ainda estou com muita dificuldade em gravar esses comandos , estou buscando fazer exercicios para melhor entender . -->
 
 
### Como foi a experiência?
<-- Gostei bastante mas deveria ter umas atividades menos complexa, sei que o proposito é a competição em si , mas estou bem no inicio do meu curso e tive que forçar muito o aprendizado , ainda existe lacumas para que eu preencha , tentarei melhor este ano a competição para mim sera de aprendizado , ano que vem se deus quiser entrarei de cabeça , gostaria de agradecer os professores que tiraram o tempo deles para ensinar todas nós ate por que no meu caso , estou graduando em 2 cursos e tive que forçar muito o simples , ainda existe muitas duvidas , fico grata a todos que fizeram este material maravilhoso , prometo que farei o meu melhor na competição e desejo sorte a todas.-->

