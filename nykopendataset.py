import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_NYK_DATASET")

# ID do dataset "Housing Database"
DATASET_ID = 'uzf5-f8n2' 

# URL base da API Socrata para o NYC Open Data
BASE_URL = f'https://data.cityofnewyork.us/resource/{DATASET_ID}.json'

# Parâmetros da requisição (exemplo: buscando os 10 primeiros registros)
params = {
    '$limit': 10,
    # ATENÇÃO: Os nomes das colunas foram ajustados para o padrão Socrata (minúsculas, sublinhado)
    '$select': 'address, apartment_number, zip_code, residential_units, commercial_units, total_units, land_square_feet, gross_square_feet, year_built, tax_class_at_time_of_sale, building_class_at_time_of_sale, sale_price, sale_date',
    '$where': 'sale_price > 0 AND residential_units > 0',
    '$order': 'sale_date DESC',
}

# Cabeçalhos da requisição, incluindo o token da aplicação
headers = {
    'X-App-Token': api_key,
    'Accept': 'application/json'
}

try:
    response = requests.get(BASE_URL, params=params, headers=headers)
    response.raise_for_status()  # Levanta um erro para códigos de status HTTP ruins (4xx ou 5xx)

    data = response.json()

    print("Requisição bem-sucedida! Dados recebidos:")
    print(json.dumps(data, indent=2))

except requests.exceptions.HTTPError as http_err:
    # Se o erro for 400 Bad Request (provavelmente devido a nomes de coluna errados), esta mensagem aparecerá.
    print(f'Erro HTTP (Verifique os nomes das colunas no "$select"): {http_err}' )
except Exception as err:
    print(f'Outro erro: {err}')