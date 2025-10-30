✈️ Projeto API Schiphol - Pipeline de ETL com Python

Este projeto realiza um processo ETL (Extração, Transformação e Carga) completo utilizando dados da API pública do Aeroporto de Schiphol (Amsterdã).

Utilizando Python, o pipeline consome múltiplos endpoints, trata as informações de voos, companhias aéreas e destinos. O objetivo é demonstrar uma pipeline de dados robusta, com integração de APIs, lógica de paginação, transformação com Pandas e monitoramento via logging.

---

### ✨ Features Principais

* **Extração (Extract):** Consome 4 endpoints principais da API (Airlines, Destinations, Aircraft Types, Flights).
* **Lógica de Paginação Robusta:** Implementa um loop `while` que busca *todas* as páginas de resultados disponíveis na API, respeitando os limites com `time.sleep()`.
* **Monitoramento (Logging):** O script gera um arquivo `aeroporto.log` que registra cada etapa do processo (ex: "Buscando página X..."), permitindo o monitoramento em tempo real (como o nosso teste de 2 terminais).
* **Orquestração:** Um script `main.py` centralizado orquestra todo o fluxo, chamando os módulos de extração, transformação e carga em ordem.

---

### 🧩 Etapas do ETL

1.  **Extração**
    * Consumo da API oficial do Aeroporto de Schiphol com o módulo `requests`.
    * Testes de endpoints e parâmetros feitos no Postman para validar respostas e autenticação.
2.  **Transformação**
    * Limpeza e padronização dos dados JSON brutos com `Pandas`.
    * Ajustes de colunas, tipos de dados e tratamento de valores nulos.
3.  **Carga (Load)**
    * Armazenamento final dos dados limpos em arquivos `.csv` para futuras análises.

---

### ⚙️ Tecnologias Utilizadas

| Tecnologia | Descrição |
| :--- | :--- |
| **Python 3.x** | Linguagem principal do projeto |
| **Requests** | Consumo da API e lógica de paginação |
| **Pandas** | Manipulação e transformação de dados |
| **Postman** | Testes e validação dos endpoints da API |
| **python-dotenv**| Leitura segura das credenciais da API via arquivo `.env` |
| **Logging** | Monitoramento e registro de execução |

---

### 🔐 Segurança

As chaves de API e credenciais são armazenadas em um arquivo `.env`.
O arquivo `.gitignore` garante que informações sensíveis (como `.env`, `venv/`, `.csv` e `.log`) não sejam enviadas para o GitHub.

---

### 🚀 Como Executar o Projeto

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/DiegoHenry09/Api_Schiphol.git](https://github.com/DiegoHenry09/Api_Schiphol.git)
    cd Api_Schiphol
    ```

2.  **Crie e ative o ambiente virtual (venv):**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure suas Chaves de API (Obrigatório):**
    * Crie um arquivo chamado `.env` na pasta raiz (`Api_Schiphol/`).
    * Adicione suas chaves obtidas no site da Schiphol:
        ```ini
        APP_ID=SUA_APP_ID_AQUI
        APP_KEY=SUA_APP_KEY_AQUI
        ```

5.  **Execute o ETL Completo:**
    ```bash
    # (Estando na pasta raiz Api_Schiphol)
    python main.py
    ```
