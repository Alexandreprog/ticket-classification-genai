import os
from groq import Groq

from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_justification(ticket, classe):
    """Generate a natural language justification for a predicted ticket class.

    This function uses a large language model to explain why a given
    ticket was classified into a specific category.

    Args:
        ticket (str): The original ticket text.
        classe (str): Predicted ticket category.

    Returns:
        str: A short explanation describing why the ticket belongs to the predicted class.

    Example:
        ```python
        from src.justification import generate_justification

        explanation = generate_justification(
            "Cannot connect to VPN",
            "network_issue"
        )

        print(explanation)
        ```
    """

    prompt = f"""
    Você é um especialista em suporte de TI.

    Ticket:
    {ticket}

    Classe prevista: {classe}

    Explique em no máximo 2 frases por que esse ticket pertence a essa classe.
    Destaque palavras ou evidências do texto.
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0,
        max_tokens=80
    )

    return response.choices[0].message.content