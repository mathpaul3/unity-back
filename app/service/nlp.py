from sqlalchemy.orm import Session
from konlpy.tag import Okt
from app.repository.nlp import get_url_by_word


tokenizer = Okt()


def get_nlp_result(sentence: str, db: Session) -> dict[str, list[dict[str, str]]]:
    results: dict[str, list] = dict()
    words = tokenizer.pos(sentence, norm=True)
    filter = ["Alpha", "Foreign", "Hashtag",
              "Josa", "Punctuation", "ScreenName"]

    PREFIX = "http://sldict.korean.go.kr/multimedia/multimedia_files/convert/"
    POSTFIX = "_700X466.webm"
    for (word, tag) in words:
        if tag not in filter:
            if tag not in results:
                results[tag] = []
            url = get_url_by_word(word, db)
            results[tag].append({
                "word": word,
                "url": f"{PREFIX}{url}{POSTFIX}" if url else ""
            })
    return results
