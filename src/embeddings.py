from sentence_transformers import SentenceTransformer
import torch

def load_embedding_model():

    device = "cuda" if torch.cuda.is_available() else "cpu"

    model = SentenceTransformer(
        "all-MiniLM-L6-v2",
        device=device
    )

    return model


def encode_texts(model, texts):
    return model.encode(texts)


