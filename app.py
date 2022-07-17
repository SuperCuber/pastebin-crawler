from pastebin_crawler.crawl import crawl
from pastebin_crawler.args import parser
from time import sleep

def main():
    args = parser.parse_args()
    while True:
        crawl()
        sleep(20)

if __name__ == "__main__":
    main()
