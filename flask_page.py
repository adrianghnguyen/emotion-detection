from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    return render_template('index.html')

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    return render_template('greeting.html', say=request.form['say'], to=request.form['to'])

@app.route('/processed_emotion', methods=['GET', 'POST'])
def processed_emotion():
    return render_template('processed_text.html', input_text=request.form['input_text'])

if __name__ == "__main__":
    app.run()