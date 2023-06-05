from models.Professor import Professor


class ProfessorController:
    def __init__(self) -> None:
        self.model_professor = Professor()
    
    def add(self, cpf, nome, telefone, email, senha, rua, complemento, cep, bairro):
        return self.model_professor.add(
            cpf=cpf,
            nome=nome,
            telefone=telefone, 
            email=email, 
            senha=senha, 
            rua=rua, 
            complemento=complemento, 
            cep=cep, 
            bairro=bairro
        )
    

    def get_all(self):
        response = []
        results = self.model_professor.get_all()
        for result in results:
            response.append(
                {
                    'matricula': result[0].matricula,
                    'cpf' : result[0].cpf,
                    'nome': result[0].nome,
                    'telefone': result[0].telefone,
                    'email': result[0].email,
                    'senha': result[0].senha,
                    'rua': result[0].rua,
                    'complemento': result[0].complemento,
                    'cep': result[0].cep,
                    'bairro': result[0].bairro
                }
            )
        return response
    

    def get_by_matricula(self, matricula: int):
        result = self.model_professor.get_by_matricula(matricula=matricula)
        if result:
            response = {
                'matricula': result[0].matricula,
                'cpf' : result[0].cpf,
                'nome': result[0].nome,
                'telefone': result[0].telefone,
                'email': result[0].email,
                'senha': result[0].senha,
                'rua': result[0].rua,
                'complemento': result[0].complemento,
                'cep': result[0].cep,
                'bairro': result[0].bairro
            }
        else:
            response = {}
        return response
    

    def update(self, matricula: int, **kwords):
        return self.model_professor.update(matricula, **kwords)
    
    
    def delete(self, matricula: int):
        return self.model_professor.delete(matricula=matricula)