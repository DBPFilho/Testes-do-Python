from random import shuffle
P = ('Sorteador')
print('{:_^65}'.format(P))
print('Quem são seus alunos?')
A1 = input('Primeiro aluno: ')
A2 = input('Segundo aluno: ')
A3 = input('Terceiro aluno: ')
A4 = input('Quarto aluno: ')
AE = ('{}, {}, {}, {}'.format(A1,A2,A3,A4)).split()
shuffle(AE)
print('O aluno escolhido foi {}'.format (AE))
