import datetime
from flask import Flask, render_template, request
from models import Flat, db
from flask import Flask

PER_PAGE = 15

app = Flask(__name__)
app.config.from_object('config')
db.app = app
db.init_app(app)


@app.route('/')
@app.route('/<int:page>')
def search(page=1):
    oblast_district = request.args.get('oblast_district',
                                       type=str, default=None)
    min_price = request.args.get('min_price',
                                 type=int, default=None)
    max_price = request.args.get('max_price',
                                 type=int, default=None)
    new_building = request.args.get('new_building',
                                    type=bool, default=None)
    ads = Flat.query.filter_by(active=True)
    if new_building:
        now_year = datetime.date.today().year
        max_year_difference = 2
        new_building_check = now_year - Flat.construction_year
        ads = ads.filter(new_building_check <= max_year_difference)
    if oblast_district:
        ads = ads.filter_by(oblast_district=oblast_district)
    if min_price:
        ads = ads.filter(Flat.price >= min_price)
    if max_price:
        ads = ads.filter(Flat.price <= max_price)
    ads = ads.paginate(page, PER_PAGE, error_out=False)
    return render_template('ads_list.html', ads=ads,
                           min_price=min_price,
                           max_price=max_price,
                           new_building=new_building,
                           oblast_district=oblast_district,)


if __name__ == "__main__":
    app.run()
