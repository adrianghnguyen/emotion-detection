from transformers import pipeline

class DecodedEmotion:
    def __init__(self, input_sentence):
        self.input_text = input_sentence
        self.raw_scores_dict = self.score_for_emotions(self.input_text)
        self.acceptable_score_threshold = 0.1 # Default value
        self.filtered_scores = None

    def score_for_emotions(self, input_text):
        print("Running emotion classifier")
        classifier = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None)
        model_outputs_results = classifier(input_text)

        return model_outputs_results[0] # Set to 0 to flatten

    def display_input(self):
        print(f'Input sentence: {self.input_text}')

    def display_raw_scores(self):
        for score in self.raw_scores_dict:
            print(score)

    def modify_score_threshold(self, new_acceptable_score):
        self.acceptable_score_threshold = new_acceptable_score

    # Get rid of emotions which don't pass a certain value
    def filter_scores(self):
        # TODO: On second thought, this would've been better added as a value within the dictionary as a new
        #  key-value pair such as {passable_score : True/False}
        filtered_list = [item for item in self.raw_scores_dict if item['score'] > self.acceptable_score_threshold] # Using dict comprehension.

        self.filtered_scores = filtered_list

    def print_filtered_scores(self):

        print('Printing out the filtered scores')

        if self.filtered_scores is None:
            print('Scores not filtered')
        else:
            for filtered_score in self.filtered_scores:
                print(filtered_score)

    def add_label_definitions(self):
        emotions_dict = {
            'admiration': "Finding something impressive or worthy of respect",
            'amusement': "Finding something funny or being entertained",
            'anger': "A strong feeling of displeasure or antagonism",
            'annoyance': "Mild anger, irritation",
            'approval': "Having or expressing a favorable opinion",
            'caring': "Displaying kindness and concern for others",
            'confusion': "Lack of understanding, uncertainty",
            'curiosity': "A strong desire to know or learn something",
            'desire': "A strong feeling of wanting something or wishing for something to happen",
            'disappointment': "Sadness or displeasure caused by the nonfulfillment of one’s hopes or expectations",
            'disapproval': "Having or expressing an unfavorable opinion",
            'disgust': "Revulsion or strong disapproval aroused by something unpleasant or offensive",
            'embarrassment': "Self-consciousness, shame, or awkwardness",
            'excitement': "Feeling of great enthusiasm and eagerness",
            'fear': "Being afraid or worried",
            'gratitude': "A feeling of thankfulness and appreciation",
            'grief': "Intense sorrow, especially caused by someone’s death",
            'joy': "A feeling of pleasure and happiness",
            'love': "A strong positive emotion of regard and affection",
            'nervousness': "Apprehension, worry, anxiety",
            'optimism': "Hopefulness and confidence about the future or the success of something",
            'pride': "Pleasure or satisfaction due to one's own achievements or the achievements of those with whom one is closely associated",
            'realization': "Becoming aware of something",
            'relief': "Reassurance and relaxation following release from anxiety or distress",
            'remorse': "Regret or guilty feeling",
            'sadness': "Emotional pain, sorrow",
            'surprise': "Feeling astonished, startled by something unexpected"
        }

        for result in self.raw_scores_dict:
            if result['label'] in emotions_dict:
                emotion_name = result['label']
                emotion_definition = emotions_dict.get(emotion_name)
                result['label_definition'] = emotion_definition

    def print_relevant_emotions(self): # This function can be used to display the final result in the web version? Could be modified accordingly.
        print(f'Original text: {self.input_text}')
        print(f'Acceptable score threshold is set to >{self.acceptable_score_threshold}')
        print("===========================")
        for emotion_detected in self.filtered_scores:
            print(f'{emotion_detected.get("label").title()} ({emotion_detected.get("label_definition")[:-1]}) detected with score {round(emotion_detected.get("score"),3)}')

def main():
    # input_text = input("Enter the text which needs to be decoded for emotions: ")
    input_text = [
        "I just feel mentally exhausted you know. I don't even know why I am tired in the first place and what's weighing me down. And because of that, I feel like I've lost progress on the last few weeks. I was mainly lying down in bed, suffering, but I can't even tell what. I guess it weighs on me to not feel like I have made more progress - is that being fair to myself?",
        'This can serve as the basic and the most simple template. This can get more and more complex as you add conditionalities to it.',
        'Love, love, love how Dad washed his hands first before picking up his son!',
        "She isn't fun anymore, she refuses to cut loose and drink more than a single drink or ever smoke weed with me even when the kids are at grandparents for the night. Sex is getting boring, she has no fantasies what so ever and I'm pretty sure she hasn't masturbated in years",
        'Everything about my wife is just bland now. She gets more excited talking about her job than I see her excited about anything we do together. You get her talking about her job and she can literally talk for hours. My job to me is purely a means to make money so we can afford things and do fun things so hearing about another person\'s job is like listening to a lecture on the step by step process of paint drying.',
        "I just feel mentally exhausted you know. I don't even know why I am tired in the first place and what's weighing me down. And because of that, I feel like I've lost progress on the last few weeks. I was mainly lying down in bed, suffering, but I can't even tell what. I guess it weighs on me to not feel like I have made more progress - is that being fair to myself?"]
    # results = process_emotions(input_text)
    #
    # filtered_results = filter_model_results(results, acceptable_score_threshold=0.25)
    # # print(*filtered_results, sep='\n')
    #
    # print_results_definitions(filtered_results)

    test_sentence = "I just feel mentally exhausted you know. I don't even know why I am tired in the first place and what's weighing me down. And because of that, I feel like I've lost progress on the last few weeks. I was mainly lying down in bed, suffering, but I can't even tell what. I guess it weighs on me to not feel like I have made more progress - is that being fair to myself?"

    # decoded_sentence = DecodedEmotion(test_sentence)
    decoded_sentence = DecodedEmotion(input_text[0])
    decoded_sentence.add_label_definitions() # TODO: Incorporate into the class behavior itself?
    decoded_sentence.filter_scores()
    decoded_sentence.print_relevant_emotions()

if __name__ == "__main__":
    main()
