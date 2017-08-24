import datetime
from flask import Flask, render_template, request
from models import Flat, db
from flask import Flask

app = Flask(__name__)
app.config.from_object('config')
db.app = app
db.init_app(app)


@app.route('/', defaults={'page': 1})
@app.route('/<int:page>')
def ads_list(page):
    per_page = 15
    district = request.args.get('oblast_district')
    min_price = request.args.get('min_price')
    max_price = request.args.get('max_price')
    new_building = request.args.get('new_building')
    ads = Flat.query.filter_by(active=True)
    if new_building:
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
