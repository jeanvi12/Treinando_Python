# ==========================================
#  Treinando os loops(for/while) e iteração em
#  sequências (listas e tuplas)
# ==========================================


# ==========================================
#  Desafio 1 — Relatório de vendas do posto
# ==========================================
# Você tem uma lista com os valores das vendas de cada dia da semana.
# Usando for, faça o seguinte:
#
#   1- Mostre cada dia com sua venda no formato: Seg: R$1250.00
#   2- Calcule e mostre o total de vendas da semana
#   3- Encontre o dia com a maior venda e mostre: Melhor dia: Sáb com R$2500.00
#   4- Mostre quantos dias tiveram vendas acima de R$1500.00
#
# Dica: Use zip() para percorrer as duas sequências ao mesmo tempo.
#       Se não conhece ainda, pesquise ou me pergunte — é bem útil!
print(f"\n{'-'*20}Desafio 1 — Relatório de vendas do posto{'-'*20}\n")

dias = ("Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom")
vendas = [1250.00, 980.50, 1540.75, 1100.00, 2010.30, 2500.00, 1890.45]
contador_dias_acima_1500 = 0

for dia, venda in zip(dias, vendas):
    dia_formatado = f"{dia}: R${venda:.2f}"
    print(dia_formatado)

    if venda > 1500.00:
        contador_dias_acima_1500 += 1

total_vendas = sum(vendas)
print(f"\n ---> O Total de vendas da semana é: R${total_vendas:.2f}\n")

maior_venda = max(vendas)
print(
    f" ---> O dia com a maior venda foi: {dias[vendas.index(maior_venda)]} com R${maior_venda:.2f}\n")

print(
    f" ---> Os dias que tiveram vendas acima de R$1500.00 foram: {contador_dias_acima_1500}\n")

print(f"{'-'*30}FIM DO PRIMEIRO DESAFIO{'-'*30}\n")


# ==========================================
#  Desafio 2 — Validador de senhas
# ==========================================
# Você recebeu uma lista de senhas que os clientes tentaram cadastrar:
#   senhas = ["abc", "Senh@Forte123", "12345678", "MinhaSenha", "P@ss1", "Prog#2024ok"]
#
# Para cada senha, usando for, verifique e mostre:
#   1- Se tem pelo menos 8 caracteres
#   2- Se contém pelo menos um número (itere sobre os caracteres da senha com outro for)
#   3- Se contém pelo menos um caractere especial (@, #, !, $, %)
#   4- No final, classifique cada senha como "APROVADA" (passou nas 3 condições)
#      ou "REPROVADA" (falhou em alguma)
#
# Exemplo de saída esperada:
#   "abc" -> REPROVADA (menos de 8 caracteres, sem número, sem especial)
#   "Senh@Forte123" -> APROVADA
#
# Dica: Aqui você vai usar for dentro de for (loops aninhados) — um pra
#       percorrer a lista de senhas e outro pra percorrer cada caractere.

print(f"\n{'-'*20}Desafio 2 — Validador de senhas{'-'*20}\n")

senhas = ["abc", "Senh@Forte123", "12345678",
          "MinhaSenha", "P@ss1", "Prog#2024ok"]


for senha in senhas:
    
    tem_oito_caracteres = False
    tem_numero = False
    tem_caractere_especial = False
    
    if len(senha) >= 8:
        tem_oito_caracteres = True

    for caractere in senha:
        if caractere.isdigit():
            tem_numero = True
        if caractere in "@#$%!":
            tem_caractere_especial = True

    if tem_oito_caracteres and tem_numero and tem_caractere_especial:
        print(f"{senha} -> APROVADA")
    else:
        motivos_reprovacao = []
        if not tem_oito_caracteres:
            motivos_reprovacao.append("menos de 8 caracteres")
        if not tem_numero:
            motivos_reprovacao.append("sem número")
        if not tem_caractere_especial:
            motivos_reprovacao.append("sem caractere especial")
        print(f" '{senha}' -> REPROVADA ({', '.join(motivos_reprovacao)})")


# DESAFIOS DO CURSO DE PYTHON PARA INICIANTES - SEQUÊNCIAS E LOOPS

# Desafio 1) Dado uma sequência de números, calcule a soma e média dos números
# (Sem usar sum() ou len())
print(f"\n{'='*20}DESAFIOS DO CURSO DE PYTHON PARA INICIANTES - SEQUÊNCIAS E LOOPS{'='*20}")
print("Desafio 1)\n")

sequencia_numeros = [10, 20, 30, 40, 50]
soma = 0
quantidade_numeros = 0

for numero in sequencia_numeros:
    soma += numero
    quantidade_numeros += 1

media = soma / quantidade_numeros
print(f"Soma dos números: {soma}")
print(f"A média dos números é: {media}")
print(f"\n{'-'*30}FIM DO DESAFIO 1{'-'*30}\n")



# Desafio 2) Dado uma sequência de números, encontre o maior e o menor número
# (Sem usar max() ou min())
print("Desafio 2)\n")

sequencia_numeros2 = [15, 8, 22, 5, 30, 12]
numero_maior = sequencia_numeros2[0]
numero_menor = sequencia_numeros2[0]
for num in sequencia_numeros2:
    if num > numero_maior:
        numero_maior = num
    elif num < numero_menor:
        numero_menor = num
print(f"O maior número é: {numero_maior}")
print(f"O menor número é: {numero_menor}")
print(f"\n{'-'*30}FIM DO DESAFIO 2{'-'*30}\n")



# Desafio 3) Dado uma lista de palavras, printe todas as palavras com pelo menos 5 caracteres
print("Desafio 3)\n")

sequencia_palavras = ["Python", "Java", "C++", "JavaScript", "Ruby", "Go"]
for caracteres in sequencia_palavras:
    if len(caracteres) >= 5:
        print(caracteres)
print(f"\n{'-'*30}FIM DO DESAFIO 3{'-'*30}\n")



# Desafio 4) Dado duas listas, printe uma mensagem dizendo se existem
# elementos comuns entre elas ou não
print("Desafio 4)\n")
lista1 = [1, 2, 3, 4, 5]
lista2 = [5, 6, 7, 8, 9]
comuns = []

for item in lista1:
    if item in lista2:
        comuns.append(item)

if comuns:
    print(
        f"Existem elementos comuns entre as listas.\nOs elementos comuns são:{comuns}")
else:
    print("Não existem elementos comuns entre as listas.\n")
print(f"\n{'-'*30}FIM DO DESAFIO 4{'-'*30}\n")
