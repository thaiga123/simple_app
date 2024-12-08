from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("home.html")

@app.route("/continue")
def continue_():
    return render_template("next_page.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)