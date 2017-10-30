import argparse
from collections import Counter
from string import punctuation


def load_data(path_to_file):
    with open(path_to_file, 'r', encoding='utf-8') as file:
        return file.read()


def get_clean_words(txt_data):
    text = txt_data
    all_punctuation = punctuation + "–«»…\n"
    for symbol in range(len(all_punctuation)):
        text = text.replace(all_punctuation[symbol], "")
    words = text.lower().split(" ")
    return words


def get_most_frequent_words(text):
    words = get_clean_words(text)
    most_frequent_words = []
    for most_frequent_word in Counter(words).most_common(10):
        most_frequent_words.append(most_frequent_word[0])
    return most_frequent_words


def add_parser():
    new_parser = argparse.ArgumentParser()
    new_parser.add_argument('data', help='path to file')
    return new_parser.parse_args()


if __name__ == '__main__':
    args = add_parser()
    print("Most frequent words:\n{}"
          .format(", ".join(get_most_frequent_words(load_data(args.data)))))
