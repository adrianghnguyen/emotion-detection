from flask import *
from old.minimal_feelings import DecodedEmotion
import re

app = Flask(__name__)
testing = False

def clean_input(raw_text):
    clean_header = re.sub(r'[\r\n]', '', raw_text)
    print(f'Sanitized text: {clean_header}')
    return clean_header

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # print(request.form["input_text"])
        input_text = request.form['input_text']
        print(f'Received the following input text: {input_text}')

        if testing:
            input_text = ("So I met a girl through bumble, she and I had an amazing vibe. I really liked her but in the "
                          "long run, I was planning to go to Yale for my masters and she decided to stay in India. For "
                          "three months I treated her with outmost respect, love and care. I honestly tried to be there "
                          "for her always. Before dating me she was in a very toxic relationship and her ex was very "
                          "abusive. She kinda started seeing a few guys after that ex, and she started seeing her "
                          "classmate who apparently at that time only wanted a causal relationship. So she denied it to "
                          "him. After a few days she met me. And I became her best friend for three months. I tried to be "
                          "a realistic person with her, always gave her space and respected boundaries. So I went back "
                          "home after three months of situationship and apparently she made out with the guy who just "
                          "wanted casual. So next day she broke up with me telling me it was my fault. Later she told me "
                          "that she fucked up and I forgave her and tried to fix things. She told me she loves me and she "
                          "would never be with the other guy who is his classmate. Today I saw them together after "
                          "college and she saw me. I texted her I was a standby for you, I hope you find your happiness "
                          "and thanks for everything. She said I hope the same for you. So yeah, fuck her.") # TODO: Remove this hard-coded value after testing



        return redirect(f"/process/{clean_input(input_text)}")

    return render_template("index.html")

@app.route("/process/<text>")
def process_emotion(text):

    user_emotion = DecodedEmotion(input_sentence=text) # More descriptive variable name needed?
    user_emotion.add_label_definitions() # FUCKING SPAGHETTITTITITITITI
    user_emotion.filter_scores() # Get rid of this into the class behavior. The class should have everything packed in.
    emotion_results = user_emotion.filtered_scores
    filtering_threshold = getattr(user_emotion, 'acceptable_score_threshold')
    print(emotion_results)

    return render_template("processed_text.html", emotion_results=emotion_results, input_text=text, filtering_threshold=filtering_threshold)


if __name__ == "__main__":
    app.run()
