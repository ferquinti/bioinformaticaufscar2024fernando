import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from criar_tabela_fernando import (
    criar_tabela_vazia, 
    preencher_tabela, 
    zerar_celulas, 
    exportar_tabela_csv
)
from tss_fernando import calcular_tss
from rarefacao_fernando import rarefar_tabela
from shannon_fernando import calcular_shannon_para_tabela
from curva_coletor_fernando import plotar_curvas

def main():
    
    np.random.seed(13)
    # Criando uma tabela vazia
    tabela = criar_tabela_vazia(26, 100)
    
    # Preenchendo a tabela com números aleatórios
    preencher_tabela(tabela)
    
    # Zerando células aleatórias da tabela
    zerar_celulas(tabela)
    
    # Soma das colunas
    soma_tabela = tabela.sum()
    
    # Aplicando o TSS
    tabela_tss = calcular_tss(tabela)
    
    # Soma das colunas
    soma_tss = tabela_tss.sum()
    
    # Aplicando a rarefação
    tabela_rarefada = rarefar_tabela(tabela)
    
    # Soma das colunas da tabela rarefeita
    soma_rarefada = tabela_rarefada.sum()

    #exportar as tabelas em TSV
    exportar_tabela_csv(tabela, "tabela_original.tsv")
    exportar_tabela_csv(tabela_tss, "tabela_tss.tsv")
    exportar_tabela_csv(tabela_rarefada, "tabela_rarefada.tsv")
    
    # Calcular Shannon para a tabela original
    shannon_original = calcular_shannon_para_tabela(tabela)
    
    # Calculando Shannon para a tabela TSS
    shannon_tss = calcular_shannon_para_tabela(tabela_tss)
    
    # Calculando Shannon para a tabela rarefeita
    shannon_rarefada = calcular_shannon_para_tabela(tabela_rarefada)
    
    dados_tabelas = {
        "Tabela": ["Tabela", "Tabela_TSS", "Tabela_Rarefada"],
        "Média": [soma_tabela.mean(), soma_tss.mean(), soma_rarefada.mean()],
        "Desvio Padrão": [soma_tabela.std(), soma_tss.std(), soma_rarefada.std()]
    }
    
    tabela_md = pd.DataFrame(dados_tabelas)
    exportar_tabela_csv(tabela_md, "tabela_md.tsv")
    
    plt.figure(figsize=(10, 6))
    plt.boxplot([soma_tabela, soma_tss, soma_rarefada], tick_labels=tabela_md["Tabela"])
    plt.title("Total de reads por amostra ")
    plt.xlabel("Tratamentos")
    plt.ylabel("Reads")
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.boxplot([shannon_original, shannon_tss, shannon_rarefada], tick_labels=tabela_md["Tabela"])
    plt.title("Shannon")
    plt.xlabel("Amostras")
    plt.ylabel("Índice de Shannon")
    plt.show()
    
    plotar_curvas(tabela, "Original")
    plotar_curvas(tabela_tss, "TSS")
    plotar_curvas(tabela_rarefada, "Rarefação")

if __name__ == "__main__":
    main()