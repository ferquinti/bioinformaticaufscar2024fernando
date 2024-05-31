import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

def amostrar_reads(coluna):
    reads_acumulados = []
    riqueza_acumulada = []
    especies_unicas = set()
    total_amostrado = coluna.sum()
    reads_somados = 0

    while reads_somados < total_amostrado:
        # Realizar a amostragem
        amostra = np.random.choice(coluna.index, size=10, p=coluna / coluna.sum(), replace=True)
        reads_somados += 10
        # Adicionar novas espécies ao conjunto
        especies_unicas.update(amostra)
        # Calcular a riqueza acumulada (número total de espécies únicas)
        riqueza_acumulada.append(len(especies_unicas))
        reads_acumulados.append(reads_somados)
    return reads_acumulados, riqueza_acumulada

def suavizar_dados(x, y, pontos=10000):
    # Interpolação dos dados para suavizar a curva
    interpolador = interp1d(x, y, kind='cubic')
    x_suave = np.linspace(min(x), max(x), pontos)
    y_suave = interpolador(x_suave)
    return x_suave, y_suave

def plotar_curvas(tabela, titulo, metodo_suavizacao='interpolacao'):
    # Aplicar a função amostrar_reads a todas as colunas
    resultados = tabela.apply(amostrar_reads)
    # Inicializar a plotagem
    plt.figure(figsize=(10, 6))
    # Plotar cada coluna
    for coluna, (reads_acumulados, riqueza_acumulada) in resultados.items():
        if metodo_suavizacao == 'interpolacao':
            x_suave, y_suave = suavizar_dados(reads_acumulados, riqueza_acumulada)
        else:
            raise ValueError("Método de suavização desconhecido. Use 'interpolacao'.")
        plt.plot(x_suave, y_suave, label=coluna)
    
    # Ajustar a escala do eixo x para logarítmica
    plt.xscale('log')
    # Adicionar título e rótulos
    plt.title(titulo)
    plt.xlabel('Reads Acumulados (escala logarítmica)')
    plt.ylabel('Riqueza Acumulada')
    plt.grid(True, which="both", ls="--")
    # Mostrar o gráfico
    plt.show()