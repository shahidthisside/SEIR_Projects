import sys
import requests
from bs4 import BeautifulSoup


def word_hash(word):
    p = 53
    mod = 2**64
    value = 0
    power = 1

    for letter in word:
        value = (value + ord(letter) * power) % mod
        power = (power * p) % mod

    return value


def make_hash(text):

    stop_words = {
        "with", "an", "this", "of", "are", "by",
        "the", "was", "in", "that", "a", "as",
        "be", "to", "it", "on", "and", "at",
        "for", "is"
    }

    words = text.lower().split()
    counts = {}

    for word in words:
        clean = ""

        for letter in word:
            if letter.isalnum():
                clean += letter

        if clean and clean not in stop_words:
            counts[clean] = counts.get(clean, 0) + 1

    bits = [0] * 64

    for word in counts:
        number = word_hash(word)

        for i in range(64):
            if number & (1 << i):
                bits[i] += counts[word]
            else:
                bits[i] -= counts[word]

    result = 0
    for i in range(64):
        if bits[i] > 0:
            result |= (1 << i)

    return result


def get_page_hash(link):
    response = requests.get(link)
    if response.status_code != 200:
        return None

    soup = BeautifulSoup(response.text, "html.parser")
    return make_hash(soup.get_text(" "))


if __name__ == "__main__":

    if len(sys.argv) < 3:
        print("Enter two links")
    else:
        h1 = get_page_hash(sys.argv[1])
        h2 = get_page_hash(sys.argv[2])

        if h1 and h2:
            diff = bin(h1 ^ h2).count("1")
            print("Common bits:", 64 - diff)