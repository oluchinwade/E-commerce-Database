from flask import Blueprint, jsonify, abort, request
from ..models import User, Vendor, Product, Order, product_order

bp = Blueprint('vendors', __name__, url_prefix='/vendors')

# Getting all vendors
@bp.route('', methods=['GET']) # decorator takes path and list of HTTP verbs
def index():
    vendors = Vendor.query.all() # ORM performs SELECT query
    result = []
    for v in vendors:
        result.append(v.serialize()) # build list of Users as dictionaries
    return jsonify(result)