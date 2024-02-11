from .question import router as question_router
from fastapi import APIRouter


router = APIRouter()
router.include_router(question_router)
