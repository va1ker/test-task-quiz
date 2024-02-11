from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, func

from .base import Base


class Question(Base):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    question = Column(String, unique=True)
    anwser = Column(String)
    ## Cache
    question_id = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow, server_default=func.now())
