from datetime import datetime
from app import db

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    full_name = db.Column(db.String(255), nullable=False)
    family_id = db.Column(db.Integer, db.ForeignKey('families.family_id'))
    role = db.Column(db.String(255))
    tenant_id = db.Column(db.Integer, db.ForeignKey('tenants.tenant_id'))
    
    def __repr__(self):
        return f"<User {self.email}>"
