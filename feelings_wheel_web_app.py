from flask import *
from minimal_feelings import DecodedEmotion

app = Flask(__name__)

def test_function():
    print("I am executing a test function")
    result = "test function result"

    return result


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        print(request.form["input_text"])
        input_text = request.form['input_text']
        input_text = 'I am feeling sad today'
        return redirect(f"/process/{input_text}")

    return render_template("index.html")

@app.route("/process/<text>")
def process_emotion(text):
    user_emotion = DecodedEmotion(input_sentence=text) # More descriptive variable name needed?

    return render_template("processed_text.html", result=user_emotion.filtered_scores, input_text=text)
    # return f"You sent \"{text}\" to be processed"


if __name__ == "__main__":
    app.run()
