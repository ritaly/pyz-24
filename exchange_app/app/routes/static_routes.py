#extracted static routes for cleanup

from flask import Blueprint, send_from_directory

static_bp = Blueprint('static_pages', __name__)


@static_bp.route('/')
def home():
    return send_from_directory('UI', 'index.html')


@static_bp.route('/products')
def products():
    return send_from_directory('UI', 'list_products.html')


@static_bp.route('/edit-product/<int:product_id>')
def edit_product(product_id):
    return send_from_directory('UI', 'edit_product.html')
