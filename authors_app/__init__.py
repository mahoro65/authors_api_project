from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from authors_app.extensions import db
from authors_app.extensions import migrate

# from authors_app.controllers import db
from authors_app.controllers.auth.auth_controllers import auth


#setting up an application factory and everything must be within the function
def create_app():
    
    app = Flask(__name__)

    app.config.from_object('config.Config')# registering the class from config.py #config function

    db.init_app(app)#initialization of our database instance
    migrate.init_app(app,db) # Use Migrate from flask_migrate to initialize migrations

    
    #importing and regitering models
    from authors_app.models.user import User
    # from authors_app.models.companies import Company
    # from authors_app.models.book import Book
    

#registering blue prints
    
    
#testing if the application is working
    @app.route('/') #route
    def home(): #the function
     return"hello world"
 
    app.register_blueprint(auth, url_prefix="/api/v1/auth")

 
 


    return app