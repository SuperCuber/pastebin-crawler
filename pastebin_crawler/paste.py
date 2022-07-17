from dataclasses import dataclass, asdict
import arrow
from pymongo.mongo_client import MongoClient

@dataclass
class Pastebin:
    """Represents a pastebin crawled from pastebin.com with all of its associated data"""

    id: str
    title: str | None
    author: str | None
    content: str
    date: arrow.Arrow

    def to_mongo_object(self) -> dict:
        """Transform the dataclass into a dict ready to insert into mongodb"""
        res = asdict(self)
        res["date"] = res["date"].datetime
        return res

class PastebinDb:
    def __init__(self) -> None:
        db = MongoClient("mongodb://db:27017/").crawler
        self.pastes = db.pastes

    def pastebin_exists(self, paste_id: str) -> bool:
        return self.pastes.find_one({"id": paste_id}) is not None

    def save_pastebin(self, paste: Pastebin):
        self.pastes.insert_one(paste.to_mongo_object())
