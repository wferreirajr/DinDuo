/*
    psql -h localhost -U postgres -d dinduodb -a -f create-tables.sql
    DROP DATABASE dinduodb;
    CREATE DATABASE dinduodb;
    DROP TABLE tabela1, tabela2, tabela3, ...;

    CONECTAR NO BANCO
    psql -U postgres -h localhost dinduodb

    conectar no banco
    \c FamilyFinances

    LISTAR TABLES
    \dt

    LISTAR DATABASES
    \l

    LISTAR COLUNAS DE UMA TABELA
    \d nome_da_tabela

    COMO COMENNTAR UM BLOCO DE CÓDIGO
*/

-- Tabela para Inquilinos
CREATE TABLE Tenants (
    tenant_id INT PRIMARY KEY,
    tenant_name VARCHAR(255) NOT NULL,
    tenant_status BOOLEAN NOT NULL
);
COMMENT ON TABLE Tenants IS 'Tabela que armazena informações sobre os inquilinos ou organizações.';

-- Tabela para Famílias
CREATE TABLE Families (
    family_id INT PRIMARY KEY,
    family_name VARCHAR(255) NOT NULL,
    budget DECIMAL(15,2),
    tenant_id INT,
    FOREIGN KEY (tenant_id) REFERENCES Tenants(tenant_id)
);
COMMENT ON TABLE Families IS 'Tabela que armazena informações sobre as famílias ou grupos.';

-- Tabela para Usuários
CREATE TABLE Users (
    user_id INT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL, -- Estamos supondo uma criptografia de até 255 caracteres
    full_name VARCHAR(255) NOT NULL,
    family_id INT,
    role VARCHAR(255),
    tenant_id INT,
    FOREIGN KEY (family_id) REFERENCES Families(family_id),
    FOREIGN KEY (tenant_id) REFERENCES Tenants(tenant_id)
);
COMMENT ON TABLE Users IS 'Tabela que armazena informações sobre os usuários.';

-- Tabela para Transações
CREATE TABLE Transactions (
    transaction_id INT PRIMARY KEY,
    date DATE NOT NULL,
    value DECIMAL(15,2) NOT NULL,
    payment_date DATE,
    due_date DATE NOT NULL,
    category VARCHAR(255),
    description TEXT,
    installment_number INT,
    credit_card VARCHAR(255),
    bank_account VARCHAR(255),
    user_id INT,
    tenant_id INT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (tenant_id) REFERENCES Tenants(tenant_id)
);
COMMENT ON TABLE Transactions IS 'Tabela que armazena informações sobre as transações financeiras.';

-- Tabela para Orçamentos e Metas
CREATE TABLE Budgets_Goals (
    bg_id INT PRIMARY KEY,
    type VARCHAR(50) NOT NULL,
    value DECIMAL(15,2) NOT NULL,
    duration VARCHAR(50) NOT NULL,
    description TEXT,
    family_id INT,
    tenant_id INT,
    FOREIGN KEY (family_id) REFERENCES Families(family_id),
    FOREIGN KEY (tenant_id) REFERENCES Tenants(tenant_id)
);
COMMENT ON TABLE Budgets_Goals IS 'Tabela que armazena informações sobre os orçamentos e metas das famílias.';

-- Tabela para Ativos, Dívidas e Investimentos
CREATE TABLE Assets_Debts_Investments (
    adi_id INT PRIMARY KEY,
    type VARCHAR(50) NOT NULL,
    value DECIMAL(15,2) NOT NULL,
    description TEXT,
    family_id INT,
    tenant_id INT,
    FOREIGN KEY (family_id) REFERENCES Families(family_id),
    FOREIGN KEY (tenant_id) REFERENCES Tenants(tenant_id)
);
COMMENT ON TABLE Assets_Debts_Investments IS 'Tabela que armazena informações sobre os ativos, dívidas e investimentos das famílias.';

