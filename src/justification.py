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

    Example::

        from src.justification import generate_justification

        explanation = generate_justification(
            "Cannot connect to VPN",
            "network_issue"
        )

        print(explanation)
        
    """

    prompt = f"""
    You are an IT support specialist.

    Ticket:
    {ticket}

    Predicted class: {classe}

    Explain in at most 2 sentences why this ticket belongs to this class.
    Highlight words or evidence from the text.
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