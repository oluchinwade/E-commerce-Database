from flask import Blueprint, jsonify, abort, request
from ..models import User, Vendor, Product, Order, product_order

import hashlib
import secrets

def scramble(password: str):
    """Hash and salt the given password"""
    salt = secrets.token_hex(16)
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()

bp = Blueprint('users', __name__, url_prefix='/users')

#Getting all users
@bp.route('', methods=['GET']) 
def index():
    users = User.query.all() # ORM performs SELECT query
    result = []
    for u in users:
        result.append(u.serialize()) # build list of Users as dictionaries in a JSON format
    return jsonify(result)




