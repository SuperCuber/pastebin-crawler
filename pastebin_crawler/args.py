import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description="Continuously crawl pastebin for new pastes"
    )
    parser.add_argument("--once", action="store_true", help="Crawl only once")
    parser.add_argument("--interval", type=int, help="The interval between crawls in seconds", default=120)
    parser.add_argument("--quiet", "-q", action="store_true", help="Disable logging")

    args = parser.parse_args()
    if not args.quiet and not args.once:
        print(f"Crawling pastebin.com every {args.interval} seconds.")
    return args
