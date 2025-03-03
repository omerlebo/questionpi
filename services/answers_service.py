from schemas.answer_schema import Answer
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


async def retrieve_all_answers_by_id_async(async_session: AsyncSession, question_id: int):
    """
    Retrieves a Player by its ID from the database.

    Args:
        async_session (AsyncSession): The async version of a SQLAlchemy ORM session.
        player_id (int): The ID of the Player to retrieve.

    Returns:
        The Player matching the provided ID, or None if not found.
    """
    stmt = select(Answer).where(Answer.question_id == question_id).limit(4)
    result = await async_session.execute(stmt)
    items = result.scalars().all()
    return items