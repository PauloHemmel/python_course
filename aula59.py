# Desempacotamento em chamadas
# de métodos e funções

salas = [
    ['Maria', 'Helena',],

    ['Elaine',],

    ['Luiz', 'João', 'Eduarda',]
]

string = 'ABCD'
lista = ['Maria', 'Helena', 1,2,3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

# p, b *_, ap, u = lista
# print(p, u ap)

print(*lista)
print(*string)
print(*tupla)
print(*salas, sep='\n')