import random
n1 = input('primeiro aluno:')
n2 = input('Segundo aluno:')
n3 = input('Terceiro aluno')
n4 = input('Quarto aluno')
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentação é:')
print(lista)