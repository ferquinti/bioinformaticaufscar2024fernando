def calcular_tss(tabela_original):
    soma_colunas = tabela_original.sum(axis=0)
    prop = tabela_original / soma_colunas
    multiplicado = prop * 100000
    inteiros = multiplicado.astype(int)
    return inteiros