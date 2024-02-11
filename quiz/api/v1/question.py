from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from quiz import crud, schemas, database, utils

router = APIRouter(prefix="/questions", tags=["questions"])


@router.post("/", response_model=schemas.QuestionResponse)
async def process_questions(
    payload: schemas.QuestionPayload, db: Session = Depends(database.get_db)
):
    questions_num = payload.questions_num
    questions_in = utils.collect_questions(number_of_questions=questions_num, db=db)
    print(questions_in)
    crud.crud_question.bulk_create_questions(db=db,questions_data=questions_in)
    last_saved_question = crud.crud_question.get_last_saved_question(db=db)
    return schemas.QuestionResponse(
        message=f"Received {questions_num} questions",
        last_saved_question=schemas.QuestionSchema(
            id=last_saved_question.id,
            question_id=last_saved_question.question_id,
            question=last_saved_question.question,
            answer=last_saved_question.anwser,
            created_at=last_saved_question.created_at,
        ),
    )
