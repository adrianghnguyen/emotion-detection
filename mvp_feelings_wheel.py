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
    classifier = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None)
    model_outputs_results = classifier(text)

    return model_outputs_results


def get_emotion_definitions():
    dict_emotion = {}

    with open(file='emotion_definition.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            key = row['emotion']
            value = row['definition']

            dict_emotion[key] = value

    # Testing the returned values from the CSV
    test_dict_emotions = {
        'admiration': "Finding something impressive or worthy of respect.",
        'amusement': "Finding something funny or being entertained."
    }

    assert dict_emotion.get("admiration") == test_dict_emotions.get("admiration"), "Imported CSV should match GoEmotions taxonomy definitiions"

    return dict_emotion

def output_results():
    pass

def main():

    dict_emotion = get_emotion_definitions()

    print(dict_emotion)


if __name__ == "__main__":
    main()
