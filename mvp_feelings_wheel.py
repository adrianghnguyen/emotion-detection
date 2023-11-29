from transformers import pipeline
from icecream import ic
import csv


def receive_console_input():
    """
    Receives the text which the user wishes to submit for processing
    :return:
    """

    input_text = input("Enter the text which needs to be decoded for emotions: ")
    return input_text


def process_emotion(text):
    # Sets up the emotion decoding model then parses it for emotions
    classifier = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None)
    model_outputs_results = classifier(text)

    return model_outputs_results


def output_results():
    pass


def parse_emotion_dictionary():
    """
    Reads a csv which contains labeled emotions, the desired display label
    and its associated definition and places it into a dictionary
    :return dict_emotion_defs:
    """

    csv_filename = 'emotion_definition.csv'

    with open(csv_filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row)


def main():
    dict_emotions = parse_emotion_dictionary()


if __name__ == "__main__":
    main()
