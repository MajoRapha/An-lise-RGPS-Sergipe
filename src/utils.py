import pandas as pd

def carregar_csv(caminho):
    return pd.read_csv(caminho, sep=";", encoding="utf-8", low_memory=False)
