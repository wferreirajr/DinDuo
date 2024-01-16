# DinDuo: Seu Aplicativo de Gerenciamento Financeiro

## Visão Geral

DinDuo é um aplicativo de gerenciamento financeiro que oferece recursos como controle de transações, gerenciamento de usuários e famílias, e muito mais.

## Tecnologias Utilizadas

- **Linguagem de Programação**: Python
- **Framework Web**: Flask
- **Banco de Dados**: SQLite

## Estrutura de Pastas e Arquivos Atualizada

```plaintext
DinDuo/
├── app/
│   ├── - `__init__.py`
│   ├── main/
│   │   ├── - `__init__.py`
│   │   ├── - `templates/`
│   │   └── - `static/`
│   ├── api/
│   │   ├── - `__init__.py`
│   │   ├── auth/
│   │   │   ├── - `__init__.py`
│   │   │   ├── models.py
│   │   │   └── routes.py
│   │   ├── transactions/
│   │   │   ├── - `__init__.py`
│   │   │   ├── models.py
│   │   │   └── routes.py
│   │   ├── users/
│   │   │   ├── - `__init__.py`
│   │   │   ├── models.py
│   │   │   └── routes.py
│   │   ├── families/
│   │   │   ├── - `__init__.py`
│   │   │   ├── models.py
│   │   │   └── routes.py
│   │   └── ... (outras features)
│   └── common/
│       ├── - `__init__.py`
│       └── (utilitários compartilhados)
├── tests/
│   ├── - `__init__.py`
│   ├── test_auth.py
│   ├── test_transactions.py
│   ├── test_users.py
│   ├── test_families.py
│   └── ... (outros testes)
├── venv/
├── config.py
├── requirements.txt
├── .env
└── run.py
```

## Descrição dos Arquivos

### `app/`

- `__init__.py`: Inicializa o aplicativo Flask e configura as blueprints.

### `app/main/`

- `__init__.py`: Inicializa a parte principal do aplicativo.
- `templates/`: Contém os templates HTML para renderização no lado do cliente.
- `static/`: Armazena arquivos estáticos como CSS, JavaScript e imagens.

### `app/api/`

Cada subdiretório dentro de api/ representa uma feature separada com seu próprio conjunto de modelos e rotas.

Exemplo: `app/api/auth/`
- `__init__.py`: Inicializa a blueprint específica da feature.
- `models.py`: Define os modelos de dados relacionados à autenticação.
- `routes.py`: Contém as rotas e lógicas associadas à autenticação.

### `app/common/`

- `__init__.py`: Pode ser usado para importar vários utilitários comuns.

### `Raiz`

- `config.py`: Configurações do aplicativo.
- `run.py`: Script para iniciar o aplicativo Flask.
- `requirements.txt`: Dependências do projeto.

### `Como Executar`

Para executar este projeto, siga as etapas abaixo:

1. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

2. Execute o script `run.py`:
    ```bash
    python run.py
    ```

Isso iniciará o servidor Flask, e você poderá acessar o aplicativo em `http://localhost:5000/`.

## Modelo de Dados

Neste projeto, usamos várias tabelas para organizar nossa estrutura de dados. Cada tabela e sua estrutura são explicadas abaixo.

---

## Contribuição
(Sinta-se à vontade para contribuir com o projeto, seguindo as diretrizes para issues e pull requests.)

## Teste curl
(Exemplo de comando curl para testar a API.)