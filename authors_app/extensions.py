

from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate

from flask_bcrypt import Bcrypt # for ashing our passwords

# #from flask_jwt_extended import JWTManager# for creating tokens



#objects
db=SQLAlchemy()#db is the variable and the asiggned to is the instructor
migrate=Migrate()

bcrypt = Bcrypt()
#jwt = JWTManager()


