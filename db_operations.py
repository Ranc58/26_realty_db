import os

import argparse
import requests
from flask_init import db
from models import Flat

DB_NAME = 'flats.db'
JSON_URL = 'https://devman.org/assets/ads.json'


def create_db():
    if not os.path.exists(DB_NAME):
        db.create_all()


def get_flat_content_from_url():
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
                            ad_id=flat['id'],
                            active=True)
        session.add(flat_content)
        session.commit()


def create_parser_for_user_arguments():
    parser = argparse.ArgumentParser(description='Work with database.')
    parser.add_argument('-u', '--update',
                        action='store_const', const=True,
                        help='Update database')
    parser.add_argument('-c', '--create',
                        action='store_const', const=True,
                        help='Create new database')
    return parser.parse_args()


if __name__ == '__main__':
    user_argument = create_parser_for_user_arguments()
    if user_argument.create:
        create_db()
    if user_argument.update:
        all_flats = Flat.query.all()
        for flat in all_flats:
            flat.active = False
        json_content = get_flat_content_from_url()
        add_flat_content_to_db(json_content)
