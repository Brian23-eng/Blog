from . import db
from werkzeug.security import generate_password_hash,check_password_hash


class Quote:
    '''
    Quote class to define the quotes objects
    
    '''
    
    def __init__(self,author,quote):
        self.author = author
        self.quote = quote
        
        
class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    hash_pass = db.Column(db.String(255))
    
    
    @property
    def password(self):
        raise AttributeError("You can not read password attribution")
    @password.setter
    def password(self, password):
        self.hash_pass = generate_password_hash(password)
        
    def set_password(self,password):
        self.hash_pass = generate_password_hash(password)
        
    def verify_password(self, password):
        return check_password_hash(self.hash_pass, password)
    
    
    def __repr__(self):
        return f'User {self.username}'
    