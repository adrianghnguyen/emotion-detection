from transformers import pipeline



def process_emotions(text):
    print("Running emotion classifier")
    classifier = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None)
    model_outputs_results = classifier(text)
    results = [{'input_text': text, 'scores': scores} for text, scores in zip(text, model_outputs_results)]

    return results


def filter_model_results(results, acceptable_score_threshold):
    filtered_results = []

    # Only keep the model results which pass a certain value
    for item in results:
        original_scores_list = item['scores']
        temp_list = []
        for label in original_scores_list:
            if label['score'] > acceptable_score_threshold:
                temp_list.append(label)

        filtered_item = {'input_text': item['input_text'],
                         'clean_scores': temp_list,
                         'accepted_threshold': acceptable_score_threshold}
        filtered_results.append(filtered_item)

    return filtered_results

def print_results_definitions(model_results):

    emotions_dict = {
        'admiration': "Finding something impressive or worthy of respect.",
        'amusement': "Finding something funny or being entertained.",
        'anger': "A strong feeling of displeasure or antagonism.",
        'annoyance': "Mild anger, irritation.",
        'approval': "Having or expressing a favorable opinion.",
        'caring': "Displaying kindness and concern for others.",
        'confusion': "Lack of understanding, uncertainty.",
        'curiosity': "A strong desire to know or learn something.",
        'desire': "A strong feeling of wanting something or wishing for something to happen.",
        'disappointment': "Sadness or displeasure caused by the nonfulfillment of one’s hopes or expectations.",
        'disapproval': "Having or expressing an unfavorable opinion.",
        'disgust': "Revulsion or strong disapproval aroused by something unpleasant or offensive.",
        'embarrassment': "Self-consciousness, shame, or awkwardness.",
        'excitement': "Feeling of great enthusiasm and eagerness.",
        'fear': "Being afraid or worried.",
        'gratitude': "A feeling of thankfulness and appreciation.",
        'grief': "Intense sorrow, especially caused by someone’s death.",
        'joy': "A feeling of pleasure and happiness.",
        'love': "A strong positive emotion of regard and affection.",
        'nervousness': "Apprehension, worry, anxiety.",
        'optimism': "Hopefulness and confidence about the future or the success of something.",
        'pride': "Pleasure or satisfaction due to one's own achievements or the achievements of those with whom one is closely associated.",
        'realization': "Becoming aware of something.",
        'relief': "Reassurance and relaxation following release from anxiety or distress.",
        'remorse': "Regret or guilty feeling.",
        'sadness': "Emotional pain, sorrow.",
        'surprise': "Feeling astonished, startled by something unexpected."
    }

    # Prints associated definition based on emotion labels found
    for item in model_results:
        scores = item['clean_scores']

        for label_item in scores:
            if label_item['label'] in emotions_dict:
                emotion_name = label_item['label']
                emotion_definition = emotions_dict.get(emotion_name)
                print(f'{emotion_name}: {emotion_definition}')


    return None

def main():
    # input_text = input("Enter the text which needs to be decoded for emotions: ")
    input_text = [
        "I just feel mentally exhausted you know. I don't even know why I am tired in the first place and what's weighing me down. And because of that, I feel like I've lost progress on the last few weeks. I was mainly lying down in bed, suffering, but I can't even tell what. I guess it weighs on me to not feel like I have made more progress - is that being fair to myself?",
        'This can serve as the basic and the most simple template. This can get more and more complex as you add conditionalities to it.',
        'Love, love, love how Dad washed his hands first before picking up his son!',
        "She isn't fun anymore, she refuses to cut loose and drink more than a single drink or ever smoke weed with me even when the kids are at grandparents for the night. Sex is getting boring, she has no fantasies what so ever and I'm pretty sure she hasn't masturbated in years",
        'Everything about my wife is just bland now. She gets more excited talking about her job than I see her excited about anything we do together. You get her talking about her job and she can literally talk for hours. My job to me is purely a means to make money so we can afford things and do fun things so hearing about another person\'s job is like listening to a lecture on the step by step process of paint drying.',
    "I just feel mentally exhausted you know. I don't even know why I am tired in the first place and what's weighing me down. And because of that, I feel like I've lost progress on the last few weeks. I was mainly lying down in bed, suffering, but I can't even tell what. I guess it weighs on me to not feel like I have made more progress - is that being fair to myself?"]
    results = process_emotions(input_text)

    filtered_results = filter_model_results(results, acceptable_score_threshold=0.25)
    # print(*filtered_results, sep='\n')

    print_results_definitions(filtered_results)


if __name__ == "__main__":
    main()
