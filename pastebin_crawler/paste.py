from datetime import datetime
from dataclasses import dataclass

@dataclass
class Pastebin:
    title: str
    author: str
    content: str
    date: datetime
