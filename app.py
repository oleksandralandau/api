from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("currency_converter.html", code=11)


if __name__ == "__main__":
    app.run(debug=True)

