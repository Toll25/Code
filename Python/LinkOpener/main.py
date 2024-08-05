import webbrowser
from urllib.parse import urlparse


def extract_urls(text):
    urls = []
    for word in text.split('"'):
        parsed_url = urlparse(word)
        if parsed_url.scheme and parsed_url.netloc:
            urls.append(word)
    return urls


if __name__ == "__main__":
    file = open("text.txt")
    urls = extract_urls(file.read())
    print(urls)
    for url in urls:
        webbrowser.open(url)
