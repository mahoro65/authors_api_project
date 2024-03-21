from authors_app.extensions import db
class Config:#allows us to centralise our applications configerations
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:@localhost/myapi' #SQL db  URI key, assigned to value of the connection string 
     
     
      
     #sqlite:///project.db