from transformers import pipeline
from icecream import ic
import pyperclip as clipboard
import random


def classify_emotion(text):
    classifier = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None)
    model_outputs = classifier(text)

    return model_outputs


def receive_console_input():
    input("Copy the text you wish to decode into the clipboard now then hit ANY key")
    data = clipboard.paste()

    return data


def process_emotions_zipped(input_text):
    """
    Transformers process emotions in sequence so we can map the input list to the output list in sequence.
    The goal is to create a tuple of (input, output)
    :param input_text: list of strings to be decoded for emotions
    :return: associated input strings and their decoded values
    """

    decoded_emotions = classify_emotion(input_text)

    if isinstance(input_text, list): # Passing in multiple lines to be decoded
        zipped_result = list(zip(input_text, decoded_emotions))
    elif isinstance(input_text, str): # Passed in a single line to be decoded
        zipped_result = [input_text, decoded_emotions]

    return zipped_result


def testing_input_order():
    """
    Trying to see if the returned output of the transformer is sequential.
    Expecting input order to map directly to output sequence order

    :return:
    """
    test_string_emotion = "It's insane how stupid these people are."
    test_multi_list = ["It's insane how stupid these people are.", "We wear the mask that grins and lies, It hides "
                                                                   "our cheeks and shades our eyes,— This debt we pay "
                                                                   "to human guile; With torn and bleeding hearts we "
                                                                   "smile, And mouth with myriad subtleties.", "I have "
                                                                                                               "never "
                                                                                                               "felt "
                                                                                                               "more "
                                                                                                               "satisfied than today. I feel incredibly happy"]

    result = classify_emotion(test_multi_list)
    zipped_result = list(zip(test_multi_list, result))

    print("Original result")
    ic(zipped_result)

    print("Shuffled - maintained order?")
    random.shuffle(test_multi_list)
    shuffled_results = classify_emotion(test_multi_list)
    shuffled_zipped_result = list(zip(test_multi_list, shuffled_results))
    ic(shuffled_zipped_result)


def main():
    # testing_input_order()

    console_input = receive_console_input()
    print(f"Received input: {console_input}")
    results = process_emotions_zipped(console_input)
    ic(results[1])


if __name__ == "__main__":
    main()
