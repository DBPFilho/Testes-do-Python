P = ('Adivinhação')
print('{:_^65}'.format(P))
from random import randint
C = randint(1,5)
E = int (input('Será que consegue adivinhar? Qual seu palpite (1-5): '))
print('{}'.format(C))
print('{}'.format(E))
if C==E:
    print ('Nossa, você acertou.')   
else:
    print ('Bom, era apenas 20% de chance. Tente novamente.')
