P = ('calculadora')
print('{:_^65}'.format(P))
print('\n Que números deseja?')
N1 = int(input('N1: '))
N2 = int(input('N2: '))
SOMA = N1+N2
SUBTRACAO = N1-N2
MULTIPLICACAO = N1*N2
POTENCIA = N1**N2
DIVISAO = N1/N2
DIVISAOINT = N1//N2
RESTO = N1%N2
RAIZ1 = N1** (1/2)
RAIZ2 = N2** (1/2)
ANT1 = N1-1
ANT2 = N2-1
SUC1 = N1+1
SUC2 = N2+1
D1 = N1*2
D2 = N2*2
T1 = N1*3
T2 = N2*3
MEDIA = (N1+N2)/2
print ('\n Seguem os seguintes cálulos: \n \n A soma entre eles é: {} \n A subtração entre eles é: {}'.format(SOMA, SUBTRACAO))
print (' A multiplicação entre eles é: {} \n A divisão entre eles é: {}'.format(MULTIPLICACAO, DIVISAO))
print (' A parte inteira da divisão entre eles é: {} \n O resto da divisão entre eles é: {}'.format(DIVISAOINT, RESTO))
print (' {} elevado a {} é: {} \n A raiz quadrada de {} é: {} \n A raiz quadrada de {} é: {}'.format(N1, N2, POTENCIA, N1, RAIZ1, N2, RAIZ2))
print (' O sucessor de {} é: {} \n O sucessor de {} é: {} \n O antecessor de {} é: {} \n O antecessor de {} é: {}'.format(N1, SUC1, N2, SUC2, N1, ANT1, N2, ANT2))
print (' O dobro de {} é: {} \n O dobro de {} é: {} \n O triplo de {} é: {} \n O triplo de {} é: {}'.format(N1, D1, N2, D2, N1, T1, N2, T2))
print (' A média entre {} e {} é {}'.format(N1, N2, MEDIA))
