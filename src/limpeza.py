import pandas as pd

def padronizar_colunas(df):
    df.columns = (
        df.columns
        .str.lower()
        .str.strip()
        .str.replace(" ", "_")
    )
    return df

def converter_datas(df, colunas):
    for col in colunas:
        df[col] = pd.to_datetime(df[col], errors="coerce")
    return df

def remover_inconsistencias(df):
    return df.drop_duplicates().reset_index(drop=True)
