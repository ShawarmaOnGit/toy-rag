from openai import OpenAI, OpenAIError

client = OpenAI()

def generate_answer(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )

        answer = response.choices[0].message.content
        
        if not answer:
            raise ValueError("Model returned no answer")
        
        return answer

    except OpenAIError:
        raise