from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate

db = SQLAlchemy()


def create_app():   
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    migrate = Migrate(app,db)

    with app.app_context():
        from app.models.clube import Clube  # Import routes to register them
        db.create_all()  # Create database tables

    from app.routes.main_route import main as main_blueprint
    app.register_blueprint(main_blueprint)
    # Register other blueprints if needed
    # Additional configurations can be added here   
    
    return app