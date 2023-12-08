from flask import Blueprint, jsonify, abort, request
from ..models import User, Vendor, Product, Order, product_order

bp = Blueprint('products', __name__, url_prefix='/products')

# Getting all products
@bp.route('', methods=['GET']) # decorator takes path and list of HTTP verbs
def index():
    products = Product.query.all() # ORM performs SELECT query
    result = []
    for p in products:
        result.append(p.serialize()) # build list of Users as dictionaries
    return jsonify(result)