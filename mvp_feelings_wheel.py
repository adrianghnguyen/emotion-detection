import csv
from transformers import pipeline


def receive_console_input():
    """
    Receives the text which the user wishes to submit for processing
    :return:
    """
    input_text = input("Enter the text which needs to be decoded for emotions: ")
    return input_text


def process_emotion(text):
    """
    Sets up the emotion decoding model then parses it for emotions
    :return:
    """
    print("Running emotion classifier")
    classifier = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None)
    model_outputs_results = classifier(text)

    return model_outputs_results[0] # Set to 0 so it only results a flat list - otherwise it's nested TODO: Look for more elegant solution


def get_emotion_definitions():
    dict_emotion = {}
    filepath = 'emotion_definition.csv'

    # Retrieves emotion taxonomy definition from GoEmotions paper used in the classifier model
    with open(file=filepath, mode='r') as file:
        reader = csv.DictReader(file)
        print(f"Grabbing emotion definitions from {filepath}")

        for row in reader:
            key = row['emotion']
            value = row['definition']

            dict_emotion[key] = value

    # Testing the returned values from the CSV
    test_dict_emotions = {'admiration': "Finding something impressive or worthy of respect.",
        'amusement': "Finding something funny or being entertained."}

    assert dict_emotion.get("admiration") == test_dict_emotions.get(
        "admiration"), "Imported CSV should match GoEmotions taxonomy definitiions"

    return dict_emotion


def output_results(emotion_scores, emotion_definition, threshold):
    """
    :param model_results: results from the GoEmotions classifier transformer
    :param emotion_definition: dictionary of definitions for the associated label
    :param threshold: the required score before outputting a specific result
    :return:
    """

    accepted_score_emotions = []

    # Only return the emotion scores which pass a significant value
    for label in emotion_scores:
        if threshold <= label.get('score'):
            accepted_score_emotions.append(label)

    print(f"Labels which passed threshold of {threshold}", accepted_score_emotions)

    # Add definition entry into the dictionary of the label
    for item in accepted_score_emotions:

        emotion_name = item.get('label')
        item['definition'] = emotion_definition[emotion_name]



def test_output_results():

    sample_model_results = [{'label': 'caring', 'score': 0.82}, {'label': 'approval', 'score': 0.15}, {'label': 'admiration', 'score': 0.008}]
    sample_threshold = 0.5
    sample_definitions = {'caring': 'ya care', 'approval': 'nice job - approved'}

    output_results(sample_model_results, sample_definitions,sample_threshold)

def test_sample_decode_text():
    sample_text = ("For me, it really helped me understand that he cared and even though he's a man of few words, "
                   "he does deeply care about our well-being.")

    result = process_emotion(sample_text)

    print(*result, sep='\n')

def main():
    dict_emotion = get_emotion_definitions()

    raw_text = receive_console_input()
    process_emotion(raw_text)

    # test_sample_decode_text()
    # test_output_results()


if __name__ == "__main__":
    main()
