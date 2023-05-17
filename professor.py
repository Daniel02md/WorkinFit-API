import flask_sqlalchemy as sa

db = sa.SQLAlchemy()

class Professor(db.Model):
    __tablename__ = "Professor"
    matricula = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cpf = db.Column(db.String(12), unique=True, nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    senha = db.Column(db.String(15), nullable=False)
    rua = db.Column(db.String(50), nullable=False)
    complemento = db.Column(db.String(50), nullable=True)
    cep = db.Column(db.String(12), nullable=False)
    bairro = db.Column(db.String(12), nullable=True)


    def __init__(self, cpf, nome, email, senha, rua, complemento='', cep='', bairro='', extend_existing = True):
        self.cpf = cpf
        self.nome = nome
        self.email = email
        self.senha = senha
        self.rua = rua
        self.complemento = complemento
        self.cep = cep
        self.bairro = bairro
        

    