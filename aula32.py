"""
Faça um programa que peça ao usuário para digitar
um número inteiro, informe se este número é par ou
ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
#METODO 1
# entrada = input('Digite um número: ')

# if entrada.isdigit():
#     entrada_int = int(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'ímpar'

#     if par_impar:
#         par_impar_texto = 'par'

#     print(f'O número {entrada_int} é {par_impar_texto}')
# else:
#     print('Você não digitou um número inteiro')


#METODO 2
# entrada = input('Digite um número: ')

# try:
#      entrada_int = int(entrada)
#      par_impar = entrada_int % 2 == 0
#      par_impar_texto = 'ímpar'

#      if par_impar:
#          par_impar_texto = 'par'
#      print(f'O número {entrada_int} é {par_impar_texto}')
# except:
#      print('Você não digitou um número inteiro')

"""
Faça um programa que pergunte a hora ao usuário e,
baseando-se no horário descrito, exiba a saudação
apropriada. Ex. Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# horario =  int(input('Que horas são? '))

# if horario >= 0 and horario <= 11:
#     print('Bom dia 0-11')
# elif horario >= 12 and horario <= 17:
#     print('Boa tarde 12-17')
# else:
#     print('Boa noite 18-23')

entrada =  input('Digite a hora em números inteiros: ')

try:
    horario = int(entrada)
    
    if horario >= 0 and horario <= 11:
        print('Bom dia 0-11')
    elif horario >= 12 and horario <= 17:
        print('Boa tarde 12-17')
    elif horario >= 18 and horario <= 23:
        print('Boa noite 18-23')
    else:
        print('Não conheço essa hora')
except:
    print('Por favor, digite apenas números inteiros')

"""
Faça um programa que peça o primeiro nome do usuário.
Se o nome tiver 4 letras ou menos escreva 
"Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal" ; maior que 6 esvreca "Seu nome é muito grande".
"""

# nome = input('Escreva seu primeiro nome: ')
# nomestring = len(nome)

# if len(nome) <= 4:
#     print("Seu nome é curto")
# elif len(nome) >= 5 and len(nome) <= 6:
#     print("Seu nome é normal")
# else:
#     print("Seu nome é muito grande")