# edu-assistant

Простой учебный AI-ассистент с ролями, шаблонами системных инструкций и подключением к LLM через OpenAI-compatible API.

## Быстрый старт

Установите зависимости:

```powershell
uv sync
```

Проверьте, что локальная Ollama запущена и нужные модели доступны:

```powershell
ollama list
```

Запустите тестовый сценарий без поднятия настоящего сервера:

```powershell
uv run main.py
```

## REST API

Приложение FastAPI находится в `edu_assistant.api:app`. Благодаря настройке в `pyproject.toml` его можно запустить так:

```powershell
uv run fastapi dev
```

Демо-страница доступна в браузере:

```text
http://127.0.0.1:8000/demo
```

Основной эндпоинт:

```text
POST /ask
```

Он принимает Form-data:

- `role`: роль ассистента, например `math_tutor` или `history_tutor`;
- `template`: шаблон ответа, например `tutor_quick_answer`;
- `question`: вопрос пользователя;
- `llm_key`: ключ модели из `config.yml`, по умолчанию `api`.

## Модели

Модели настраиваются в `config.yml` в секции `llms`. Сейчас доступны ключи:

- `api`: `gpt-5.4-nano`;
- `api_full`: `gpt-5.4`;
- `ollama`: `gemma3:1b`;
- `ollama_small`: `gemma3:270m`.
