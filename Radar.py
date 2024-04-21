V = int (input ('Qual a velocidade? '))
M = (V-80)*7
if V>80:
    print('Deu ruim, a multa será de {:.2f}R$.'.format(M))
else:
    print('Tudo bem, siga viagem.')
