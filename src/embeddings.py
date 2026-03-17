from sentence_transformers import SentenceTransformer

def load_embedding_model():
    """Load a sentence embedding model.

    This function initializes and returns a pre-trained sentence
    transformer model for generating text embeddings. The model
    is configured to run on CPU to ensure compatibility across
    different environments.

    Returns:
        SentenceTransformer: Loaded embedding model configured for CPU usage.

    Example::
        
        from src.embeddings import load_embedding_model

        model = load_embedding_model()
        
    """

    model = SentenceTransformer(
        "all-MiniLM-L6-v2",
        device="cpu"
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


