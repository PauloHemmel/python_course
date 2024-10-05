frase = 'O Python é uma linguagem de programação '\
    'multiparadigma. ' \
    'Python foi criado por Guido van Rossum'

i = 0
qnt_apareceu_mais_vezes = 0
letra_apar3eceu_mais_vezes = ' '

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qnt_apareceu_mais_vezes_atual = frase.count(letra_atual)

    if qnt_apareceu_mais_vezes < qnt_apareceu_mais_vezes_atual:
        qnt_apareceu_mais_vezes = qnt_apareceu_mais_vezes_atual
        letra_apar3eceu_mais_vezes = letra_atual
    
    i += 1
print('A letra que apareceu mais vezes foi '
      f'"{letra_apar3eceu_mais_vezes}" que apareceu '
      f'{qnt_apareceu_mais_vezes}x')