from flask import Blueprint
from app.repositories.product_repository import get_all_products

product_bp = Blueprint('products', __name__)

@product_bp.route('/', methods=['GET'])
def list_products():
    products = get_all_products()
    #return products jako json
    pass

product_bp.route('/', method=['POST'])
def create_product():
    # przyjdą dane
    # sprawdź cenę po przekonwertowaniu
    # create_product(... te dane )
    # return 201 i added successfuly
    pass
