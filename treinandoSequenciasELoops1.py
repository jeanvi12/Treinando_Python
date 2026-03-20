# ==========================================
#  Desafio 1 — Gerenciador de lista de compras
# ==========================================
# Crie um programa que comece com uma lista de compras pré-definida com pelo menos 5 itens.
# A partir dela, você deve:
#   1- Mostrar os 3 primeiros itens usando slicing
#   2- Substituir o segundo item por outro (explorando mutabilidade)
#   3- Adicionar 2 itens novos ao final
#   4- Mostrar a lista de trás pra frente usando slicing
#   5- Mostrar a lista final completa
#
# O objetivo aqui é praticar operações básicas com listas
# e entender como o slicing funciona na prática.

print(f"\n{'-'*20}Desafio 1 — Gerenciador de lista de compras{'-'*20}\n")
compras = ['Fones', 'Mochila', 'Caderno', 'Caneta', 'Lápis']

print(f"Os primeiros 3 itens da lista são: {compras[:3]}\n")

compras[1] = 'Camera'
print(f"Lista após substituir o segundo item(mochila por Camera): {compras}\n")

compras.append('Celular')
compras.append('Notebook')
print(f"Lista após adicionar 2 elementos novos ao final: {compras}\n")

print(f"Mostrando a lista de tras para frente: {compras[::-1]}\n")

print(f"Lista final completa: {compras}\n")

print(f"{'-'*30}FIM DO PRIMEIRO DESAFIO{'-'*30}\n")


# ==========================================
#  Desafio 2 — Registro de abastecimentos (tuplas vs listas)
# ==========================================
# Imagine que você está registrando abastecimentos em um posto.
# Cada abastecimento é uma tupla com 3 dados: (data, litros, valor_total).
# Exemplo: ("15/03", 25.5, 142.80).
#
# Tarefas:
#   1- Crie uma lista contendo pelo menos 4 tuplas de abastecimentos
#   2- Mostre apenas os 2 abastecimentos mais recentes (slicing)
#   3- Calcule o total de litros e o total gasto percorrendo a lista com um for
#   4- Tente alterar o valor de litros dentro de uma tupla — observe o erro
#   5- Explique a diferença entre a lista ser mutável e as tuplas serem imutáveis

print(f"\n{'-'*20}Desafio 2 — Registro de abastecimentos (tuplas vs listas){'-'*20}\n")

lista_abastecimentos = [
    ('15/03', 25.5, 142.80),
    ('16/03', 35.5, 198.00),
    ('17/03', 40.0, 220.00),
    ('18/03', 30.0, 165.00)
]
print(f"Lista de abastecimentos: {lista_abastecimentos}\n")

ultimos_dois_abastecimentos = lista_abastecimentos[-2:]
print(f"Os dois ultimos abastecimentos são: {ultimos_dois_abastecimentos}\n")

total_litros = 0
total_gasto = 0
for abastecimento in lista_abastecimentos:
    total_litros += abastecimento[1]
    total_gasto += abastecimento[2]
print(f"Total de litros: {total_litros}\nTotal gasto: R${total_gasto:.2f}\n")

print(f"{'-'*30}FIM DO PRIMEIRO DESAFIO{'-'*30}\n")

# Os valores das Tuplas são imutáveis, por isso não é possível alterar o valor de litros.
# Já a lista é mutável, o que significa que podemos adicionar, remover ou alterar
# os elementos da lista, mas não podemos alterar os valores dentro das tuplas
# que estão na lista.


# ==========================================
#  Desafio 3 — Sistema de ranking de clientes
# ==========================================
# Você tem uma lista de nomes de clientes ordenados por pontos
# (do que tem mais pontos pro que tem menos):
#   clientes = ["Ana", "Carlos", "Bia", "Diego", "Eva", "Fábio", "Gabi", "Hugo"]
#
# A partir dessa lista:
#   1- Mostre o pódio (top 3) usando slicing
#   2- Mostre os clientes na "zona de risco" (os 3 últimos) usando slicing com índices negativos
#   3- Crie uma nova lista só com os clientes de posição par (índice 0, 2, 4...) usando slicing com step
#   4- Um novo cliente "Zara" entrou em 2º lugar — insira ela na posição correta
#   5- O último cliente saiu do programa — remova ele
#   6- Mostre o ranking final e guarde o top 3 em uma tupla
#      (porque o pódio não pode ser alterado depois de definido)

clientes = ["Ana", "Carlos", "Bia", "Diego", "Eva", "Fábio", "Gabi", "Hugo"]
print(f"\n{'-'*20}Desafio 3 — Sistema de ranking de clientes{'-'*20}\n")
print(f"A lista de clientes ordenados por pontos: {clientes}\n")

print(f"O pódio (Top 3) de clientes com mais pontos é: {clientes[:3]}\n")

print(
    f"Os clientes em 'Zona de Risco', ou seja, com menos pontos são: {clientes[-3:]}\n")

clientes_posicoes_pares = (clientes[::2])
print(
    f"Nova lista só com os clientes de posição par (índice 0, 2, 4...): {clientes_posicoes_pares}\n")

clientes.insert(1, 'Zara')
print(
    f"O ranking atualizado, após a entrada de Zara em 2º lugar: {clientes}\n")

removendo_ultimo_cliente = clientes.pop()
print(
    f"O cliente {removendo_ultimo_cliente} saiu do programa.\n Ranking atualizado: {clientes}\n")

ranking_final = tuple(clientes[:3])
print(f"O ranking final (top 3) é: {ranking_final}\n")

print(f"{'-'*30}FIM DO TERCEIRO DESAFIO{'-'*30}\n")
