from openai import OpenAI, OpenAIError
import logging

logger = logging.getLogger(__name__)

client = OpenAI()

GENERATION_MODEL = "gpt-4o-mini"
TEMPERATURE = 0

def generate_answer(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model=GENERATION_MODEL,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=TEMPERATURE
        )

        answer = response.choices[0].message.content

        if not answer:
            raise ValueError("Model returned no answer")
        
        return answer

    except OpenAIError as e:
        logger.error(f"Generation failed: {e}")
        raise