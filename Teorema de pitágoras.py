from math import sqrt
P = ('Teorema de pitágoras')
print('{:_^65}'.format(P))
CO = int(input('Qual o cateto oposto? '))
CA = int(input('Qual o cateto adjacente? '))
H = (CO**2) + (CA**2)
print ('A hipotenusa é: {}'.format (sqrt(H)))
