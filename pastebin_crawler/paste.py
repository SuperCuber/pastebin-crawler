from dataclasses import dataclass
import arrow

@dataclass
class Pastebin:
    id: str
    title: str
    author: str
    content: str
    date: arrow.Arrow
