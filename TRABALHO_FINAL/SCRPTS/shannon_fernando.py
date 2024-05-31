import numpy as np

def calcular_shannon(coluna):
    valores = coluna[coluna > 0].values
    prop = valores / valores.sum()
    shannon = -np.sum(prop * np.log(prop))
    return shannon

def calcular_shannon_para_tabela(tabela):
    return tabela.apply(calcular_shannon, axis=0)