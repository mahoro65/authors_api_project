
# from authors_app.extensions import db
# from datetime import datetime

# class Book(db.Model):
#     __tablename__ ='books'
#     id=db.Column(db.Integer, primary_key=True)
#     title=db.Column(db.String(150),nullable=False)
#     pages=db.Column(db.Integer,nullable=False)
#     price=db.Column(db.Integer,nullable=False)
#     price_unit=db.Column(db.String(50),nullable=False,default='UGX')
#     publication_date=db.Column(db.Date,nullable=False)# date of when the book was published
#     isbn=db.Column(db.String(30), nullable=True, unique=True)#international standard book number
#     genre=db.Column(db.String(50), nullable=False)#category to which each book belongs
#     description=db.Column(db.String(255),nullable=False)
#     image=db.Column(db.String(255),nullable=True)#nuallable optional
#     user_id=db.Column(db.Integer, db.ForeignKey('user.id'))
#     company_id=db.Column(db.Integer, db.ForeignKey('Companies.id'))#keeps track of the company id to which each book is going to belong 
    
#      #time below helps to store the time and date at which a user was created in our system
#     created_at = db.Column(db.DateTime, default =datetime.now())
#     updated_at = db.Column(db.DateTime, onupdate =datetime.now())
 
#     #relationship between the user and the book and the user
#     #user=db.relationship('User',backref='books')
#     company=db.relationship('company',backref='books')
#     user = db.relationship('User', backref='user_books')

    
    
    
# def __init__(self,title,user_id,pages,isbn,image,genre,price,company_id,publication_date,description):#constructor for the book class
#   super(Book,self).__init__()#ensures that any necesarry initialization from the db.model class is excuted before the initilization of the book class
#   self.title = title
#   self.price = price
#   self.description = description
#   self.pages = pages
#   self.image = image
#   self.genre = genre
#   self.company_id = company_id
#   self.publication_date = publication_date
#   self.isbn = isbn
#   self.user_id = user_id
  
  
  #string representation for our book class
def __repr__(self)->str:#rep function returns a string type of an instace that has been created
    return f"Book{self.title}"

  
    
    
 
  
    
       
       
    
 