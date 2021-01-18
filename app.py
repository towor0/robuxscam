from flask import render_template, Flask

app = Flask("__name__")

@app.route("/")
def start():
    return render_template("index.html")

@app.route("/generator")
def generate():
    return render_template("scam.html")

@app.route("/report")
def report():
    return render_template("report.html")
    