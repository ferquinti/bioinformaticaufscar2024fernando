import string
import numpy as np
import pandas as pd

#Criar tabela vazia
def criar_tabela_vazia(n_colunas, n_indices):
    colunas = list(string.ascii_lowercase[:n_colunas])
    indices = [f"OTU_{x+1}" for x in range(n_indices)]
    tabela = pd.DataFrame(index=indices, columns=colunas)
    return tabela

# preenchendo a tabela vazia
def preencher_tabela(tabela_vazia):
    num_indices = tabela_vazia.shape[0]    
    for col in tabela_vazia.columns:
        values = np.random.randint(1, 3701, num_indices)
        tabela_vazia[col] = values

# zerando celulas aleatórias
def zerar_celulas(tabela_vazia, min_zeros=0.55, max_zeros=0.70):
    num_indices = tabela_vazia.shape[0]
    for col in tabela_vazia.columns:
        num_zeros = np.random.randint(int(min_zeros * num_indices), int(max_zeros * num_indices) + 1)
        zero_indices = np.random.choice(tabela_vazia.index, num_zeros, replace=False)
        tabela_vazia.loc[zero_indices, col] = 0

# Exportando
def exportar_tabela_csv(tabela_original, filename):
    tabela_original.to_csv(filename, sep='\t')