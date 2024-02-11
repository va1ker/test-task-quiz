from sqlalchemy.orm import Session
from quiz import models, schemas
from typing import List

class QuestionCRUD:

    # TODO: no use found, we need to pass pydantic model here
    def create_question(self, db: Session, question_data: schemas.QuestionSchema):
        question = models.Question(**question_data)
        db.add(question)
        db.commit()
        db.refresh(question)
        return question

    def get_question(self, db: Session, question_id: int):
        return (
            db.query(models.Question)
            .filter(models.Question.id == question_id)
            .first()
        )

    def get_questions(self, db: Session, skip: int = 0, limit: int = 10):
        return db.query(models.Question).offset(skip).limit(limit).all()


    def delete_question(self, db: Session, question_id: int):
        question = (
            db.query(models.Question)
            .filter(models.Question.id == question_id)
            .first()
        )
        db.delete(question)
        db.commit()

    def get_last_saved_question(self,db: Session):
        return (
            db.query(models.Question).order_by(models.Question.id.desc()).first()
        )
    
    def bulk_create_questions(self, db: Session, questions_data: List[schemas.QuestionSchema]):
        db.add_all(questions_data)
        db.commit()
        return questions_data


crud_question = QuestionCRUD()
