from models.Aluno import Aluno


class AlunoController:
    def __init__(self) -> None:
        self.model_aluno = Aluno()
    
    def add(self, cpf: int, nome: str, telefone: str, email: str, senha: str, rua: str, complemento='', cep='', bairro='') -> bool:
        pass
    
    
    def get_all(self) -> list:
        pass
    

    def get_by_matricula(self, matricula: int) -> list[dict[str, any]]:
        pass
    

    def update(self, matricula: int, **kwords) -> bool:
        pass
    

    def delete(self, matricula: int) -> bool:
        pass