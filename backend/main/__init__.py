import os
from flask import Flask
from dotenv import load_dotenv

#Importo el modulo para crear la api-rest
from flask_restful import Api

#Importo el modulo para conectarme con una base SQL
from flask_sqlalchemy import SQLAlchemy

api = Api()

db = SQLAlchemy()

def create_app():

    app = Flask(__name__)

    #cargo las variables de entorno
    load_dotenv()

    #Configuración de la base de datos
    PATH = os.getenv("DATABASE_PATH")
    DB_NAME = os.getenv("DATABASE_NAME")
    if not os.path.exists(f'{PATH}{DB_NAME}'):
        os.chdir(f'{PATH}')
        file = os.open(f'{DB_NAME}', os.O_CREAT)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{PATH}{DB_NAME}'
    db.init_app(app)

    import main.resources as resources
    api.add_resource(resources.ClientesResource, '/clientes')
    api.add_resource(resources.ClienteResource, '/cliente/<id>')
    api.add_resource(resources.UsuariosResource, '/usuarios')
    api.add_resource(resources.UsuarioResource, '/usuario/<id>')

    api.init_app(app)
 
    return app