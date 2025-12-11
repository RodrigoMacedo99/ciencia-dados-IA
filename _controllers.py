from dash import html, dcc
import dash_bootstrap_components as dbc
from app import app


list_of_locations = {
    "Todos": 0,
    "Manhattan": 1,
    "Bronx": 2,
    "Brooklyn": 3,
    "Queens": 4,
    "Staten Island ": 5,
}

slider_size = [100, 500, 1000, 10000, 10000000]

controllers = dbc.Row([
                dcc.Store(id='store-global'),
                html.Img(id="logo", src=app.get_asset_url("cimatec.png"), style={'width':'50%'}),
                html.H3("Vendas de imóveis - NYC", style={"margin-top": "30px"}),
                html.P(
                """Dashboard para analisar vendas ocorridas na 
                cidade de New York no período de 1 ano (2016 - 2017) """
                ),

                html.H4("""Borough""", style={"margin-top": "50px", "margin-bottom": "50px"}),
                dcc.Dropdown(
                    id="location-dropdown",
                    options=[{"label": i, "value": j} for i, j in list_of_locations.items()],
                    value=0,
                    placeholder="Select a borought"),

                html.P("""Metragem (m2)""", style={"margin-top": "20px"}),

                dcc.Slider(min=0, max=4, id='slider-square-size', value=4,
                marks = {i: str(j)for i, j in enumerate(slider_size)}),

                # Variável de COR para o Mapa
                html.P("""Variável de COR (Mapa)""", style={"margin-top": "20px"}),
                
                dcc.Dropdown(
                    options=[
                        {'label': 'ANO DE CONSTRUÇÃO', 'value': 'YEAR BUILT'},
                        {'label': 'TOTAL DE UNIDADES', 'value': 'TOTAL UNITS'},
                        {'label': 'PREÇO DE VENDA', 'value': 'SALE PRICE'},
                    ],
                    value='SALE PRICE',
                    id="dropdown-color"),

                # Variável para o Eixo X do Gráfico de Dispersão (NOVA ANÁLISE)
                html.P("""Eixo X do Gráfico de Dispersão""", style={"margin-top": "20px"}),
                dcc.Dropdown(
                    options=[
                        {'label': 'Área Bruta', 'value': 'GROSS SQUARE FEET'},
                        {'label': 'Ano de Construção', 'value': 'YEAR BUILT'},
                        {'label': 'Total de Unidades', 'value': 'TOTAL UNITS'},
                    ],
                    value='GROSS SQUARE FEET',
                    id="dropdown-scatter-x")
    ])