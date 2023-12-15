from flask import *

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        print(request.form["input_text"])

    return render_template("index.html")


if __name__ == "__main__":
    app.run()
