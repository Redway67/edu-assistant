from typing import Annotated

from fastapi import Body, FastAPI, Form, HTTPException
from fastapi.responses import PlainTextResponse

from edu_assistant.assistant import create_response
from edu_assistant.config import RoleType, TemplateType

app = FastAPI()


@app.post("/assistant", response_class=PlainTextResponse)
def create_assistant_response(
    llm_key: str = Body(...),
    role: RoleType = Body(...),
    template: TemplateType = Body(...),
    prompt: str = Body(...),
) -> str:
    return create_response(
        llm_key=llm_key,
        role=role,
        template=template,
        prompt=prompt,
    )


@app.post("/ask", response_class=PlainTextResponse)
def ask(
    role: Annotated[
        RoleType,
        Form(description="Роль AI-ассистента из конфигурации."),
    ],
    template: Annotated[
        TemplateType,
        Form(description="Шаблон системной инструкции для ответа."),
    ],
    # Вопрос пользователя, который будет передан ассистенту.
    question: Annotated[
        str,
        Form(
            description="Вопрос пользователя для AI-ассистента.",
            examples=["Что такое число Пи?"],
        ),
    ],
    llm_key: Annotated[
        str,
        Form(description="Ключ LLM-модели из секции llms в config.yml."),
    ] = "api",
) -> str:
    try:
        return create_response(
            llm_key=llm_key,
            role=role,
            template=template,
            prompt=question,
        )
    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Не удалось получить ответ ассистента: {error}",
        ) from error
