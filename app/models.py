from . import db
from datetime import datetime

# Tabela para Inquilinos
class Tenant(db.Model):
    __tablename__ = "Tenants"

    tenant_id = db.Column(db.Integer, primary_key=True)
    tenant_name = db.Column(db.String(255), nullable=False)
    tenant_status = db.Column(db.Boolean, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

# Tabela para Famílias
class Family(db.Model):
    __tablename__ = "Families"

    family_id = db.Column(db.Integer, primary_key=True)
    family_name = db.Column(db.String(255), nullable=False)
    budget = db.Column(db.Numeric(15, 2), nullable=False)
    tenant_id = db.Column(db.Integer, db.ForeignKey("Tenants.tenant_id"))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

# Tabela para Usuários
class User(db.Model):
    __tablename__ = "Users"

    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    full_name = db.Column(db.String(255), nullable=False)
    family_id = db.Column(db.Integer, db.ForeignKey("Families.family_id"))
    role = db.Column(db.String(255))
    tenant_id = db.Column(db.Integer, db.ForeignKey("Tenants.tenant_id"))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

# Tabela para Transações
class Transaction(db.Model):
    __tablename__ = "Transactions"

    transaction_id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    value = db.Column(db.Numeric(15, 2), nullable=False)
    payment_date = db.Column(db.Date)
    due_date = db.Column(db.Date, nullable=False)
    category = db.Column(db.String(255))
    description = db.Column(db.Text)
    installment_number = db.Column(db.Integer)
    credit_card = db.Column(db.String(255))
    bank_account = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey("Users.user_id"))
    tenant_id = db.Column(db.Integer, db.ForeignKey("Tenants.tenant_id"))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

# Tabela para Orçamentos e Metas
class BudgetGoal(db.Model):
    __tablename__ = "Budgets_Goals"

    bg_id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    value = db.Column(db.Numeric(15, 2), nullable=False)
    duration = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
    family_id = db.Column(db.Integer, db.ForeignKey("Families.family_id"))
    tenant_id = db.Column(db.Integer, db.ForeignKey("Tenants.tenant_id"))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

# Tabela para Tokens de Autenticação (JWT)
class AuthToken(db.Model):
    __tablename__ = "AuthTokens"

    token_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    token = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("Users.user_id"), nullable=False)
    expiration_date = db.Column(db.DateTime, nullable=False)
    scope = db.Column(db.String(255))
    type = db.Column(db.String(50), nullable=False)
    jti = db.Column(db.String(255))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Foreign Key Constraints
    user = db.relationship("User", foreign_keys=[user_id])

    # Indexes
    index_token = db.Index('idx_authtoken_token', token)
    index_user_id = db.Index('idx_authtoken_user_id', user_id)

# Create the database tables
db.create_all()