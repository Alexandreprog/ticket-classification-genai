from sentence_transformers import SentenceTransformer
import torch

def load_embedding_model():
    """Load a sentence embedding model.

    The model will automatically use GPU if available,
    otherwise it will run on CPU.

    Returns:
        SentenceTransformer: Loaded embedding model.

    Example::
        
        from src.embeddings import load_embedding_model

        model = load_embedding_model()
        
    """

    device = "cuda" if torch.cuda.is_available() else "cpu"

    model = SentenceTransformer(
        "all-MiniLM-L6-v2",
        device=device
    )

    return model


def encode_texts(model, texts):
    """Generate embeddings for a list of texts.

    Args:
        model (SentenceTransformer): Preloaded embedding model.
        texts (list[str]): List of text inputs to encode.

    Returns:
        numpy.ndarray: Array of embeddings representing the texts.

    Example::
        
        from src.embeddings import encode_texts

        embeddings = encode_texts(model, ["Example ticket"])
        
    """

    return model.encode(texts)


