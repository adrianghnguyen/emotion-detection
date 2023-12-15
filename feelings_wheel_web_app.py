from flask import *

app = Flask(__name__)

def test_function():
    print("I am executing a test function")
    result = "test function result"

    return result


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        print(request.form["input_text"])
        text = request.form['input_text']
        return redirect(f"/process/{text}")

    return render_template("index.html")

@app.route("/process/<text>")
def process(text):
    result = test_function()

    return render_template("processed_text.html", result=result, input_text=text)
    # return f"You sent \"{text}\" to be processed"


if __name__ == "__main__":
    app.run()
