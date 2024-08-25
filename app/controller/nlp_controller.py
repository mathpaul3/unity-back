from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.connection import get_db
from app.service.nlp import get_nlp_result

router = APIRouter()


@router.get("/tokenize")
def tokenize_controller(sentence: str = "안녕하세요. 이것은 수어 번역기입니다.", db: Session = Depends(get_db)) -> dict[str, list[dict[str, str]]]:
    """
    문장을 토큰화하여 반환해주는 함수입니다.
    """
    return get_nlp_result(sentence, db)
