from flask import Flask, redirect, url_for

app = Flask(__name__) # What does this do?

@app.route("/")
def home():
    return 'Howdy this is some text for a hello world</a>'

@app.route("/input/<input_text>")
def print_input(input_text):
    return f"Here is the input text: {input_text}"

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

@app.route("/joke")
def say_joke():
    return "Farts"

if __name__ == "__main__":
    app.run()