import requests
import lxml.html as html
import arrow

from .paste import Pastebin

BASE_URL = "https://pastebin.com"

def crawl():
    response = requests.get(BASE_URL + "/")
    doc = html.document_fromstring(response.text)
    pastes = extract_new_pastes_links(doc)
    print(pastes)

    for paste_url in pastes:
        crawl_paste(paste_url)

def extract_new_pastes_links(doc):
    new_posts = doc.cssselect(".sidebar__menu a")
    return [post.attrib["href"] for post in new_posts]

def crawl_paste(paste_url):
    response = requests.get(BASE_URL + paste_url)
    doc = html.document_fromstring(response.text)

    title = doc.cssselect(".info-top h1")[0].text
    author = doc.cssselect(".username a")[0].text
    date = arrow.get(doc.cssselect(".date span")[0].text, "MMM DD[th], YYYY")
    content = requests.get(BASE_URL + "/raw" + paste_url).text
    print(Pastebin(title=title, author=author, date=date, content=content))
