   
# from authors_app.controllers import db
# from authors_app.extensions import db
# from datetime import datetime


# class Company(db.Model):
#  __tablename__="Companies"
#  id =db.Column(db.Integer,primary_key=True)
#  name=db.Column(db.String(100),nullable=False,unique=True)
#  origin=db.Column(db.String(100),nullable=False)
#  description=db.Column(db.String(100),nullable=False)
 
#  user_id =db.Column(db.Integer, db.ForeignKey("user.id"))#refering to the table plus the id for which the relationship occurs
 
#  #time below helps to store the time and date at which a user was created in our system
#  created_at = db.Column(db.DateTime, default =datetime.now())
#  updated_at = db.Column(db.DateTime, onupdate =datetime.now())
 
#  #defining the relationship between the user and the company
#  user=db.relationship('User',backref='companies')#backref helps the user to acces the different campanys that thyve created
 
 
 
 
#  def __init__(self,name,origin,discription,user_id):#defining an instructor then pass in the attributes
#         super(Company,self)._init__()
#         self.name = name
#         self.origin = origin
#         self.discription = discription
#         self.user_id = user_id
  
  
#   #string representation for the campanies that will be created
# def __repr__(self):
#     return f"<company(name='{self.name}',origin ='{self.origin}')>"
        

    
 