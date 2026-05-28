import matplotlib.pyplot as plt
import seaborn as sns

def grafico_linha(df, x, y, titulo):
    plt.figure(figsize=(12, 5))
    sns.lineplot(data=df, x=x, y=y)
    plt.title(titulo)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.tight_layout()
    plt.show()
