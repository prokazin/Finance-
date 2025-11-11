import openai
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")

def get_budget_advice(chat_id):
    prompt = "Дай 3 совета, как лучше управлять бюджетом пользователя."
    try:
        resp = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role":"system","content":"Ты финансовый консультант"},{"role":"user","content":prompt}],
            max_tokens=250
        )
        return resp.choices[0].message.content.strip()
    except:
        return "Ошибка AI"
