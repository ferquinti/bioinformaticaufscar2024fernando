import pandas as pd
import numpy as np

def rarefar_tabela(tabela):
    min_reads = tabela.sum(axis=0).min()  #  Achando o mínimo da soma de reads
    def rarefar_coluna(coluna):
        reads = coluna.values
        #  fazendo um array para os indices e repetidindo os elementos  proporcionalmente aos reads -:> um vetor
        vetor = np.repeat(np.arange(len(reads)), reads)
        np.random.shuffle(vetor)  #  embaralhar os elementos do vetor
        escolher_elementos = np.random.choice(vetor, min_reads, replace=False)  #  escolhendo os elementos do vetor
        contar_elementos = np.bincount(escolher_elementos, minlength=len(reads))  #  agrupando os elementos em reads novamente
        return contar_elementos
    tabela_rarefada = tabela.apply(rarefar_coluna, axis=0)  #  aplicando as funções nas colunas
    tabela_rarefada_final = pd.DataFrame(tabela_rarefada, index=tabela.index, columns=tabela.columns)
    return tabela_rarefada_final