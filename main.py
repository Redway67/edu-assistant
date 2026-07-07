from edu_assistant.assistant import create_response


# TODO: поэкспериментировать с разными формулами и выражениями
# PROMPT = "1+2*2"
PROMPT = "Посчитай 1+1/2-0,5-(3/2-3/6)"
# PROMPT = "Упрости выражение: x^2-x(x+1)+2(0.5x-1)+2"

response = create_response(
    llm_key="api",
    role="math_tutor",
    template="tutor_quick_answer",
    prompt=PROMPT,
)

print("-> Ответ ассистента:")
print(response)
