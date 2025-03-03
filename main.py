# ------------------------------------------------------------------------------
# Main
# ------------------------------------------------------------------------------

from fastapi import FastAPI
from routes import question
from routes import answer


app = FastAPI(title="python-samples-fastapi-restful",
              description="🧪 Proof of Concept for a RESTful API made with Python 3 and FastAPI",
              version="1.0.0",)

app.include_router(question.api_router)
app.include_router(answer.api_router)