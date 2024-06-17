
from datetime import datetime

from ..database import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    price_usd = db.Column(db.Float, nullable=False)
    price_pln = db.Column(db.Float)
    last_updated = db.Column(db.DateTime, default=datetime.utcnow())
    source = db.Column(db.String(30), nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price_usd': self.price_usd,
            'price_pln': self.price_pln,
            'last_updated': self.last_updated.isoformat() if self.last_updated else None,
            'source': self.source
        }