# ------------------------------------------------------------------------------
# Model
# ------------------------------------------------------------------------------

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class MainModel(BaseModel):
    """
    Base model configuration for all Pydantic models in the application.

    This class sets a common configuration for alias generation and name population
    for any model that inherits from it. It uses camelCase for JSON field names.

    Attributes:
        model_config (ConfigDict): Configuration for Pydantic models, including:
            alias_generator (function): A function to generate field aliases.
                Here, it uses `to_camel` to convert field names to camelCase.
            populate_by_name (bool): Allows population of fields by name when using Pydantic models.
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)


class QuestionModel(MainModel):
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