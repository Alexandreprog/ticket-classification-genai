import pandas as pd


def load_dataset(path):
    df = pd.read_csv(path)
    return df


def sample_dataset(df, n=500, seed=42):
    return df.sample(n=n, random_state=seed)


def train_test_split(df, test_size=200):

    test = df.sample(n=test_size, random_state=42)
    train = df.drop(test.index)

    return train, test