
from schemas.question_schema import Question
from sqlalchemy.ext.asyncio import AsyncSession

async def retrieve_by_id_async(async_session: AsyncSession, question_id: int):
    """
    Retrieves a Player by its ID from the database.

    Args:
        async_session (AsyncSession): The async version of a SQLAlchemy ORM session.
        player_id (int): The ID of the Player to retrieve.

    Returns:
        The Player matching the provided ID, or None if not found.
    """
    question = await async_session.get(Question, question_id)
    return question