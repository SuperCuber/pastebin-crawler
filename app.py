"""
The entry point of the application.
Uses the pastebin_crawler package to crawl pastebin.com according to given command line args.
"""

from pastebin_crawler.crawl import crawl
from pastebin_crawler.args import parse_args
from pastebin_crawler.paste import PastebinDb
from time import sleep

def main():
    args = parse_args()
    db = PastebinDb()
    while True:
        crawl_latest(db, not args.quiet)
        if args.once: break
        sleep(args.interval)

def crawl_latest(db: PastebinDb, log: bool):
    if log: print("Crawling...")
    pastes = crawl(lambda id: not db.pastebin_exists(id))
    if log: print(f"Found {len(pastes)} new pastes")

    for paste in pastes:
        db.save_pastebin(paste)

if __name__ == "__main__":
    main()
