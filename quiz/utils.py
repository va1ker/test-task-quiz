import requests
from quiz import models, database, core, schemas, crud
from fastapi import Depends
from sqlalchemy.orm import Session
from typing import List


def get_trivia_question(question_num: int) -> list | None:
    params = {"limit": question_num}
    try:
        response = requests.get(core.settings.url, params=params)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


def get_questions_list(trivia_data, db: Session = Depends(database.get_db)) -> list:
    question_ids = [question["id"] for question in trivia_data]
    existing_questions = (
        db.query(models.Question.id)
        .filter(models.Question.question_id.in_(question_ids))
        .all()
    )
    existing_questions_ids = [question["id"] for question in existing_questions]
    questions_to_create = [
        question
        for question in trivia_data
        if question["id"] not in existing_questions_ids
    ]
    return [get_question_object(question) for question in questions_to_create]
     

def get_question_object(
    question_data: schemas.QuestionSchema,
) -> models.Question:
    question = question_data.get("question", {}).get("text")
    answer = question_data.get("correctAnswer")
    question_id = question_data.get("id")
    return models.Question(question=question, anwser=answer, question_id=question_id)


def collect_questions(
    db: Session, number_of_questions: int, questions_to_create: list | None = None
) -> List[models.Question | None]:
    if questions_to_create is None:
        questions_to_create = []
    if number_of_questions == 0:
        return questions_to_create
    trivia_questions = get_trivia_question(question_num=number_of_questions)
    questions_not_in_db = [
        get_question_object(question_data=question) for question in trivia_questions
    ]
    number_of_questions -= len(questions_not_in_db)
    questions_to_create.extend(questions_not_in_db)
    return collect_questions(
        db, number_of_questions, questions_to_create
    ) 
