from app import app, db
from models import User, Comment, Post

def seed():
    print('Seeding...')

    user1 = User(name='User1')
    user2 = User(name='User2')

    # Create posts
    post1 = Post(title='Post 1 Title', content='Content of post 1')
    post2 = Post(title='Post 2 Title', content='Content of post 2')

    # Create comments
    comment1 = Comment(text='Comment 1 text')
    comment2 = Comment(text='Comment 2 text')

    # Associate comments with posts
    post1.comments.append(comment1)
    post2.comments.append(comment2)

    # Add objects to the session
    db.session.add(user1)
    db.session.add(user2)
    db.session.add(post1)
    db.session.add(post2)
    db.session.add(comment1)
    db.session.add(comment2)

    # Commit the session to the database
    db.session.commit()
    
if __name__ == '__main__':
    seed()