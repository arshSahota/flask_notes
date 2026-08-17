from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///heroes.db"

db = SQLAlchemy(app)

class Hero(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False )

with app.app_context():
    db.create_all()

    """
    This tells SQLAlchemy to create any tables described by your models"""

@app.route("/", methods = ["GET", "POST"])

def heroes():
    if request.method == "POST":
        hero_name = request.form.get("hero_name")

        if hero_name:
            new_hero = Hero(name=hero_name)

            db.session.add(new_hero)
            db.session.commit()

            return redirect(url_for("heroes"))

        """
        redirect sends the user to another route
        go to heroes page
        instead of redirect("/")
        Flask developers usually write 
        redirect(url_for("heroes")) ==> because thats the function name
        Flask finds the url automatically and this is safer when URL changes later
        """

    all_heroes = Hero.query.all()

    return render_template(
        "heroes.html",
        heroes=all_heroes
                )

"""
what happens when the form is submitted??
Ans: so HTML input is read
a new Hero Python object is created
db.session.add(new_hero) prepares it for insertion
db.session.commit() --> permanenty saves it

all_heroes = Hero.query.all()
Finally, the list is sent to the template
"""

if __name__ == "__main__":
    app.run(debug=True)

"""
usual pattern

POST ==> SAVE DATA ==> REDIRECT ==> GET"""