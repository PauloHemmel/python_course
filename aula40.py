""" Calculadora com while"""
while True:
    sair = input('Quer sair? [s]im: ')
    sair = sair.lower()
    sair = sair.startswith('s')
    print(sair)