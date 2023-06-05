from config import app_active, app_config
from flask import Flask, request, jsonify
from controllers.ProfessorController import ProfessorController
from controllers.AlunoController import AlunoController
from flask_cors import cross_origin
import os


config = app_config[app_active]


def create_app(*config_name) -> Flask:
    app = Flask(__name__)
    app.config['SECRE_KEY'] = config.SECRET
    app.config.from_object(config)


    @app.route('/professor/add', methods=["POST"])
    @cross_origin(origin='*',headers=['Content-Type','Authorization'])
    def inserir_professor():
        # recebe um formulário
        response = ProfessorController().add(
            **request.form.to_dict()
        )
        return jsonify(success=response)

    
    @app.route('/professor/buscar/<int:matricula>', methods=["GET"])
    @app.route('/professor/buscar', methods=["GET"])
    @cross_origin(origin='*',headers=['Content-Type','Authorization'])
    def get_by_matricula(matricula = None):
        if matricula:
            return jsonify(success=True, results=ProfessorController().get_by_matricula(matricula=matricula))
        else:
            return jsonify(success=True, results=ProfessorController().get_all())
        

    @app.route('/professor/atualizar/<int:matricula>', methods=["POST"])
    @cross_origin(origin='*',headers=['Content-Type','Authorization'])
    def atualizar_professor(matricula):
        return jsonify(success=ProfessorController().update(matricula=matricula, **request.form.to_dict()))
        
        
    @app.route('/professor/deletar/<int:matricula>', methods=['DELETE'])
    @cross_origin(origin='*',headers=['Content-Type','Authorization'])
    def deletar_professor(matricula):
        return jsonify(success=ProfessorController().delete(matricula=matricula))
            

    return app
