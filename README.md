# ✈️ Projeto API Schiphol - ETL com Python

Este projeto realiza um processo **ETL (Extração, Transformação e Carga)** utilizando dados da **API do Aeroporto de Schiphol (Amsterdã)**.  
O objetivo é extrair informações de voos, tratar os dados e armazená-los de forma estruturada para análises posteriores.

---

## 🧩 Etapas do ETL

### 1. Extração
- Consumo da API oficial do Aeroporto de Schiphol.
- Requisições realizadas com o módulo **`requests`**.
- Testes de endpoints e parâmetros feitos no **Postman**, para validar respostas e autenticação.

### 2. Transformação
- Limpeza e padronização dos dados com **Pandas**.
- Ajustes de colunas, tipos de dados e horários de voo.
- Tratamento de possíveis valores nulos e inconsistências.

### 3. Carga
- Armazenamento final em arquivo `.csv` para futuras análises e integração com ferramentas de BI.

---

## ⚙️ Tecnologias Utilizadas

| Tecnologia | Descrição |
|-------------|------------|
| **Python 3.x** | Linguagem principal do projeto |
| **Requests** | Consumo da API |
| **Pandas** | Manipulação e transformação de dados |
| **Postman** | Testes e validação dos endpoints da API |
| **dotenv** | Leitura segura das credenciais da API via arquivo `.env` |

---

## 🔐 Segurança

- As **chaves de API e credenciais** são armazenadas em um arquivo `.env`, que **não é enviado para o GitHub**.
- O arquivo `.gitignore` garante que informações sensíveis permaneçam protegidas.

---

## 🚀 Como Executar o Projeto

### 1. Clonar o repositório
```bash
git clone https://github.com/DiegoHenry09/Api_Schiphol.git
cd Api_Schiphol
