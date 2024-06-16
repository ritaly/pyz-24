from ..models.product import Product
import pandas as pd

class ProductRepository:
    def __init__(self, db):
        self.db = db

    def get_all_products(self):
        return Product.query.all()

    def create_product(self, name, price_usd, price_pln, source):
        if not name or not price_usd:
            return None
        new_product = Product(name=name, price_usd=price_usd, price_pln=price_pln, source=source)
        self.db.session.add(new_product)
        self.db.session.commit()
        return new_product

    def update_product(self, product_id, name, price_usd, price_pln, last_updated, source):
        product = self.get_product(product_id)
        if not product:
            return None
        product.name = name
        product.price_usd = price_usd
        product.price_pln = price_pln
        product.last_updated = last_updated
        product.source = source
        self.db.session.commit()
        return product

    def delete_product(self, product_id):
        product = self.get_product(product_id)
        if not product:
            return None
        self.db.session.delete(product)
        self.db.session.commit()

    @staticmethod
    def get_product(product_id):
        return Product.query.get(product_id)

