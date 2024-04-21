import json

with open('config.json', 'r') as arquivo:
    dados = json.load(arquivo)

guerreiro_geral_1 = dados['guerreiro_geral_1']
guerreiro_geral_2 = dados['guerreiro_geral_2']
guerreiro_geral_3 = dados['guerreiro_geral_3']

print(guerreiro_geral_1)  # Valor de A
print(guerreiro_geral_2)  # Valor de B
print(guerreiro_geral_3)  # Valor de C
