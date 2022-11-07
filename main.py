from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from forms import AddCafe
from datetime import date
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

Bootstrap(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    map_url = db.Column(db.String, nullable=False)
    img_url = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    seats = db.Column(db.String, nullable=False)
    coffee_price = db.Column(db.String, nullable=False)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/cafes")
def all_cafes():
    cafes = Cafe.query.all()

    return render_template("cafes.html", cafes=cafes)


@app.route("/add", methods=['GET', 'POST'])
def add_cafe():
    form = AddCafe()

    if form.cancel.data:
        return redirect(url_for('all_cafes'))
    elif form.validate_on_submit():
        data = Cafe(
            name=form.name.data,
            map_url=form.map_url.data,
            img_url=form.img_url.data,
            location=form.location.data,
            has_sockets=int(form.has_sockets.data),
            has_toilet=int(form.has_toilet.data),
            has_wifi=int(form.has_wifi.data),
            can_take_calls=int(form.can_take_calls.data),
            seats=form.seats.data,
            coffee_price=form.coffee_price.data,
        )
        db.session.add(data)
        db.session.commit()
        return redirect(url_for("all_cafes"))

    return render_template("add_cafe.html", form=form)


@app.route("/edit/<int:cafe_id>", methods=['GET', 'POST'])
def edit_cafe(cafe_id):
    cafe = Cafe.query.get(cafe_id)

    form = AddCafe(name=cafe.name,
                   map_url=cafe.map_url,
                   img_url=cafe.img_url,
                   location=cafe.location,
                   has_sockets=int(cafe.has_sockets is True),
                   has_toilet=int(cafe.has_toilet is True),
                   has_wifi=int(cafe.has_wifi is True),
                   can_take_calls=int(cafe.can_take_calls is True),
                   seats=cafe.seats,
                   coffee_price=cafe.coffee_price
                   )

    if form.cancel.data:
        return redirect(url_for('all_cafes'))
    elif form.validate_on_submit():
        cafe.name = form.name.data,
        cafe.map_url = form.map_url.data,
        cafe.img_url = form.img_url.data,
        cafe.location = form.location.data,
        cafe.has_sockets = form.has_sockets.data,
        cafe.has_toilet = form.has_toilet.data,
        cafe.has_wifi = form.has_wifi.data,
        cafe.can_take_calls = form.can_take_calls.data,
        cafe.seats = form.seats.data,
        cafe.coffee_price = form.coffee_price.data
        db.session.commit()

        return redirect(url_for("all_cafes"))

    return render_template("add_cafe.html", form=form, cafe_id=cafe_id)


@app.route("/delete/<int:cafe_id>")
def delete_cafe(cafe_id):
    cafe = Cafe.query.get(cafe_id)
    db.session.delete(cafe)
    db.session.commit()
    return redirect(url_for('all_cafes'))


@app.context_processor
def inject_copyright():
    return {"year": date.today().year}


if __name__ == "__main__":
    app.run()
