from typing import List
import requests
import lxml.html as html
import arrow

from .paste import Pastebin

BASE_URL = "https://pastebin.com/"

def crawl(should_crawl=lambda _: True) -> List[Pastebin]:
    """
    Crawl pastebin.com's latest public pastes

    :param should_crawl:
        Optional: a function that takes a paste id and returns
        whether its contents should be crawled
    :returns: a list of Pastebin objects
    """
    response = requests.get(BASE_URL)
    doc = html.document_fromstring(response.text)
    paste_ids = _extract_new_pastes_links(doc)

    pastes = []
    for paste_id in paste_ids:
        if should_crawl(paste_id):
            pastes.append(_crawl_paste(paste_id))
    return pastes

def _extract_new_pastes_links(doc):
    new_posts = doc.cssselect(".sidebar__menu a")
    return [post.attrib["href"][1:]
            for post in new_posts]

def _crawl_paste(paste_id):
    response = requests.get(BASE_URL + paste_id)
    doc = html.document_fromstring(response.text)

    title = doc.cssselect(".info-top h1")[0].text
    author = doc.cssselect(".username a")[0].text
    date = arrow.get(doc.cssselect(".date span")[0].text, "MMM DD[th], YYYY")
    content = requests.get(BASE_URL + "raw/" + paste_id).text
    return Pastebin(id=paste_id, title=title, author=author, date=date, content=content)
