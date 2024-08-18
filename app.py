from flask import Flask, render_template
from config import Config
from extensions import db
from flask_migrate import Migrate
from routes import main

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    register_resources(app)
    register_extensions(app)
    app.secret_key = 'ad1aeea3dba460d2419e7c62702bcc7e'  
    return app

def register_extensions(app):
    db.init_app(app)
    migrate = Migrate(app, db)

def register_resources(app):
    app.register_blueprint(main)
    @app.route('/', methods=['GET'])
    def home():
        return render_template('index.html')

if __name__ == "__main__":
    app = create_app()
    app.run(port=5001)
