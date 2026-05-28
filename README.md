# 📊 Análise da Concessão dos Benefícios do RGPS em Sergipe (2019–2022)

Este repositório contém o projeto de análise de dados utilizado no Trabalho de Conclusão de Curso de Amanda Santos de Jesus (UFS), cujo objetivo foi investigar como ocorreram as concessões dos benefícios do **Regime Geral da Previdência Social (RGPS)** no estado de Sergipe entre **2019 e 2022**.

A análise foi desenvolvida em Python, utilizando dados públicos do Governo Federal, IBGE, CAGED e CadÚnico. O projeto combina **limpeza de dados**, **tratamento**, **visualização**, **estatística descritiva** e **interpretação contextual**, com foco no impacto social das políticas previdenciárias.

---

## 🧠 Objetivo do Projeto

Avaliar como se comportaram:

- as **solicitações** de benefícios;
- as **concessões**;
- os **indeferimentos**;
- os **motivos de indeferimento**;
- o perfil das pessoas solicitantes (gênero, idade, território);
- o impacto da pandemia e da contrarreforma da previdência (EC 103/2019).

---

## 📂 Estrutura do Repositório

---

## 📁 Estrutura do Repositório

```text
📁 rgps-sergipe-analise/
├── 📄 README.md
├── 📄 requirements.txt
├── 📁 data/
│   └── .gitkeep
├── 📁 notebooks/
│   └── analise_rgps_sergipe.ipynb
├── 📁 src/
│   ├── limpeza.py
│   ├── visualizacoes.py
│   └── utils.py
└── 📁 img/
    ├── grafico_beneficios.png
    ├── nuvem_indeferimentos.png
    └── ...
```


### 📁 Pastas

- **data/**  
  Pasta destinada aos arquivos de dados (não incluídos no repositório por boas práticas).

- **notebooks/**  
  Contém o notebook principal com todo o pipeline de análise.

- **src/**  
  Scripts auxiliares para limpeza, transformação e visualização.

- **img/**  
  Gráficos exportados para uso no README ou no TCC.

---

## 🛠️ Tecnologias Utilizadas

- Python 3.10+
- Pandas
- NumPy
- Matplotlib
- Seaborn
- WordCloud
- Jupyter Notebook

---

## 🔍 Metodologia

A análise segue as etapas:

1. **Coleta de dados**  
   Dados extraídos de portais oficiais (INSS, CAGED, CadÚnico, IBGE).

2. **Limpeza e padronização**  
   - Conversão de tipos  
   - Remoção de inconsistências  
   - Padronização de categorias  
   - Tratamento de valores ausentes  

3. **Análise exploratória (EDA)**  
   - Séries temporais  
   - Distribuições  
   - Comparações entre grupos  
   - Nuvem de palavras para motivos de indeferimento  

4. **Visualização**  
   Gráficos descritivos para facilitar a interpretação dos resultados.

5. **Interpretação**  
   Relacionando os dados com:
   - pandemia da COVID-19  
   - contrarreforma da previdência  
   - vulnerabilidade socioeconômica sergipana  

---

## 📊 Exemplos de Resultados

- Crescimento expressivo dos **indeferimentos** entre 2020 e 2022.  
- Redução das concessões durante a pandemia.  
- Predominância de solicitações feitas por **mulheres**.  
- Concentração de solicitantes entre **30 e 59 anos**.  
- Motivos de indeferimento relacionados a:
  - falta de documentação,
  - perda da qualidade de segurado,
  - ausência de carência.

---

## 🚀 Como Executar o Projeto

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/rgps-sergipe-analise.git
cd rgps-sergipe-analise
```
2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Abra o notebook:

```bash
jupyter notebook notebooks/analise_rgps_sergipe.ipynb
```

4. Coloque os arquivos de dados na pasta /data.

📚 Sobre o TCC
Este projeto foi desenvolvido como parte do TCC:

“Análise da Concessão dos Benefícios do Regime Geral da Previdência Social em Sergipe entre 2019 e 2022”  
Autora: Amanda Santos de Jesus  
Universidade Federal de Sergipe – 2023

📝 Licença
Este repositório está sob a licença MIT.
Sinta-se livre para usar, adaptar e compartilhar.


---

# 📦 Arquivo: `requirements.txt`

```txt
pandas
numpy
matplotlib
seaborn
wordcloud
jupyter
```

