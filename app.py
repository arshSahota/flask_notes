from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/heroes")
def heroes():
    return render_template("heroes.html")


@app.route("/quests")
def quests():
    return render_template("quests.html")


if __name__ == "__main__":
    app.run(debug=True)