import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from models import Flat
from db_init import app, db


@app.route('/')
def ads_list():
    flats = Flat.query.all()
    return render_template('ads_list.html', ads=flats)


if __name__ == "__main__":
    app.run()
