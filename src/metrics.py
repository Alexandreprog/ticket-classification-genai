from sklearn.metrics import classification_report


def evaluate_model(y_true, y_pred):
    """Evaluate classification performance using standard metrics.

    Args:
        y_true (array-like): True labels.
        y_pred (array-like): Predicted labels.

    Returns:
        str: Text summary containing precision, recall, f1-score, and support.

    Example::
        
        from src.metrics import evaluate_model

        report = evaluate_model(y_true, y_pred)
        print(report)
        
    """

    report = classification_report(y_true, y_pred)

    return report