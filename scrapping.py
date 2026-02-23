import sys
import requests
from bs4 import BeautifulSoup


def take_url(n):
    try:

        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/120.0.0.0 Safari/537.36"
        }

        response = requests.get(n, headers=headers)

        if response.status_code != 200:
            print("Unable to find, here is the status", response.status_code)
            return

        html_content = response.text


        parsing = BeautifulSoup(html_content, "html.parser")


        page_title = parsing.title.string.strip() if parsing.title else "No Title Found"
        print("Page Title:")
        print(page_title)
        print()


        page_body = parsing.get_text(separator="\n").strip()
        print("Page Body:")
        print(page_body)
        print()


        print("URLs Found:")
        all_url_page_points_to = parsing.find_all("a")

        for link in all_url_page_points_to:
            href = link.get("href")
            if href:
                print(href)

    except Exception as e:
        print("Error:", e)



if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("give a url")
    else:
        url = sys.argv[1]
        take_url(url)