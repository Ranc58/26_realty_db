import os
import argparse
import json
from sqlalchemy.exc import IntegrityError

from models import Flat
from server import db

DB_NAME = 'flats.db'

def create_db():
    if not os.path.exists(DB_NAME):
        db.create_all()


def get_flat_content_from_json(json_file):
    return json.load(json_file)


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
        session.close()


def create_parser_for_user_arguments():
    parser = argparse.ArgumentParser(description='Work with database.')
    parser.add_argument('-u', '--update', required=True,
                        type=argparse.FileType(mode='r'),
                        help='Update database')
    return parser.parse_args()


if __name__ == '__main__':
    user_argument = create_parser_for_user_arguments()
    create_db()
    try:
        json_content = get_flat_content_from_json(user_argument.update)
        active_ads = Flat.query.filter_by(active=True)
        active_ads.update(dict(active=False))
        add_flat_content_to_db(json_content)
    except json.decoder.JSONDecodeError as e:
        print('Please check that JSON file have correct structure!\n', e)
    except IntegrityError:
        print('Error! Please check ads for unique!\nUpdate canceled.')
        db.session.rollback()
    except KeyError as e:
        print('Error! This value is missing:', e,
              '\nCheck JSON file for data integrity \nUpdate canceled.')
        db.session.rollback()
    db.session.close()
