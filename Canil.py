from itertools import permutations

# Função para verificar se uma distribuição satisfaz as restrições
def verifica_restricoes(distribuicao):
    a, b, c = distribuicao
    if (a == 'A' and b == 'B') or (a == 'B' and b == 'A'):
        return False
    if (a == 'A' and c == 'C') or (a == 'C' and c == 'A'):
        return False
    if (b == 'B' and c == 'C') or (b == 'C' and c == 'B'):
        return False
    return True

# Gera todas as permutações possíveis dos elementos A, B e C
permutacoes = permutations(['A', 'B', 'C'])

# Lista para armazenar as distribuições válidas
distribuicoes_validas = []

# Verifica cada permutação e armazena as distribuições válidas
for permutacao in permutacoes:
    if verifica_restricoes(permutacao):
        distribuicoes_validas.append(permutacao)

# Imprime as distribuições válidas
for distribuicao in distribuicoes_validas:
    print("Conjunto 1:", distribuicao[0])
    print("Conjunto 2:", distribuicao[1])
    print("Conjunto 3:", distribuicao[2])
    print()
