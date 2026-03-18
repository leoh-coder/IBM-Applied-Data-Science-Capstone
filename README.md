# Predicao de Pouso do Falcon 9 (IBM Capstone)

[English](README.en.md)

Autor: **Leonardo Henrique Ramos Ferreira**  
Curso: **IBM Applied Data Science Capstone**

## Visao Geral

Este projeto analisa se o **primeiro estagio do Falcon 9** pousa com sucesso.  
O fluxo cobre coleta de dados por API, web scraping, tratamento de dados, EDA com SQL e visualizacoes, mapas com Folium, dashboard com Dash e modelos de classificacao.

## Contexto de Negocio

A reutilizacao do primeiro estagio reduz custo de lancamento.  
Ao prever o sucesso de pouso com base em variaveis da missao (site de lancamento, orbita, carga util e versao do booster), e possivel estimar risco operacional com mais consistencia.

## Fontes de Dados

- API publica da SpaceX
- Tabelas da Wikipedia (web scraping)
- Arquivos locais processados para analise e dashboard

## Fluxo do Projeto (por notebook)

| Etapa | Notebook | Objetivo |
|---|---|---|
| 1 | `1. jupyter-labs-spacex-data-collection-api.ipynb` | Coletar dados de lancamentos via API |
| 2 | `2. jupyter-labs-webscraping.ipynb` | Extrair registros complementares via web scraping |
| 3 | `3. labs-jupyter-spacex-data-wrangling.ipynb` | Tratar dados e preparar base analitica |
| 4 | `4. jupyter-labs-eda-sql-coursera_sqllite.ipynb` | Realizar EDA com consultas SQL |
| 5 | `5. jupyter-labs-eda-dataviz.ipynb` | Realizar EDA visual (padroes por site, carga e orbita) |
| 6 | `6. lab_jupyter_launch_site_location.ipynb` | Analise geoespacial com Folium e proximidade |
| 7 | `7. SpaceX_Machine_Learning_Prediction_Part_5.jupyterlite.ipynb` | Treinar e avaliar modelos de classificacao |

## Principais Resultados

- SQL e EDA visual mostraram padroes diferentes entre os sites de lancamento.
- Site, orbita e massa de payload influenciam o resultado de pouso.
- Mapas Folium confirmam concentracao costeira dos lancamentos.
- Dashboard Dash (pizza e dispersao) facilita comparacao entre sites e cargas.
- Melhor modelo nesta execucao: **Decision Tree** com acuracia de teste em torno de **0.9444**.

### Comparacao de Acuracia dos Modelos

| Modelo | Acuracia |
|---|---|
| Regressao Logistica | 0.8333 |
| SVM | 0.8333 |
| Decision Tree | 0.9444 |
| KNN | 0.8333 |

## Arquivos do Repositorio

- `spacex_dash_app.py` - Aplicacao interativa em Plotly Dash
- `spacex_launch_dash.csv` - Base usada no dashboard
- `spacex_launch_geo.csv` - Base geoespacial usada no Folium
- `my_data1.db` - Banco SQLite usado nas consultas SQL
- `spacex_dash_app_screenshot.png` - Captura de tela do dashboard
- `DS-Capstone-Coursera.pdf` - Versao final da apresentacao em PDF
- `ds-capstone-template-coursera.pptx` - Arquivo editavel da apresentacao

## Preview do Dashboard

![Preview do Dashboard](spacex_dash_app_screenshot.png)

## Como Executar Localmente

1. Instale as dependencias:

```bash
pip install pandas numpy matplotlib seaborn plotly dash folium scikit-learn sqlalchemy ipython-sql
```

2. Execute os notebooks na ordem (`1` ate `7`).
3. Inicie o dashboard:

```bash
python spacex_dash_app.py
```

4. Abra no navegador:

```text
http://127.0.0.1:8060
```

## Entregaveis

- Apresentacao final: `DS-Capstone-Coursera.pdf`
- Fonte da apresentacao: `ds-capstone-template-coursera.pptx`

## Formato da Apresentacao

- O template segue o requisito do curso com **54 slides**.
- A versao final do deck foi feita em **portugues e ingles**.
