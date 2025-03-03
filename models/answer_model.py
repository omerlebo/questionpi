from models import base_model

class AnswerModel(base_model.MainModel):
    id: int
    question_id: int
    answer: str