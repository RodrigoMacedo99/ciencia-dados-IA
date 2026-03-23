# Dashboard de Vendas de Imóveis em Nova York

## Descrição do Projeto

Este projeto consiste em um dashboard interativo desenvolvido em Python utilizando a biblioteca Dash, que permite a visualização e análise de dados de vendas de imóveis na cidade de Nova York. O objetivo é fornecer uma ferramenta para explorar tendências de preços, localização e características dos imóveis, como área e ano de construção, em diferentes bairros (Boroughs) da cidade.
<img width="1884" height="877" alt="image" src="https://github.com/user-attachments/assets/4b61a96e-4ef8-4b7c-a513-89655b12d1bf" />

## Funcionalidades

*   **Visualização Interativa de Dados:** Explore dados de vendas de imóveis através de um mapa interativo e um gráfico de dispersão.
*   **Filtros por Localização:** Selecione bairros específicos de Nova York para focar a análise.
*   **Filtros por Área:** Ajuste o tamanho dos imóveis em metros quadrados para refinar a busca.
*   **Personalização de Visualização:** Altere a variável de cor no mapa e o eixo X do gráfico de dispersão para diferentes perspectivas de análise.
*   **Dados Georreferenciados:** Utilização de dados de latitude e longitude para plotagem precisa no mapa.

## Estrutura do Projeto

O projeto é organizado nos seguintes arquivos:

*   `app.py`: Arquivo principal da aplicação Dash, responsável pela inicialização do servidor.
*   `index.py`: Define o layout principal do dashboard, integra os componentes de controle e visualização, e implementa os callbacks para a interatividade.
*   `data_treatment.py`: Script responsável pelo pré-processamento dos dados brutos de vendas de imóveis. Inclui limpeza de dados, conversão de tipos, filtragem e geocodificação de endereços utilizando a API HERE.
*   `_controllers.py`: Define os componentes da interface do usuário (UI) para os controles do dashboard, como dropdowns de seleção de localização, variáveis de cor e eixo X, e um slider para a área dos imóveis.
*   `_map.py`: Define a estrutura inicial do componente de mapa, que é posteriormente preenchido com dados e interatividade via `index.py`.
*   `_histogram.py`: Apesar do nome, este arquivo define a estrutura inicial para o gráfico de dispersão (scatter plot), que também é populado e atualizado dinamicamente pelo `index.py`.
*   `dataset/`: Diretório que contém os arquivos de dados, incluindo `nyc-rolling-sales.csv` (dados brutos) e `cleaned_data.csv` (dados tratados).
*   `keys/`: Diretório que armazena a chave da API HERE (não incluída no repositório por segurança).
*   `dict_notes.json`: Arquivo JSON utilizado para armazenar em cache as coordenadas geográficas dos endereços já consultados, evitando requisições repetidas à API.

## Tecnologias Utilizadas

*   **Python 3.x**
*   **Dash:** Framework para construção de aplicações web analíticas.
*   **Plotly Express:** Biblioteca para criação de gráficos interativos.
*   **Dash Bootstrap Components (dbc):** Componentes de layout e estilo baseados em Bootstrap para Dash.
*   **Pandas:** Biblioteca para manipulação e análise de dados.
*   **NumPy:** Biblioteca para computação numérica.
*   **Requests:** Biblioteca para fazer requisições HTTP (utilizada para a API HERE).
*   **python-dotenv:** Para carregar variáveis de ambiente (como a chave da API).

## Como Executar o Projeto

Para executar este projeto localmente, siga os passos abaixo:

1.  **Clone o repositório:**

    ```bash
    git clone <URL_DO_REPOSITORIO>
    cd <DIRETORIO_DO_PROJETO>
    ```

2.  **Crie um ambiente virtual (recomendado):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: `venv\Scripts\activate`
    ```

3.  **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```
    (Você precisará criar um arquivo `requirements.txt` com as dependências listadas acima, ou instalá-las manualmente.)

4.  **Obtenha uma chave da API HERE:**
    *   Crie uma conta em [HERE Developer](https://developer.here.com/).
    *   Gere uma chave de API para o serviço Geocoding & Search.
    *   Crie um diretório `keys/` na raiz do projeto.
    *   Dentro de `keys/`, crie um arquivo chamado `here_api` e cole sua chave da API nele.

5.  **Execute o script de tratamento de dados:**

    ```bash
    python data_treatment.py
    ```
    Este script irá baixar e processar os dados, além de geocodificar os endereços, salvando o resultado em `dataset/cleaned_data.csv` e as coordenadas em `dict_notes.json`.

6.  **Execute a aplicação Dash:**

    ```bash
    python app.py
    ```

    A aplicação estará disponível em `http://127.0.0.1:8050/` no seu navegador.

## Fontes de Dados

Os dados brutos utilizados neste projeto são provenientes do arquivo `nyc-rolling-sales.csv`, que contém informações sobre vendas de imóveis em Nova York. As coordenadas geográficas (latitude e longitude) são obtidas através da API de Geocodificação da [HERE Technologies](https://developer.here.com/documentation/geocoding-search-api/api-reference-dev-guide.html).

## Tratamento de Dados

O script `data_treatment.py` realiza as seguintes etapas de tratamento:

*   Carregamento do dataset `nyc-rolling-sales.csv`.
*   Substituição de valores ausentes ou inválidos (representados por ' - ') por 0.
*   Conversão de colunas relevantes (`LAND SQUARE FEET`, `GROSS SQUARE FEET`, `SALE PRICE`) para o tipo numérico (float).
*   Conversão da coluna `SALE DATE` para o tipo datetime.
*   Remoção de registros onde `SALE PRICE`, `LAND SQUARE FEET` ou `GROSS SQUARE FEET` são iguais a 0.
*   Geocodificação dos endereços únicos presentes no dataset utilizando a API HERE para obter latitude e longitude. Os resultados são armazenados em `dict_notes.json` para evitar chamadas repetidas à API.
*   Criação das colunas `LATITUDE` e `LONGITUDE` no DataFrame principal.
*   Salvamento do DataFrame tratado em `dataset/cleaned_data.csv`.

## Visualizações

O dashboard apresenta duas visualizações principais:

1.  **Mapa de Dispersão (Scatter Mapbox):** Exibe os imóveis no mapa de Nova York, com a possibilidade de colorir os pontos por diferentes variáveis (Ano de Construção, Total de Unidades, Preço de Venda) e ajustar o tamanho dos pontos com base na área do imóvel.
2.  **Gráfico de Dispersão (Scatter Plot):** Apresenta a relação entre o preço de venda e uma variável selecionável pelo usuário (Área Bruta, Ano de Construção, Total de Unidades), permitindo identificar correlações e padrões.
