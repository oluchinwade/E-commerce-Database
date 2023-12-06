from flask_sqlalchemy import SQLAlchemy
import datetime
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True,nullable=False)

class Vendor(db.Model):
    __tablename__ = 'vendors'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category = db.Column(db.String(128), unique=True, nullable=False)
    description = db.Column(db.String(280), unique=True, nullable=False)
    amount = db.Column(db.Numeric, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('vendors.id'), nullable=False)

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amount =  db.Column(db.Numeric, nullable=False)
    date_time = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)

product_oredr = db.Table(
    'product_order',
    db.Column('product_id', db.Integer, db.ForeignKey('products.id'), primary_key=True),
    db.Column('order_id', db.Integer, db.ForeignKey('orders.id'), primary_key=True),
    db.Column('date_time',db.DateTime, default=datetime.datetime.utcnow, nullable=False),
    db.Column('amount', db.Numeric, nullable=False)
)

