from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  # Add this import statement
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})



metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def _repr_(self):
        return f'<Review {self.id}, {self.name}>'
    
class User(db.Model):
    __tablename__= 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    posts = db.relationship('Post')

    def _repr_(self):
        return f'<User {self.id}, {self.name}>'
    
    
class PostComment(db.Model):
    __tablename__ = 'post_comments'

    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    comment_id = db.Column(db.Integer, db.ForeignKey('comments.id'))

    post = db.relationship('Post', back_populates='comments')
    comment = db.relationship('Comment', back_populates='posts')
    def __repr__(self):
        return f'<PostComment {self.id}, {self.post_id}, {self.comment_id}>'



class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    content = db.Column(db.String)

    comments = db.relationship('Comment', secondary='post_comments', back_populates='posts')
    def __repr__(self):
        return f'<Post {self.id}, {self.title}, {self.content}>'



class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String)

    postComments = db.relationship('PostComment', back_populates='comment',cascade='all, delete-orphan')


    def __repr__(self):
        return f'<Comment  {self.id}, {self.text}>'

    if __name__ == '__main__':
        app.run(debug=True)
