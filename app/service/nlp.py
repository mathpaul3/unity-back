from repository.nlp import get_url_by_word
from sqlalchemy.orm import Session
from konlpy.tag import Okt


tokenizer = Okt()


def get_nlp_result(sentence: str, db: Session) -> list[dict[str, str]]:
    results = list()
    words = tokenizer.pos(sentence, norm=True)
    filter = ["Alpha", "Foreign", "Hashtag", "Josa", "ScreenName"]

    PREFIX = "http://sldict.korean.go.kr/multimedia/multimedia_files/convert/"
    POSTFIX = "_700X466.webm"
    for (word, tag) in words:
        url = "" if tag in filter else get_url_by_word(word, db)
        results.append({
            "word": word,
            "url": f"{PREFIX}{url}{POSTFIX}" if url else ""
        })
    return results
