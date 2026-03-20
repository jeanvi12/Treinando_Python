#Número Secreto - Jogo de Adivinhação

import random

numero_secreto = random.randint(1, 100)
acertou = False


for tentativa in range(5):
    chute = int(input("Adivinhe o número secreto entre 1 e 100: "))
    if chute > numero_secreto:
        print("Muito alto! Tente mais baixo.")
    elif chute < numero_secreto:
        print("Muito baixo! Tente mais alto.")
    else:
        acertou = True
        print(f"Parabéns! Você acertou o número secreto: {numero_secreto}")
        break
if not acertou:
    print(f"Você esgotou suas tentativas. O número secreto era: {numero_secreto}")
