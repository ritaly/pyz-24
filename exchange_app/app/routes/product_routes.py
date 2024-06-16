from flask import Blueprint, request, redirect, url_for, jsonify

from ..repositories.exchange_rate_repository import convert_to_pln
from ..repositories.product_repository import ProductRepository

product_bp = Blueprint('products', __name__)


@product_bp.route('/', methods=['GET'])
def list_products():
    products = ProductRepository.get_all_products()
    return jsonify([product.to_dict() for product in products]) # list comprehention same as for p in products...



@product_bp.route('/', methods=['POST'])
def create_product():
    name = request.form['name']
    price_usd = request.form['price_usd']
    source = request.form['source']
    price_pln = convert_to_pln(price_usd)

    ProductRepository.create_product(name, price_usd, price_pln, source)
    return redirect(url_for('static_pages.products'))

# HOMEWORK
# update

# delete




