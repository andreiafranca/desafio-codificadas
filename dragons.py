# Passo 1: Ler a força inicial (s) e a quantidade de dragões (n)
s, n = map(int, input().split())

dragoes = []

# Passo 2: Ler as características de cada dragão e guardar na lista
for _ in range(n):
    x, y = map(int, input().split())
    dragoes.append((x, y))

# Passo 3: Ordenar a lista. O Python ordena automaticamente pelo primeiro elemento da tupla (a força x)
dragoes.sort()

# Passo 4: Simular as batalhas usando um loop
ganhou_todas = True

for x, y in dragoes:
    if s > x:
        # Se nossa força for maior, vencemos e ganhamos o bônus
        s += y
    else:
        # Se nossa força for menor ou igual, perdemos o jogo
        ganhou_todas = False
        break  # Não precisa continuar se já perdeu uma

# Passo 5: Exibir o resultado final esperado pelo Codeforces
if ganhou_todas:
    print("YES")
else:
    print("NO")
