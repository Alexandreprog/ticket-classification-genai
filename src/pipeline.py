from src.justification import generate_justification
from src.classifier import predict_ticket


def classify_ticket(ticket_text, embedding_model, clf):

    emb = embedding_model.encode([ticket_text])

    predicted_class = predict_ticket(clf, emb)

    justification = generate_justification(
        ticket_text,
        predicted_class
    )

    return {
        "classe": predicted_class,
        "justificativa": justification
    }