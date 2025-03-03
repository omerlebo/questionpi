# ------------------------------------------------------------------------------
# Schema
# ------------------------------------------------------------------------------

from sqlalchemy import Column, Integer, Text
from data.database_connection import Base


class Answer(Base):
    """
    SQLAlchemy schema describing a database table of football players.

    """

    __tablename__ = "question_answers"

    id = Column(Integer, primary_key=True, autoincrement=True)  
    question_id = Column(Integer, nullable=False)  
    answer = Column(Text, nullable=False)  