from . import db, app
from sqlalchemy.types import Integer, BigInteger, String
from sqlalchemy.schema import Column
from sqlalchemy.sql.expression import insert, select, update, delete

# RETURN REFERENCE IMPORTS
from typing import Sequence, Optional
from sqlalchemy.engine.row import Row
from sqlalchemy.engine.result import _TP

# =============================

class Aluno(db.Model):
    __tablename__ = "Alunos"
    matricula = Column(Integer, primary_key=True, autoincrement=True)
    cpf = Column(BigInteger, unique=True, nullable=False)
    nome = Column(String(110), nullable=False)
    telefone = Column(String(20), nullable=False)
    email = Column(String(110), unique=True, nullable=False)
    senha = Column(String(15), nullable=False)
    rua = Column(String(110), nullable=False)
    complemento = Column(String(110), nullable=True)
    cep = Column(String(12), nullable=False)
    bairro = Column(String(110), nullable=True)


    def add(self, cpf: int, nome: str, telefone: str, email: str, senha: str, rua: str, complemento='', cep='', bairro='') -> bool:
        try: 
            with app.app_context():
                db.session.execute(
                    insert(Aluno).values(cpf=cpf,
                                        nome=nome,
                                        telefone=telefone, 
                                        email=email, 
                                        senha=senha, 
                                        rua=rua, 
                                        complemento=complemento, 
                                        cep=cep, 
                                        bairro=bairro))
                db.session.commit()
        except:
            return False
        finally:
            return True
            

    def get_all(self) -> Sequence[Row[_TP]]:
        with app.app_context():
            try:
                results = db.session.execute(select(Aluno)).all()
            except:
                results = []
            finally:
                return results


    def get_by_matricula(self, matricula) -> Optional[Row[_TP]]:
        with app.app_context():
            try: 
                res = db.session.execute(select(Aluno).where(Aluno.matricula == matricula)).first()
            except:
                res = []
            finally:    
                return res 
            
        

    def update(self, matricula, **kwargs) -> bool:
        with app.app_context():
            if self.get_by_matricula(matricula=matricula):
                db.session.execute(update(Aluno)
                                        .where(Aluno.matricula == matricula)
                                        .values(**kwargs))
                db.session.commit()
                return True
            else:
                return False
        

    def delete(self, matricula) -> bool:
        with app.app_context():
            if self.get_by_matricula(matricula=matricula):
                db.session.execute(delete(Aluno).where(Aluno.matricula == matricula))
                db.session.commit()
                return True
            else:
                return False