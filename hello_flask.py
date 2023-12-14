from flask import Flask, redirect, url_for, render_template

app = Flask(__name__) # What does this do?

@app.route("/")
def home():
    return render_template("index.html") # This allows me call an index file to be rendered instead of writing the HTML directly in the return string.

@app.route("/input/<input_text>")
def print_input(input_text):
    return render_template("python_in_page.html", content=input_text)

@app.route("/admin")
def admin():
    """
    An example where going to the /admin page redirects to the home function which loads "/"
    :return:
    """
    return redirect(url_for("home"))

@app.route("/joke")
def say_joke():
    return "Farts"

if __name__ == "__main__":
    app.run()