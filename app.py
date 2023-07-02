# lets build this app

from flask import render_template, Flask

html_code = """index.html"""

database = {"number": 0}

app = Flask(__name__)


@app.route("/")
def home():
    return render_template(html_code, number="0")


@app.route("/increment")
def increment():
    database["number"] += 1
    return render_template(html_code, number=str(database["number"]))


@app.route("/decrement")
def decrement():
    if database["number"] == 0:
        database["number"] = 0

    else:
        database["number"] -= 1

    return render_template(html_code, number=str(database["number"]))


@app.route("/reset")
def reset():
    database["number"] = 0
    return render_template(html_code, number="0")


if __name__ == "__main__":
    app.run()
