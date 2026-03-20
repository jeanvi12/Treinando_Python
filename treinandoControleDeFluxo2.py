# validando usuário e senha com if, elif e else

usuario_correto = 'jean'
senha_correta = '123'

usuario_digitado = input('Digite o seu nome de usuário: ').strip()
senha_digitada = input('Digite a sua senha: ').strip()

if usuario_digitado == usuario_correto and senha_digitada == senha_correta:
    print('Login realizado com sucesso!')
elif usuario_digitado != usuario_correto and senha_digitada != senha_correta:
    print('Usuário e senha incorretos.')
elif usuario_digitado != usuario_correto:
    print('Usuário incorreto.')
else:
    print('Senha incorreta.')

print(f'{"_"*10}Fim do programa.{"_"*10}')
