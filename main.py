import flask_sqlalchemy as sa
from flask import Flask, request, jsonify
from professor import Professor
from flask_cors import cross_origin
import os

app = Flask(__name__)
app.config['SECRE_KEY'] = os.environ.get('SECRET_KEY')
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = sa.SQLAlchemy(app)

# def autenticação():
#     auth = request.headers.get('Authorization')
#     if app.config['SECRET_KEY'] in auth:
#         pass
#     else:
#         return jsonify(success=False, error_message="Authorization error. Invalid credential"), 403


@app.route('/professor/novo', methods=["POST"])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def inserir_professor():
    # recebe um formulário
    prof =  Professor(
        cpf = request.form.get('cpf'),
        nome = request.form.get('nome'),
        email = request.form.get('email'),
        senha = request.form.get('senha'),
        rua = request.form.get('rua'),
        complemento = request.form.get('compremento'),
        cep = request.form.get('cep'),
        bairro = request.form.get('bairro')
    )
    
    with app.app_context():
        cpf = db.session.execute(db.select( Professor).where( Professor.cpf == request.form.get('cpf'))).first()
        email = db.session.execute(db.select(Professor).where(Professor.email == request.form.get('email'))).first()
    

        if cpf:
            return jsonify(success=False, erro_message="cpf existente"), 409
        elif email:
            return jsonify(success=False, erro_message="email existente"), 409
        

        db.session.add(prof)
        db.session.commit()

    return jsonify(success=True)




@app.route('/professor/buscar/<int:matricula>', methods=["GET"])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def buscar_professor_por_matricula(matricula = None):
    
    results = {}
    with app.app_context():
        if matricula:
            select_result = db.session.execute(db.select(Professor).where(Professor.matricula == matricula)).first()
            results = {
                'matricula': select_result[0].matricula,
                'cpf' : select_result[0].cpf,
                'nome': select_result[0].nome,
                'email': select_result[0].email,
                'senha': select_result[0].senha,
                'rua': select_result[0].rua,
                'complemento': select_result[0].complemento,
                'cep': select_result[0].cep,
                'bairro': select_result[0].bairro
            }
            return jsonify(success=True, results=results)
        else:
            return jsonify(success=False)



@app.route('/professor/buscar', methods=["GET"])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def buscar_professor():
    results = {}
    with app.app_context():
        select_result = db.session.execute(db.select(Professor.matricula, Professor.nome))
        results = [{'matricula': i[0], 'nome': i[1]} for i in select_result.all()]
    
    return jsonify(success=True, results = results)
    



@app.route('/professor/atualizar/<int:matricula>', methods=["POST"])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def atualizar_professor(matricula):
    with app.app_context():
        
        professor = db.session.execute(db.select(Professor).where(Professor.matricula == matricula)).first()
        
        if professor:
            professor = professor[0]
            professor.nome = request.form.get('nome'),
            professor.email = request.form.get('email'),
            professor.senha = request.form.get('senha'),
            professor.rua = request.form.get('rua'),
            professor.complemento = request.form.get('compremento'),
            professor.cep = request.form.get('cep'),
            professor.bairro = request.form.get('bairro')
            db.session.commit()
            return jsonify(success=True)
        
        else:
            return jsonify(success=False, error_message= "não existe")
    


@app.route('/professor/deletar/<int:matricula>', methods=['DELETE'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def deletar_professor(matricula):
    with app.app_context():
        professor = db.session.execute(db.select(Professor).where(Professor.matricula == matricula)).first()
        if professor:
            db.session.delete(professor[0])
            db.session.commit()
            return jsonify(success=True)
        
        else:
            return jsonify(success=False, error_message= "não existe")


# @app.after_request()
# @cross_origin(origin='*',headers=['Content-Type','Authorization'])
# def response_aws():
#     request.headers.add('Access-Control-Allow-Origin', '*')


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))