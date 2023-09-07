# DinDuo: Seu Aplicativo de Gerenciamento Financeiro

## Visão Geral

DinDuo é um aplicativo de gerenciamento financeiro que oferece recursos como controle de transações, gerenciamento de usuários e famílias, e muito mais.

## Tecnologias Utilizadas

- **Linguagem de Programação**: Python
- **Framework Web**: Flask
- **Banco de Dados**: PostgreSQL

## Estrutura de Diretórios

DinDuo/
├── app/
│   ├── __init__.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── transactions.py
│   │   ├── users.py
│   │   └── families.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── user.py
│   │   ├── transaction.py
│   │   └── family.py
│   └── utils/
│       └── __init__.py
├── config.py
├── run.py
└── requirements.txt

DinDuo/
├── app/
│ ├── init.py
│ ├── routes/
│ │ ├── init.py
│ │ ├── auth.py
│ │ ├── transactions.py
│ │ ├── users.py
│ │ └── families.py
│ ├── models/
│ │ ├── init.py
│ │ ├── base.py
│ │ ├── user.py
│ │ ├── transaction.py
│ │ └── family.py
│ └── utils/
│ └── init.py
├── config.py
├── run.py
└── requirements.txt


## Descrição dos Arquivos

### `app/`

- `__init__.py`: Inicializa o aplicativo Flask e reúne outras partes do projeto.
  
### `app/routes/`

- `__init__.py`: Usado para importar e organizar todas as rotas criadas em outros arquivos dentro do diretório `routes`.
- `auth.py`: Contém as rotas e lógica associadas à autenticação.
- `transactions.py`: Contém as rotas e lógica para lidar com transações financeiras.
- `users.py`: Contém as rotas e lógica para lidar com informações do usuário.
- `families.py`: Contém as rotas e lógica para lidar com grupos de usuários ou famílias.

### `app/models/`

- `__init__.py`: Importa todos os modelos de dados usados no aplicativo.
- `base.py`: Contém classes e funções base que são comuns a muitos modelos.
- `user.py`: Define o modelo de dados para usuários.
- `transaction.py`: Define o modelo de dados para transações financeiras.
- `family.py`: Define o modelo de dados para famílias ou grupos de usuários.

### `app/utils/`

- `__init__.py`: Pode ser usado para importar vários utilitários.

### Raiz

- `config.py`: Usado para configurar o aplicativo.
- `run.py`: Script para iniciar o aplicativo Flask.
- `requirements.txt`: Lista todas as bibliotecas Python que o projeto depende.

## Como Executar

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

### Tabela Tenants

**Descrição:** Tabela que armazena informações sobre os inquilinos ou organizações.

- `tenant_id`: Chave primária.
- `tenant_name`: Nome do inquilino ou da organização.
- `tenant_status`: Estado do inquilino (ativo ou inativo).

**Índices**
- `idx_tenant_name`: Índice no campo `tenant_name`.
- `idx_tenant_status`: Índice no campo `tenant_status`.

---

### Tabela Families

**Descrição:** Tabela que armazena informações sobre as famílias ou grupos.

- `family_id`: Chave primária.
- `family_name`: Nome da família.
- `budget`: Orçamento da família.
- `tenant_id`: Chave estrangeira para Tenants.

**Índices**
- `idx_family_tenant_id`: Índice no campo `tenant_id`.

---

### Tabela Users

**Descrição:** Tabela que armazena informações sobre os usuários.

- `user_id`: Chave primária.
- `email`: Endereço de email do usuário.
- `password`: Senha criptografada.
- `full_name`: Nome completo do usuário.
- `family_id`: Chave estrangeira para Families.
- `role`: Função do usuário (ex: "chefe da família", "membro").

**Índices**
- `idx_user_email`: Índice no campo `email`.
- `idx_user_family_id`: Índice no campo `family_id`.
- `idx_user_tenant_id`: Índice no campo `tenant_id`.

---

(... O restante das tabelas pode seguir o mesmo formato)


## Contribuição

Sinta-se à vontade para contribuir com o projeto. Abra uma `issue` ou faça um `pull request`.


