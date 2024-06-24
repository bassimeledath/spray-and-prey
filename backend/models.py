from constants import SYSTEM_PROMPT
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()


class Model:
    def __init__(self):
        self.openai = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    def generate_text(self, prompt, model="gpt-4o"):
        completion = self.openai.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ],
            max_tokens=80,
            temperature=0.0
        )
        return completion.choices[0].message.content