-- Tabela para Notificações
CREATE TABLE Notifications (
    notification_id INT PRIMARY KEY,
    user_id INT,
    message TEXT NOT NULL,
    status BOOLEAN NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    tenant_id INT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (tenant_id) REFERENCES Tenants(tenant_id)
);
COMMENT ON TABLE Notifications IS 'Tabela que armazena informações sobre as notificações enviadas aos usuários.';

-- Tabela para Instituições Bancárias
CREATE TABLE Banks (
    bank_id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    tenant_id INT,
    FOREIGN KEY (tenant_id) REFERENCES Tenants(tenant_id)
);
COMMENT ON TABLE Banks IS 'Tabela que armazena informações sobre as instituições bancárias.';

-- Tabela para Contas Bancárias
CREATE TABLE Bank_Accounts (
    account_id INT PRIMARY KEY,
    user_id INT,
    bank_id INT,
    account_type VARCHAR(50) NOT NULL,
    balance DECIMAL(15,2) NOT NULL,
    account_number VARCHAR(50) NOT NULL,
    tenant_id INT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (bank_id) REFERENCES Banks(bank_id),
    FOREIGN KEY (tenant_id) REFERENCES Tenants(tenant_id)
);
COMMENT ON TABLE Bank_Accounts IS 'Tabela que armazena informações sobre as contas bancárias dos usuários.';

-- Tabela para Cartões de Crédito
CREATE TABLE Credit_Cards (
    card_id INT PRIMARY KEY,
    card_brand VARCHAR(50) NOT NULL,
    credit_limit DECIMAL(15,2) NOT NULL,
    credit_due_date DATE NOT NULL,
    best_purchase_day INT,
    user_id INT,
    bank_id INT,
    tenant_id INT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (bank_id) REFERENCES Banks(bank_id),
    FOREIGN KEY (tenant_id) REFERENCES Tenants(tenant_id)
);
COMMENT ON TABLE Credit_Cards IS 'Tabela que armazena informações sobre os cartões de crédito dos usuários.';

-- Índices para Tenants
CREATE INDEX idx_tenant_name ON Tenants(tenant_name);
CREATE INDEX idx_tenant_status ON Tenants(tenant_status);

-- Índices para Users
CREATE INDEX idx_user_email ON Users(email);
CREATE INDEX idx_user_family_id ON Users(family_id);
CREATE INDEX idx_user_tenant_id ON Users(tenant_id);

-- Índices para Families
CREATE INDEX idx_family_tenant_id ON Families(tenant_id);

-- Índices para Transactions
CREATE INDEX idx_transaction_date ON Transactions(date);
CREATE INDEX idx_transaction_user_id ON Transactions(user_id);
CREATE INDEX idx_transaction_tenant_id ON Transactions(tenant_id);

-- Índices para Budgets_Goals
CREATE INDEX idx_bg_family_id ON Budgets_Goals(family_id);
CREATE INDEX idx_bg_tenant_id ON Budgets_Goals(tenant_id);

-- Índices para Assets_Debts_Investments
CREATE INDEX idx_adi_family_id ON Assets_Debts_Investments(family_id);
CREATE INDEX idx_adi_tenant_id ON Assets_Debts_Investments(tenant_id);

-- Índices para Notifications
CREATE INDEX idx_notification_user_id ON Notifications(user_id);
CREATE INDEX idx_notification_tenant_id ON Notifications(tenant_id);
CREATE INDEX idx_notification_timestamp ON Notifications(timestamp);

-- Índices para Banks
CREATE INDEX idx_bank_tenant_id ON Banks(tenant_id);

-- Índices para Bank_Accounts
CREATE INDEX idx_bank_account_user_id ON Bank_Accounts(user_id);
CREATE INDEX idx_bank_account_bank_id ON Bank_Accounts(bank_id);
CREATE INDEX idx_bank_account_tenant_id ON Bank_Accounts(tenant_id);

-- Índices para Credit_Cards
CREATE INDEX idx_credit_card_user_id ON Credit_Cards(user_id);
CREATE INDEX idx_credit_card_bank_id ON Credit_Cards(bank_id);
CREATE INDEX idx_credit_card_tenant_id ON Credit_Cards(tenant_id);
