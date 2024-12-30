from dataclasses import dataclass
from flask import Flask, jsonify, abort, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
from flask_migrate import Migrate
import requests
from producer import publish

# Initialize Flask app and configure
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@db/main'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable track modifications

# Enable Cross-Origin Resource Sharing
CORS(app)

# Initialize database and Flask-Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# Define Product model with dataclass for serialization
@dataclass
class Product(db.Model):
    id: int
    title: str
    image: str

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))


# Define ProductUser model with unique constraint
@dataclass
class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    __table_args__ = (UniqueConstraint('user_id', 'product_id', name='user_product_unique'),)


# API to fetch all products
@app.route('/api/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify(products)


# API to like a product
@app.route('/api/products/<int:id>/like', methods=['POST'])
def like_product(id):
    # Simulate fetching user ID from another service
    try:
        req = requests.get('http://host.docker.internal:8000/api/user')
        req.raise_for_status()
        user_data = req.json()
    except requests.RequestException as e:
        abort(500, f"Failed to fetch user data: {e}")

    user_id = user_data.get('id')
    if not user_id:
        abort(400, "Invalid user data")

    # Add a new entry to the ProductUser table
    try:
        product_user = ProductUser(user_id=user_id, product_id=id)
        db.session.add(product_user)
        db.session.commit()

        # Publish a message to RabbitMQ
        publish('product_liked', {'user_id': user_id, 'product_id': id})
    except Exception as e:
        db.session.rollback()
        abort(400, f"You already liked this product or an error occurred: {e}")

    return jsonify({'message': 'Product liked successfully'})


# Health check or basic route
@app.route('/')
def index():
    return 'Hello, welcome to the Flask API!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
