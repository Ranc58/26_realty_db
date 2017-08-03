import os
import json
from flask import Flask, render_template, session, request
from flask_sqlalchemy import SQLAlchemy
from models import Flat
from db_init import app, db


@app.route('/<int:page>')  # TODO Change URL
def ads_list(page=1):
    per_page = 15
    district = request.args.get('oblast_district')
    min_price = request.args.get('min_price')
    max_price = request.args.get('max_price')
    ads = Flat.query.filter_by(active=True)
    if district:
        ads = ads.filter_by(oblast_district=district)
    if min_price:
        ads = ads.filter(Flat.price >= min_price)
    if max_price:
        ads = ads.filter(Flat.price <= max_price)
    ads = ads.paginate(page, per_page, error_out=False).items
    return render_template('ads_list.html', ads=ads)


@app.route('/search')  # TODO Add individual URL for results or del it
def filtred_ads():
    pass


if __name__ == "__main__":  # TODO add page listing in html template
    app.run()
