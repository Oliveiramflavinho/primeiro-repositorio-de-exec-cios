import random

n1 = input('Primeio Aluno:')
n2 = input('Segundo aluno:')
n3 = input('Terceiro aluno:')
n4 = input('Quarto aluno:')
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O escolhido foi:{}'.format(escolhido))
