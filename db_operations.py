import os
import requests
from db_init import db
from models import Flat

DB_NAME = 'flats_content.db'
JSON_URL = 'https://devman.org/assets/ads.json'


def create_db():
    if not os.path.exists(DB_NAME):
        db.create_all()


def get_flat_content():
    json_content = requests.get(JSON_URL).json()
    return json_content


def add_flat_content_to_db(json_content):
    for flat in json_content:
        session = db.session
        flat_content = Flat(settlement=flat['settlement'],
                            under_construction=flat['under_construction'],
                            description=flat['description'],
                            price=flat['price'],
                            oblast_district=flat['oblast_district'],
                            living_area=flat['living_area'],
                            has_balcony=flat['has_balcony'],
                            address=flat['address'],
                            construction_year=flat['construction_year'],
                            rooms_number=flat['rooms_number'],
                            premise_area=flat['premise_area'],
                            id=flat['id'])
        session.add(flat_content)
        session.commit()


if __name__ == '__main__':
    create_db()
    json_content = get_flat_content()
    add_flat_content_to_db(json_content)
