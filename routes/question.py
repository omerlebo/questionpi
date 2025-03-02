from fastapi import APIRouter, Depends, HTTPException, status, Path
from sqlalchemy.ext.asyncio import AsyncSession

from data.question_database import generate_async_session
from models.quetion_model import QuestionModel
from services import question_service

api_router = APIRouter()


@api_router.get(
    "/question/{question_id}",
    response_model=QuestionModel,
    status_code=status.HTTP_200_OK,
    summary="Retrieves a Player by its Id",
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
    question = await question_service.retrieve_by_id_async(async_session, question_id)
    if not question:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return question