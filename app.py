from pastebin_crawler.crawl import crawl
from pastebin_crawler.args import parse_args
from time import sleep

def main():
    args = parse_args()
    if args.once:
        pastes = crawl()
        print(len(pastes))
        return

    while True:
        pastes = crawl()
        print(len(pastes))
        sleep(args.interval)

if __name__ == "__main__":
    main()
