# Controle de fluxo com validação de entrada

respostasValidas = ['sim', 's', 'não', 'nao', 'n']

while True:
    estaComFome = input('Você está com fome? (sim/não): ').lower().strip()
    if estaComFome in respostasValidas:
        break
    print('Resposta inválida. Por favor, responda com "sim" ou "não".')

if estaComFome in ['sim', 's']:
    while True:
        temComidaEmCasa = input(
            'Você tem comida em casa? (sim/não): ').lower().strip()
        if temComidaEmCasa in respostasValidas:
            break
        print('Resposta inválida. Por favor, responda com "sim" ou "não".')
    if temComidaEmCasa in ['sim', 's']:
        print('Ótimo! Prepare uma refeição em casa e coma a comida que você preparou.')
    else:
        print('Vá até o mercado e compre comida.')
        print('Volte para casa, prepare a refeição e coma!')
else:
    print('Ótimo! Continue aproveitando o seu dia sem se preocupar com comida.')
