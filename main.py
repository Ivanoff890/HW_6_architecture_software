import requests
from typing import Dict


def get_text(url: str) -> str:
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def count_word_frequencies(text: str, words_to_count: set) -> Dict[str, int]:
    all_words = text.split()
    frequencies = {word: 0 for word in words_to_count}

    for w in all_words:
        if w in words_to_count:
            frequencies[w] += 1

    return frequencies


def load_words_from_file(filename: str) -> set:
    with open(filename, 'r') as file:
        return {line.strip() for line in file if line.strip()}


def main():
    words_file = "words.txt"
    url = "https://eng.mipt.ru/why-mipt/"

    words_to_count = load_words_from_file(words_file)
    text = get_text(url)
    frequencies = count_word_frequencies(text, words_to_count)

    print(frequencies)


if __name__ == "__main__":
    main()