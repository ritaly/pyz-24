from flask import Blueprint, request, redirect, url_for, jsonify

from ..database import db
from ..repositories.exchange_rate_repository import convert_to_pln
from ..repositories.product_repository import ProductRepository

product_bp = Blueprint('products', __name__)

product_repo = ProductRepository(db, convert_to_pln)


@product_bp.route('/', methods=['GET'])
def list_products():
    products = product_repo.get_all_products()
    return jsonify([product.to_dict() for product in products]), 200


@product_bp.route('/', methods=['POST'])
def create_product():
    name = request.form.get('name')
    price_usd = request.form.get('price_usd')
    source = request.form.get('source')

    if not name or not price_usd:
        return jsonify({'error': 'Missing required data'}), 400

    try:
        price_usd = float(price_usd)
    except ValueError:
        return jsonify({'error': 'Invalid input for price'}), 400

    product = product_repo.create_product(name, price_usd, source)
    if product:
        return redirect(url_for('static_pages.products'))
    else:
        return jsonify({'error': 'Failed to create product'}), 400


@product_bp.route('/products/<int:product_id>', methods=['PUT'])
def update_product_route(product_id):
    data = request.json
    if 'name' not in data or 'price_usd' not in data:
        return jsonify({'error': 'Missing required data'}), 400

    try:
        data['price_usd'] = float(data['price_usd'])
    except ValueError:
        return jsonify({'error': 'Invalid input for price'}), 400

    updated_product = product_repo.update_product(product_id, data)
    if updated_product:
        return jsonify({'message': 'Product updated successfully'}), 200
    else:
        return jsonify({'error': 'Product not found or update failed'}), 404


@product_bp.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product_route(product_id):
    if not product_repo.delete_product(product_id):
        return jsonify({'error': 'Product not found'}), 404
    return jsonify({'message': 'Product deleted successfully'}), 200
