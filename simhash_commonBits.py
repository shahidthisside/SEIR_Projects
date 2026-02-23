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

    for word, freq in counts.items():
        number = word_hash(word)

        for i in range(64):
            if number & (1 << i):
                bits[i] += freq
            else:
                bits[i] -= freq

    result = 0
    for i in range(64):
        if bits[i] > 0:
            result |= (1 << i)

    return result


def get_page_hash(link):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(link, headers=headers, timeout=10)

        if response.status_code != 200:
            print("Failed to fetch:", link)
            return None

        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text(" ")
        return make_hash(text)

    except Exception as e:
        print("Error fetching:", link)
        print(e)
        return None


if __name__ == "__main__":

    if len(sys.argv) < 3:
        print("Enter two links")
        sys.exit()

    url1 = sys.argv[1]
    url2 = sys.argv[2]

    h1 = get_page_hash(url1)
    h2 = get_page_hash(url2)

    if h1 is None or h2 is None:
        print("Unable to compare pages")
        sys.exit()

    diff = bin(h1 ^ h2).count("1")
    common_bits = 64 - diff
    print("Common bits:", common_bits, "out of 64")
