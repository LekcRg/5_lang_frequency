import argparse
from collections import Counter


def load_data(path_to_file):
    with open(path_to_file, 'r', encoding='utf-8') as file:
        return file.read()


def get_clean_words(txt_data):
    clean_text = ""
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" \
              "абвгдеёжзийклмнопрстуфхцчшщъыьэюя" \
              "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ "
    for symbol in txt_data:
        for letter in letters:
            if letter == symbol:
                clean_text += letter
    words = clean_text.lower().split()
    return words


def get_most_frequent_words(text):
    words = get_clean_words(text)
    number_frequent_words = 10
    return Counter(words).most_common(number_frequent_words)


def add_parser():
    new_parser = argparse.ArgumentParser()
    new_parser.add_argument('data', help='path to file')
    return new_parser.parse_args()


if __name__ == '__main__':
    args = add_parser()
    counter = 1
    frequent_words = get_most_frequent_words(load_data(args.data))
    print("Most frequent words in {}:".format(args.data))
    for word in frequent_words:
        print("{number}. {word} (occurs {count} times)"
              .format(number=counter, word=word[0].title(), count=word[1]))
        counter += 1
