from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Flat(db.Model):
    ad_id = db.Column(db.Integer, primary_key=True)
    settlement = db.Column(db.String(64))
    under_construction = db.Column(db.Boolean)
    description = db.Column(db.Text)
    price = db.Column(db.Integer)
    oblast_district = db.Column(db.String(128))
    living_area = db.Column(db.Float)
    has_balcony = db.Column(db.Boolean)
    address = db.Column(db.String(128))
    construction_year = db.Column(db.Integer)
    rooms_number = db.Column(db.Integer)
    premise_area = db.Column(db.Float)
    active = db.Column(db.Boolean)
