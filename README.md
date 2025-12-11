Perfeito! Aqui está **todo o README completo**, bem formatado e pronto para colar diretamente no seu arquivo `README.md`, **em um único bloco Markdown** — cobrindo tudo que precisa (instalação, `.env`, execução, estrutura e observações).

---

```markdown
# 🧠 Ciência de Dados - IA

Projeto desenvolvido para análise e visualização de dados utilizando **Python**, **Dash**, **Plotly** e **Mapbox**.  
O objetivo é explorar e apresentar informações de forma interativa, especialmente dados de imóveis da cidade de Nova York.

---

## ⚙️ Pré-requisitos

- **Python 3.8** ou superior  
- Conta no [Mapbox](https://www.mapbox.com/) para gerar a chave da API  
- Gerenciador de pacotes `pip`

---

## 🔑 Configuração do `.env`

Antes de rodar a aplicação, crie um arquivo chamado **`.env`** na raiz do projeto e adicione sua chave da API do Mapbox:

```

API_MAPBOX=Sua_Chave_Do_Mapbox

````

> ⚠️ Substitua `Sua_Chave_Do_Mapbox` pela sua chave obtida no site do Mapbox.

---

## 🧩 Instalação das Dependências

Instale todas as dependências do projeto listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
````

> 💡 **Dica:** É altamente recomendado criar um ambiente virtual para evitar conflitos de dependências:
>
> ```bash
> python -m venv venv
> source venv/bin/activate    # Linux / Mac
> venv\Scripts\activate       # Windows
> pip install -r requirements.txt
> ```

---

## 🚀 Execução da Aplicação

Após configurar o `.env` e instalar as dependências, execute o projeto com:

```bash
python index.py
```

O servidor será iniciado e exibirá um endereço local (geralmente):

```
http://127.0.0.1:8050
```

Abra o link no navegador para visualizar o dashboard interativo.

---

## 📁 Estrutura do Projeto

```
CIENCIA-DADOS-IA/
│
├── assets/                  # Arquivos estáticos (CSS, imagens etc.)
│
├── dataset/                 # Conjunto de dados utilizados
│   ├── brasil (simples)/    # Dados do professor
│   └── New York/            # Dados do professor de nova york
│       ├── cleaned_data.csv
│       └── nyc-rolling-sales.csv
│
├── .env                     # Contém a variável API_MAPBOX
├── .gitignore
├── README.md                # Este arquivo
├── requirements.txt         # Dependências do projeto
├── app.py                   # Configuração da aplicação Dash
├── index.py                 # Arquivo principal (executa o app)
├── _controllers.py          # Controle de callbacks e rotas
├── _histogram.py            # Geração de histogramas
├── _map.py                  # Módulo responsável pelos mapas interativos
├── data_treatment.py        # Limpeza e tratamento de dados
├── pyproject.toml           # Configuração de projeto (Poetry/Pip)
└── uv.lock                  # Arquivo de bloqueio de dependências
```

---

## 🧠 Funcionalidades Principais

* Visualização geográfica de imóveis com **Mapbox**
* Gráficos interativos de dispersão e histogramas
* Filtros dinâmicos para análise exploratória
* Estrutura modular para facilitar manutenção e expansão

---

## 🧾 Atualização das Dependências

Caso adicione novos pacotes, atualize o arquivo `requirements.txt` com o comando:

```bash
pip freeze > requirements.txt
```

---

## ⚠️ Observações Importantes

* O arquivo `.env` **não deve ser versionado** (já está listado no `.gitignore`).
* Se os mapas não carregarem, verifique se a variável `API_MAPBOX` está corretamente configurada.
* Execute o projeto sempre a partir do diretório raiz (`CIENCIA-DADOS-IA`).

---

## 👨‍💻 Autor

**Rodrigom, Iago e Icaro** — Estudantes de Engenharia de Computação
Projeto desenvolvido como parte de estudos em **Ciência de Dados e Inteligencia Computacional**.

```

