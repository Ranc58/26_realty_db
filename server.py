import os
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from models import Flat
from db_init import app, db


@app.route('/index/<int:page>')
def ads_list(page=1):
    per_page = 15
    ads = Flat.query.order_by(Flat.id.desc()).paginate(page, per_page, error_out=False).items
    return render_template('ads_list.html', ads=ads)

if __name__ == "__main__":
    app.run()
