import os
import json
import datetime
from flask import Flask, render_template, session, request
from flask_sqlalchemy import SQLAlchemy
from models import Flat
from flask_init import app, db


@app.route('/ads_list/<int:page>')
def ads_list(page=1):
    per_page = 15
    district = request.args.get('oblast_district')
    min_price = request.args.get('min_price')
    max_price = request.args.get('max_price')
    new_building = request.args.get('new_building')
    ads = Flat.query.filter_by(active=True)
    if new_building:  # TODO Fix NULL
        now_year = datetime.date.today().year
        max_year_difference = 2
        new_building_check = now_year - Flat.construction_year
        ads = ads.filter(new_building_check <= max_year_difference)
    if district:
        ads = ads.filter_by(oblast_district=district)
    if min_price:
        ads = ads.filter(Flat.price >= min_price)
    if max_price:
        ads = ads.filter(Flat.price <= max_price)
    ads = ads.paginate(page, per_page, error_out=False)
    return render_template('ads_list.html', ads=ads)


if __name__ == "__main__":
    app.run()
