# from flask import Flask
# from flask_login import LoginManager
# from DirectReport.datadependencies import appsecrets
# from .auth.auth import auth
#
# from flask_login import LoginManager
#
# app = Flask(__name__, template_folder="templates")
# app.register_blueprint(auth)
# app.secret_key = appsecrets.SECRET_KEY
# login_manager = LoginManager(app)
# login_manager.login_view = "login"
#
# # def create_app():
# #     app = Flask(__name__, template_folder="templates")
# #     app.register_blueprint(auth)
# #     app.secret_key = appsecrets.SECRET_KEY
# #     login_manager.init_app(app)
# #     login_manager.login_view = "login"
# #     return app
#
#
# # from flask_sqlalchemy import SQLAlchemy
# # from flask_login import LoginManager
# # db = SQLAlchemy()
# # login_manager = LoginManager()
# # def create_app():
# #     """Construct the core app object."""
# #     app = Flask(__name__, instance_relative_config=False)
# #     # Application Configuration
# #     app.config.from_object('config.Config')
# #     # Initialize Plugins
# #     db.init_app(app)
# #     login_manager.init_app(app)
# #     with app.app_context():
# #         from . import routes
# #         from . import auth
# #         from .assets import compile_assets
# #         # Register Blueprints
# #         app.register_blueprint(routes.main_bp)
# #         app.register_blueprint(auth.auth_bp)
# #         # Create Database Models
# #         db.create_all()
# #         # Compile static assets
# #         if app.config['FLASK_ENV'] == 'development':
# #             compile_assets(app)
# #         return app