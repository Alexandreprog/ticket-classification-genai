import pandas as pd


def load_dataset(path: str) -> pd.DataFrame:
    """Load a dataset from a CSV file.

    Args:
        path (str): Path to the CSV dataset.

    Returns:
        pandas.DataFrame: Dataset loaded into a DataFrame.

    Example::
        
        from src.data_prep import load_dataset

        df = load_dataset("tickets.csv")
        
    """

    df = pd.read_csv(path)
    return df


def sample_dataset(
    df: pd.DataFrame,
    n: int = 200,
    num_classes: int = 8,
    seed: int = 42
) -> pd.DataFrame:
    """Create a balanced sample from the dataset.

    This function samples the same number of rows from each class
    in the ``Topic_group`` column in order to create a balanced
    dataset for experimentation or model training.

    The number of samples per class is calculated automatically as:

    n / num_classes

    Args:
        df (pandas.DataFrame): Original dataset containing the tickets.
        n (int, optional): Total number of samples desired in the final dataset.
            Defaults to 200.
        num_classes (int, optional): Number of classes expected in the dataset.
            Defaults to 8.
        seed (int, optional): Random seed used for reproducibility.
            Defaults to 42.

    Returns:
        pandas.DataFrame: Balanced sampled dataset.

    Example::

        from src.data_prep import sample_dataset

        sample = sample_dataset(df)

        sample = sample_dataset(df, n=400, num_classes=8)
        
    """

    samples_per_class = int(n / num_classes)

    sample_df = (
        df.groupby("Topic_group", group_keys=False)
        .apply(lambda x: x.sample(samples_per_class, random_state=seed))
        .reset_index(drop=True)
    )

    print(sample_df["Topic_group"].value_counts())

    return sample_df


def train_test_split(
    df: pd.DataFrame,
    train_ratio: float = 0.7,
    test_ratio: float = 0.3,
    seed: int = 42
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Split a dataset into training and testing sets.

    The dataset is randomly split according to the specified
    training and testing ratios.

    By default the split is:

    - 70% training data
    - 30% testing data

    Args:
        df (pandas.DataFrame): Dataset to split.
        train_ratio (float, optional): Proportion of data used for training.
            Defaults to 0.7.
        test_ratio (float, optional): Proportion of data used for testing.
            Defaults to 0.3.
        seed (int, optional): Random seed for reproducibility.
            Defaults to 42.

    Returns:
        tuple[pandas.DataFrame, pandas.DataFrame]:
            A tuple containing:

            - Training dataset
            - Testing dataset

    Example::
        
        from src.data_prep import train_test_split

        train_df, test_df = train_test_split(df)

        train_df, test_df = train_test_split(df, train_ratio=0.8, test_ratio=0.2)
        
    """

    if train_ratio + test_ratio != 1:
        raise ValueError("train_ratio and test_ratio must sum to 1.")

    test_size = int(len(df) * test_ratio)

    test = df.sample(n=test_size, random_state=seed)
    train = df.drop(test.index)

    print("Train size:", len(train))
    print("Test size:", len(test))

    return train, test