from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    hero_name = None

    if request.method == "POST":
        hero_name = request.form.get("hero_name")

    return render_template(
        "home.html",
        hero_name=hero_name
    )


if __name__ == "__main__":
    app.run(debug=True)