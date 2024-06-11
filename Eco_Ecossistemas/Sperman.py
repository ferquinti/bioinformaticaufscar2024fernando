import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import spearmanr

data = {
    "Ecossistema/Local": [
        "FR-SP-IC", "PR-IM-FPI", "PR-IM-FNI", "PR-IM-RPP", "SP-G", "SP-C-PS-RP", "SP-C-PM-RM",
        "FA-SP-IC", "RJ-CG-FA50", "RJ-CG-FA200", "SP-RC", "SP-J", "SP-A", "SP-AR",
        "RJ-SFI-FAT-SCR", "RJ-SFI-FAT-CCS", "RR-IM-TB", "PA-TB", "SP-MG-MC", "SP-MG-CC",
        "SP-J-FA", "JM-FUEP", "JM-FUES"
    ],
    "KL": [
        1.07, 1.37, 1.12, 0.92, 0.72, 1.46, 1.09, 1.9, 1.54, 1.22, 1.5, 1.6, 1.1, 1.4, 0.38, 0.45, 2.0, 1.34, 
        0.59, 0.39, 1.3, 2.21, 2.56
    ],
    "Temperatura (ºC)": [
        21, 21.1, 21.1, 21.1, 22, 21.8, 21.8, 21.8, 21.8, 21.8, 21.8, 21.8, 21.8, 21.8, 21.8, 21.8, 21.8, 21.8, 
        21.8, 21.8, 21.8, 21.8, 21.8
    ],
    "Umidade (%)": [
        1700, 1429, 1429, 1429, 2050, 2486, 2396.5, 2600, 981.6, 981.6, 1360, 1140, 1350, 1441, 850, 850, 2300, 
        1900, 1411, 1100, 1140, 2685, 2685
    ],
    "Latitude": [
        -25.12566667, -25.51166667, -25.51166667, -25.51166667, -24.26666667, -23.83333333, -23.83333333,
        -25.12566667, -21.75444444, -21.75444444, -22.41083333, -23.18333333, -22.78333333, -22.3, 
        -21.47, -21.47, -2.083333333, -2, -21.99611111, -22.3, -23.18333333, 18.1, 18.1
    ]
}

df = pd.DataFrame(data)
df.set_index("Ecossistema/Local", inplace=True)

corr_spearman = df.corr(method='spearman')
plt.figure(figsize=(10, 8))
sns.heatmap(corr_spearman, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlação de Spearman')
plt.show()
