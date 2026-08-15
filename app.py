from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods = ["POST", "GET"])
def home():

    hero_name = None

    if request.method == "POST":

        hero_name = request.form["hero_name"]

    return render_template("hero_creator.html", hero_name=hero_name)

@app.route("/heroes")
def heroes():

    heroes = [
        "Arshdeep",
        "Luna",
        "Shadow"
    ]

    return render_template("heroes.html", heroes=heroes)


@app.route("/quests")
def quests():
    return render_template("quests.html")

@app.route("/something")
def something():
    return render_template("something.html")


if __name__ == "__main__":
    app.run(debug=True)