#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db
from models import db, User, BlogPost, Comment, PostComment 

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!
        # Create users
    
        users = []
        for _ in range(5):
            user = User(name=fake.name())
            users.append(user)
        db.session.add_all(users)
        db.session.commit()

        # Create blog posts
        posts = []
        for _ in range(10):
            post = BlogPost(name=fake.text(20), user_id=randint(1, len(users)))
            posts.append(post)
        db.session.add_all(posts)
        db.session.commit()

        # Create comments
        comments = []
        for _ in range(15):
            comment = Comment(text=fake.text(50))
            comments.append(comment)
        db.session.add_all(comments)
        db.session.commit()

        # Create post comments
        post_comments = []
        for _ in range(20):
            post_comment = PostComment(post_id=randint(1, len(posts)), comment_id=randint(1, len(comments)))
            post_comments.append(post_comment)
        db.session.add_all(post_comments)
        db.session.commit()

        print("Seed completed successfully!")