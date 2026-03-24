# Treinando Dicionários e Métodos em Python

#==================================================================
# Desafio 1: Contando Vogais em um Bloco de Texto (curso de Python)
#==================================================================

# Crie um código que conta o número de vogais de um bloco de texto qualquer.
# O código deve desconsiderar letras maiúsculas e minúsculas, elas devem ser contadas igualmente.
# O código deve ser capaz de contar vogais acentuadas (á, é, í, ó, ú) e sem acentos (a, e, i, o, u).
# O resultado deve mostrar o número total de vogais encontradas no texto.
import random
import unicodedata

texto = """De tudo, ao meu amor serei atento
Antes, e com tal zelo, e sempre, e tanto
Que mesmo em face do maior encanto
Dele se encante mais meu pensamento

Quero vivê-lo em cada vão momento
E em seu louvor hei de espalhar meu canto
E rir meu riso e derramar meu pranto
Ao seu pesar ou seu contentamento

E assim, quando mais tarde me procure
Quem sabe a morte, angústia de quem vive
Quem sabe a solidão, fim de quem ama

Eu possa me dizer do amor (que tive)
Que não seja imortal, posto que é chama
Mas que seja infinito enquanto dure"""


def remover_acentos(texto):
    # Decompõe os caracteres acentuados em base + acento
    nfkd = unicodedata.normalize('NFKD', texto)
    # Filtra apenas os caracteres que não são acentos/diacríticos
    return ''.join(c for c in nfkd if not unicodedata.combining(c))


vogais = "aeiou"
texto = texto.lower()
texto_sem_acentos = remover_acentos(texto)

contador = 0
for vogal in vogais:
    contador += texto_sem_acentos.count(vogal)

print(f"\nO número total de vogais encontradas no texto é: {contador}\n")

# ===================================================
# Resolução alternativa e eficaz para a situação (usando dicionários)
# ===================================================
contagem = {}
for v in vogais:
    contagem[v] = texto_sem_acentos.count(v)

print("Contagem de cada vogal:")
for vogal, quantidade in contagem.items():
    print(f"  {vogal}: {quantidade}")

print(f"Total de vogais: {sum(contagem.values())}")

print(f"{'-'*30}FIM DO PRIMEIRO DESAFIO{'-'*30}\n\n")


#==================================================================
# Desafio 2: Jogo dos Estados (curso de Python)
#==================================================================

# Crie um "Jodo dos Estados". Neste Jogo, o jogador precisa responder o nome da capital de um estado brasileiro sorteado aleatoriamente("Qual é a capital do estado X?")
# E checar se o usuário respondeu corretamente.
# Após cada pergunta, o usuário pode escolher parar o jogo ou continuar para a próxima pergunta.
# Quando o usuário decidir parar, o jogo, ou quando todas as perguntas forem respondidas, o cofigo deve mostrar a pontuação final(o número bruto de acertos) e a porcentagem de acertos em relação ao total de perguntas feitas.("Seu número de acertos foi x, o que corresponde a y% de acertos totais.")


estados_capitais = {
    "Acre": "Rio Branco",
    "Alagoas": "Maceió",
    "Amapá": "Macapá",
    "Amazonas": "Manaus",
    "Bahia": "Salvador",
    "Ceará": "Fortaleza",
    "Distrito Federal": "Brasília",
    "Espírito Santo": "Vitória",
    "Goiás": "Goiânia",
    "Maranhão": "São Luís",
    "Mato Grosso": "Cuiabá",
    "Mato Grosso do Sul": "Campo Grande",
    "Minas Gerais": "Belo Horizonte",
    "Pará": "Belém",
    "Paraíba": "João Pessoa",
    "Paraná": "Curitiba",
    "Pernambuco": "Recife",
    "Piauí": "Teresina",
    "Rio de Janeiro": "Rio de Janeiro",
    "Rio Grande do Norte": "Natal",
    "Rio Grande do Sul": "Porto Alegre",
    "Rondônia": "Porto Velho",
    "Roraima": "Boa Vista",
    "Santa Catarina": "Florianópolis",
    "São Paulo": "São Paulo",
    "Sergipe": "Aracaju",
    "Tocantins": "Palmas"
}
continuar_ou_parar = 's'
perguntas_feitas = 0
acertos = 0

while continuar_ou_parar.lower() != 'n' and len(estados_capitais) >0:
    perguntas_feitas += 1
    chave_sorteada = random.choice(list(estados_capitais.keys())) #sorteia um estado

    capital_original = estados_capitais[chave_sorteada] #guarda o nome original da capital (com acento e maiúscula) para mostrar depois
    
    capital_correta = remover_acentos(
        capital_original.lower().strip()) #pega o valorr da capital do estado sorteado, remove acentos, deixa tudo minusculo e tira espaços em branco

    resposta_usuario = input(
        f"Qual é a capital do estado {chave_sorteada}?: ")
    resposta_usuario = remover_acentos(resposta_usuario.lower().strip()) #na resposta do usuário,remove acentos, deixa tudo minusculo e tira espaços em branco

    del estados_capitais[chave_sorteada] #remove o estado sorteado do dicionário para não repetir a pergunta

    if resposta_usuario == capital_correta:
        print("Resposta correta!\n")
        acertos += 1
    else:
        print(f"Resposta incorreta! A Capital de {chave_sorteada} é {capital_original}.\n")
        
    if len(estados_capitais) > 0:
        continuar_ou_parar = input((f"Você quer continuar jogando? (s/n)"))
    else:
        print("Não há mais estados para perguntar. Congratulation! The game over!\n")
    

print(f"Você acertou {acertos} de {perguntas_feitas} perguntas. Isso corresponde a {(acertos/perguntas_feitas)*100:.2f}% de acertos totais. \n")

# 