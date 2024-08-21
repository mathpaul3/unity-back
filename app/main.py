from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from controller import nlp_controller, video_controller

origins = [
    "http://127.0.0.1:3000",
]


def createApp() -> FastAPI:
    _app = FastAPI()

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    _app.include_router(nlp_controller.router, prefix="/nlp")
    _app.include_router(video_controller.router, prefix="/video")
    return _app


app = createApp()
