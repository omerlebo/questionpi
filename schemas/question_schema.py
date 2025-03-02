# ------------------------------------------------------------------------------
# Schema
# ------------------------------------------------------------------------------

from sqlalchemy import Column, String, Integer, Text
from data.question_database import Base


class Question(Base):
    """
    SQLAlchemy schema describing a database table of football players.

    """

    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, autoincrement=True)  # Primary Key with serial auto-increment
    difficulty = Column(String(10), nullable=False)  # Difficulty column (varchar(10))
    category = Column(String(50), nullable=False)  # Category column (varchar(50))
    question = Column(Text, nullable=False)  # Question column (text)
    correct_answer = Column(Text, nullable=False)  # Correct answer column (text)