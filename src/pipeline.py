from src.justification import generate_justification
from src.classifier import predict_ticket


def classify_ticket(ticket_text, embedding_model, clf):
    """Classify a support ticket and generate a justification.

    The function generates an embedding for the ticket,
    predicts its class using a trained classifier,
    and produces a natural language explanation for the prediction.

    Args:
        ticket_text (str): Raw text of the support ticket.
        embedding_model (SentenceTransformer): Loaded embedding model.
        clf (LogisticRegression): Trained classification model.

    Returns:
        dict: Dictionary containing the predicted class and its justification.

    Example::
        
        from src.pipeline import classify_ticket

        result = classify_ticket(
            "VPN connection fails when logging in",
            embedding_model,
            clf
        )

        print(result["classe"])
        print(result["justificativa"])
        
    """

    emb = embedding_model.encode([ticket_text])

    predicted_class = predict_ticket(clf, emb)

    justification = generate_justification(
        ticket_text,
        predicted_class
    )

    return {
        "class": predicted_class,
        "justification": justification
    }