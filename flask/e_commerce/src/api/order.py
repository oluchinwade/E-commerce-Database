from flask import Blueprint, jsonify, abort, request
from ..models import User, Vendor, Product, Order, product_order

bp = Blueprint('orders', __name__, url_prefix='/orders')