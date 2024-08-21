from sqlalchemy import Column, Integer, String
from db.session import Base


class Word(Base):
    __tablename__ = "word"

    id = Column(Integer, primary_key=True)
    word = Column(String)
    url = Column(String)
