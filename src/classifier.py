from sklearn.linear_model import LogisticRegression


def train_classifier(X, y):

    clf = LogisticRegression(max_iter=1000)

    clf.fit(X, y)

    return clf


def predict_ticket(clf, embedding):

    probs = clf.predict_proba(embedding)[0]

    predicted_class = clf.classes_[probs.argmax()]

    confidence = probs.max()

    return predicted_class