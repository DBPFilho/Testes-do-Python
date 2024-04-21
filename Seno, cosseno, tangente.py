import math
P = ('Teorema de pitágoras')
print('{:_^65}'.format(P))
num = int(input('Qual o ângulo: '))
cos = math.cos(num)
sen = math.sin(num)
tan = math.tan(num)
print(' Seu cosseno é {} \n Seu seno é {} \n Sua tangente é {}'.format(cos, sen, tan))
