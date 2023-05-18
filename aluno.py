import flask_sqlalchemy as sa 
db = sa.SQLAlchemy()

class Aluno(db.Model):
    __tablename__ = "Alunos"
    matricula = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cpf = db.Column(db.BigInteger, unique=True, nullable=False)
    nome = db.Column(db.String(110), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(110), unique=True, nullable=False)
    senha = db.Column(db.String(15), nullable=False)
    rua = db.Column(db.String(110), nullable=False)
    complemento = db.Column(db.String(110), nullable=True)
    cep = db.Column(db.String(12), nullable=False)
    bairro = db.Column(db.String(110), nullable=True)


    def __init__(self, cpf, nome, telefone, email, senha, rua, complemento='', cep='', bairro='', extend_existing = True):
        self.cpf = cpf
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.senha = senha
        self.rua = rua
        self.complemento = complemento
        self.cep = cep
        self.bairro = bairro

    