"""Introdução ao for / in - estrutura de repetição para coisas finitas"""

texto = 'Python'

novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')
