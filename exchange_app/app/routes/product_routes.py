from flask import Blueprint, request, redirect, url_for, jsonify

from ..database import db
from ..repositories.exchange_rate_repository import convert_to_pln
from ..repositories.product_repository import ProductRepository

product_bp = Blueprint('products', __name__)

product_repo = ProductRepository(db)


@product_bp.route('/', methods=['GET'])
def list_products():
    products = product_repo.get_all_products()
    return jsonify([product.to_dict() for product in products]) # list comprehention same as for p in products...



@product_bp.route('/', methods=['POST'])
def create_product():
    name = request.form['name']
    price_usd = request.form['price_usd']
    source = request.form['source']
    price_pln = convert_to_pln(price_usd)

    product_repo.create_product(name, price_usd, price_pln, source)
    return redirect(url_for('static_pages.products'))

@product_bp.route('/products/<int:product_id>', methods=['PUT'])
def update_product_route(product_id):
    data = request.json
    product_repo.update_product(product_id, data['name'], data['price_usd'])
    return jsonify({'message': 'Product updated successfully'})

@product_bp.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product_route(product_id):
    product_repo.delete_product(product_id)
    return jsonify({'message': 'Product deleted successfully'})




