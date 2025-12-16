from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def createApp():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/flasktodo'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = "secret"
    db.init_app(app)

    from . import models

    with app.app_context():
        db.create_all()



    from app.routes.todo import todo_bp
    from app.routes.auth import auth_bp
    app.register_blueprint(todo_bp)
    app.register_blueprint(auth_bp)


    return app