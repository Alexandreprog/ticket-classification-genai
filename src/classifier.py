import joblib
from sklearn.linear_model import LogisticRegression


def load_classifier(path="models/classifier.joblib"):
    """Load a trained classification model from disk.

    This function loads a previously trained machine learning model
    using joblib. The model is expected to be saved in the specified path.

    Args:
        path (str): Path to the saved model file. Defaults to
            "models/classifier.joblib".

    Returns:
        object: Loaded classifier model.

    Example::
        
        from src.classifier import load_classifier

        clf = load_classifier()
        
    """
    return joblib.load(path)

def train_classifier(X, y):
    """Train a ticket classification model using Logistic Regression.

    Args:
        X (array-like): Feature matrix containing the embeddings of the tickets.
        y (array-like): Target labels corresponding to each ticket.

    Returns:
        LogisticRegression: A trained Logistic Regression classifier.

    Example::
        
        from src.classifier import train_classifier

        clf = train_classifier(X_train, y_train)
        
    """

    clf = LogisticRegression(max_iter=1000)

    clf.fit(X, y)

    return clf


def predict_ticket(clf, embedding):
    """Predict the class of a ticket using a trained classifier.

    Args:
        clf (LogisticRegression): Trained classification model.
        embedding (array-like): Embedding vector representing the ticket text.

    Returns:
        str: The predicted ticket class.

    Example::

        from src.classifier import predict_ticket

        predicted_class = predict_ticket(clf, embedding)
        print(predicted_class)
        
    """

    probs = clf.predict_proba(embedding)[0]

    predicted_class = clf.classes_[probs.argmax()]

    return predicted_class