from models import base_model


class QuestionModel(base_model.MainModel):
    """
    Pydantic model representing a question.

    Attributes:
        id (int): The unique identifier for the Player.
        difficulty: str
        category: str
        question: str
        correct_answer: str
    """
    id: int
    difficulty: str
    category: str
    question: str
    correct_answer: str




