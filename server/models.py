from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
from extensions import bcrypt
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})



# db = SQLAlchemy(metadata=metadata)




class User(db.Model, SerializerMixin):
    __tablename__= 'users'
    serialize_rules = ('-posts.user',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    _password_hash = db.Column(db.String, nullable=False)

    posts = db.relationship('Post')

    def __repr__(self):
        return f'<User {self.id}, {self.name}>'
    
    @hybrid_property
    def password_hash(self):
        return self._password_hash

    @password_hash.setter
    def password_hash(self, password):
        # utf-8 encoding and decoding is required in python 3
        password_hash = bcrypt.generate_password_hash(
            password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(
            self._password_hash, password.encode('utf-8'))





class Post(db.Model, SerializerMixin):#to serialize the data
    __tablename__ = 'posts'
    serialize_rules = ('-comments.post',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'<Review {self.id}, {self.name}>'
    
   
   
class Comment(db.Model, SerializerMixin):
    __tablename__ = 'comments'
    serialize_rules = ('-postComments.comment',)

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String)
    postComments = db.relationship('PostComment', back_populates='comment',cascade='all, delete-orphan')
    def __repr__(self):
        return f'<Comment  {self.id}, {self.text}>'

   
  
   
    
class PostComment(db.Model, SerializerMixin):
    __tablename__ = 'post_comments'
    serialize_rules = ('-post.comments', '-comment.posts')

    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    comment_id = db.Column(db.Integer, db.ForeignKey('comments.id'))

    post = db.relationship('Post', back_populates='comments')
    comment = db.relationship('Comment', back_populates='posts')
    def __repr__(self):
        return f'<PostComment {self.id}, {self.post_id}, {self.comment_id}>'


