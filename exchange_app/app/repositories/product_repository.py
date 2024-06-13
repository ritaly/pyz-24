from ..database import db
from ..models.product import Product


class ProductRepository:
    @staticmethod
    def get_all_products():
        return Product.query.all()


    @staticmethod
    def create_product(name, price_usd, price_pln, source):
        if not name or not price_usd:
            return None
        new_product = Product(name=name, price_usd=price_usd, price_pln=price_pln, source=source)
        db.session.add(new_product)
        db.session.commit()


    def update_product(self, product_id, name, price_usd, price_pln, last_update, source):
        if not name or not price_usd:
            return None
        product = self.get_product(product_id)
        product.name = name
        product.price_usd = price_usd
        product.price_pln = price_pln
        product.last_updated = last_update
        product.source = source
        db.session.commit()


    def delete_product(self, product_id):
        product = self.get_product(product_id)
        if not product:
            return None
        db.session.delete(product)
        db.session.commit()


    @staticmethod
    def get_product(product_id):
        return Product.query.get(product_id)


    # def load_product(self, ):
    ###
    # load products from csv