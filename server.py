import os
import json
from flask import Flask, render_template, session, request
from flask_sqlalchemy import SQLAlchemy
from models import Flat
from db_init import app, db


@app.route('/<int:page>')
def ads_list(page=1):
    per_page = 15
    district = request.args.get('oblast_district')
    #min_price = request.args.get('min_price')
    #max_price = request.args.get('max_price')
    if district:
        ads = (Flat.query.paginate(page, per_page, error_out=False))
    else:
        ads = Flat.query.order_by(Flat.id.desc()).paginate(page, per_page, error_out=False)
    # ads = Flat.query.filter_by(oblast_district = "Грязовецкий район").paginate(page, per_page, error_out=False)
    return render_template('ads_list.html', ads=ads.items)


@app.route('/search')
def filtred_ads():
    pass


if __name__ == "__main__":
    app.run()
