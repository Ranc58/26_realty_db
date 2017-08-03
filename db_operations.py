import os

import argparse
import requests
from db_init import db
from models import Flat

DB_NAME = 'flats_content.db'


JSON_URL = 'https://devman.org/assets/ads.json'


def create_db():
    if not os.path.exists(DB_NAME):
        db.create_all()


def get_content_from_file():  # TODO Add load content from file
    pass


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
                            id=flat['id'],
                            active=True)
        session.add(flat_content)
        session.commit()


def create_parser_for_user_arguments(): # TODO Total refactor of argparse
    parser = argparse.ArgumentParser(description='Work with database.')
    subparsers = parser.add_subparsers(title='subcommands',
                                       description='valid subcommands')
    url_parser = subparsers.add_parser('url_update')
    file_parser = subparsers.add_parser('file_update')
    create_db_parser = subparsers.add_parser('create_db')
    url_parser.add_argument('-u',
                            help='Load json from URL',
                            action='store_const', const=True,
                            default='https://devman.org/assets/ads.json')
    file_parser.add_argument('-f',
                             help='path to file', type=argparse.FileType())
    create_db_parser.add_argument('-c',
                                  action='store_const', const=True,
                                  help='Create new database')
    return parser.parse_args()


if __name__ == '__main__':  # TODO add argparse for load content choice
    user_argument = create_parser_for_user_arguments()
    print(user_argument)
    if user_argument == 'url_update':
        json_content = get_flat_content_from_url()
        add_flat_content_to_db(json_content)
    #elif user_argument == 'file_update':
    #
    #else:
    #    create_db()
    #all_flats = Flat.query.all()
    #for flat in all_flats:
    #    flat.active = False

