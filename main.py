import os
import openai

openai.api_key = "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"
openai.base_url = "https://openrouter.ai/api/v1"

response = openai.chat.completions.create(
        messages=[{"role": "user", "content": "Hi!"}],
        model="openai/gpt-4o-mini",
)

print(response.choices[0].message.content)
