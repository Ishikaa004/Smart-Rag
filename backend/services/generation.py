import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

current_dir = Path(__file__).resolve().parent
dotenv_path = current_dir.parent / ".env"
load_dotenv(dotenv_path=dotenv_path)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_answer(question, context):
    context_text = "\n".join(context)

    prompt = f"""
You are a helpful AI assistant.

Use ONLY the context below.

Context:
{context_text}

Question:
{question}

Answer clearly:
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    print(response)  # Debug

    return response.choices[0].message.content