from fastapi import APIRouter, Depends, HTTPException, status, Path
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from data.database_connection import generate_async_session
from models.answer_model import AnswerModel
from services.answers_service import retrieve_all_answers_by_id_async

api_router = APIRouter()


@api_router.get(
    "/answers/{question_id}",
    response_model=List[AnswerModel],
    status_code=status.HTTP_200_OK
)

async def get_by_id_async(
    question_id: int = Path(..., title="The ID of the question"),
    async_session: AsyncSession = Depends(generate_async_session)
):
    """
    Endpoint to retrieve a Player by its ID.

    Args:
        player_id (int): The ID of the Player to retrieve.
        async_session (AsyncSession): The async version of a SQLAlchemy ORM session.

    Returns:
        PlayerModel: The Pydantic model representing the matching Player.

    Raises:
        HTTPException: Not found error if the Player with the specified ID does not exist.
    """
    answers = await retrieve_all_answers_by_id_async(async_session, question_id)
    if not answers:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return answers