from ..models.product import Product
import pandas as pd


class ProductRepository:
    def __init__(self, db, convert_currency):
        self.db = db
        self.convert_currency = convert_currency

    @staticmethod
    def get_all_products():
        return Product.query.all()

    def create_product(self, name, price_usd, source):
        if not name or not price_usd:
            return None
        price_usd = float(price_usd)
        price_pln = self.convert_currency(price_usd)
        new_product = Product(name=name, price_usd=price_usd, price_pln=price_pln, source=source)
        self.db.session.add(new_product)
        self.db.session.commit()
        return new_product

    def update_product(self, product_id, data):
        product = self.get_product(product_id)
        if not product:
            return None

        if 'price_usd' in data:
            product.price_usd = float(data['price_usd'])
            product.price_pln = self.convert_currency(product.price_usd)

        product.name = data.get('name', product.name)
        product.last_updated = data.get('last_updated', product.last_updated)
        product.source = data.get('source', product.source)

        self.db.session.commit()
        return product

    def delete_product(self, product_id):
        product = self.get_product(product_id)
        if not product:
            return None
        self.db.session.delete(product)
        self.db.session.commit()
        return True

    @staticmethod
    def get_product(product_id):
        return Product.query.get(product_id)

    def load_products_from_csv(self, file_path):
        data = pd.read_csv(file_path)
        for _, row in data.iterrows():
            self.create_product(
                name=row['name'],
                price_usd=row['price_usd'],
                source=row.get('source', 'Unknown')
            )
""" csv format:
name,price_usd,source
Product 1,10.99,Source A
Product 2,15.49,Source B
Product 3,8.99,
Product 4,12.75,Source D
"""