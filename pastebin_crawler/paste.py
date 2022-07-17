from dataclasses import dataclass
import arrow

@dataclass
class Pastebin:
    title: str
    author: str
    content: str
    date: arrow.Arrow
