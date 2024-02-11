from pydantic import BaseModel
from datetime import datetime

class QuestionPayload(BaseModel):
    questions_num: int

class QuestionSchema(BaseModel):
    id: int
    question: str
    answer: str
    question_id: str
    created_at: datetime

class QuestionResponse(BaseModel):
    status: str = "success"
    message: str
    last_saved_question: QuestionSchema | None
