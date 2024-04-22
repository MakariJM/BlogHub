from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
from functools import wraps
import jwt
from flask_bcrypt import Bcrypt
from models import User, Post, Comment, PostComment


import secrets

# Generate a random secret key
secret_key = secrets.token_hex(16)  # 16 bytes for a hex-encoded secret key

print("Generated SECRET_KEY:", secret_key)


app = Flask(__name__)
app.config['SECRET_KEY'] = '44fe5d06e73553edd0d9349fb7c87575'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# Token authentication decorator
def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'error': 'Token is missing!'}), 401
        try:
            payload = jwt.decode(token, app.config['SECRET_KEY'])
        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Token has expired!'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Invalid token!'}), 401
        return func(*args, **kwargs)
    return decorated

# Routes

@app.route('/')
def home():
    return jsonify({'message': 'Welcome to GROUP 1 API'})

@app.route('/public')
def public():
    return jsonify({'message': 'This is a public endpoint.'})

@app.route('/auth')
@token_required
def auth():
    return jsonify({'message': 'JWT is verified. Welcome to your Dashboard.'})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if data.get('username') == 'username' and data.get('password') == 'password':
        token = jwt.encode({
            'user': data.get('username'),
            'exp': datetime.utcnow() + timedelta(seconds=120)
        }, app.config['SECRET_KEY'])
        return jsonify({'token': token.decode('utf-8')})
    else:
        return jsonify({'error': 'Unable to verify credentials!'}), 403

@app.route('/comments', methods=['POST'])
@token_required
def add_comment():
    data = request.get_json()
    text = data.get('text')
    post_id = data.get('post_id')

    if not text or not post_id:
        abort(400, 'Both text and post_id are required for adding a comment.')

    post = Post.query.get(post_id)
    if not post:
        abort(404, 'Post not found.')

    comment = Comment(text=text)
    post_comment = PostComment(post=post, comment=comment)

    db.session.add(comment)
    db.session.add(post_comment)
    db.session.commit()

    return jsonify({'message': 'Comment added successfully.'})

@app.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return jsonify([post.serialize() for post in posts])

@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = Post.query.get_or_404(post_id)
    return jsonify(post.serialize())

@app.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    user_id = data.get('user_id')

    if not title or not content or not user_id:
        abort(400, 'Title, content, and user_id are required for creating a post.')

    user = User.query.get(user_id)
    if not user:
        abort(404, 'User not found.')

    post = Post(title=title, content=content, user=user)
    db.session.add(post)
    db.session.commit()

    return jsonify({'message': 'Post created successfully.'})

@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')

    if not title or not content:
        abort(400, 'Both title and content are required for updating a post.')

    post.title = title
    post.content = content
    db.session.commit()

    return jsonify({'message': 'Post updated successfully.'})

@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()

    return jsonify({'message': 'Post deleted successfully.'})

if __name__ == '__main__':
    app.run(debug=True)
