from openai import OpenAIError
from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import FileResponse, PlainTextResponse

from edu_assistant.assistant import create_response
from edu_assistant.config import RoleType, TemplateType

app = FastAPI()


@app.get("/demo")
def demo():
    return FileResponse("templates/demo.html")


@app.post("/ask", response_class=PlainTextResponse)
def ask(
    role: RoleType = Form(..., description="Роль AI-ассистента"),
    template: TemplateType = Form(..., description="Формат ответа"),
    question: str = Form(
        ...,
        description="Вопрос студента",
        examples=["Что такое число Пи?"],
    ),
    llm_key: str = Form("api", description="Ключ LLM-модели из config.yml"),
) -> str:
    """Ask question to educational assistant."""
    try:
        return create_response(
            llm_key=llm_key,
            role=role,
            template=template,
            prompt=question,
        )
    except OpenAIError as error:
        raise HTTPException(status_code=502, detail=str(error)) from error
    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Не удалось получить ответ ассистента: {error}",
        ) from error
