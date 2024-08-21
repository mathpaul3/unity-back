from sqlalchemy.orm import Session
from app.model.Word import Word


def get_url_by_word(word: str, db: Session) -> str:
    data = db.query(Word).filter(Word.word == word).first()
    if data is None:
        return ""
    else:
        return data.url
