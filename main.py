from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about-me")
def about():
    name = "Domen Oslaj"
    age = 30
    address = "Filovci 45, 9222 Bogojina, Slovenia"

    best_friends = ["Miha, Luka, Grega, Lolek, Bolek"]

    return render_template("about.html", name=name, age=age, address=address, best_friends=best_friends)


if __name__ == "__main__":
    app.run(debug=True, port=5001)

