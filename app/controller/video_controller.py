from fastapi import APIRouter


router = APIRouter()


@router.get("/")
def video_controller() -> None:
    """
    전달받은 토큰에 담긴 단어에 해당하는 수어 영상을 이어붙여 반환하는 함수입니다.
    """
    return
