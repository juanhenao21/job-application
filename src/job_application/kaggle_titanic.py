"""Kaggle - Titanic - Machine Learning from Disaster."""
import git
import pandas as pd


def _load_train_data_kaggle_titanic() -> pd.DataFrame:
    """Load train data from the kaggle titanic case.

    Returns:
        pd.DataFrame with the train data.

    Raises:
        FileNotFoundError: check if the file has the right name or is in the right folder.
    """
    try:
        repo = git.Repo(".", search_parent_directories=True)
        root = repo.working_tree_dir
        raw_data: pd.DataFrame = pd.read_csv(f"{root}/data/train.csv")

    except FileNotFoundError as e:
        print("Check if the file has the right name or is in the right folder")
        print(e)
        print()
        raise FileNotFoundError

    raw_data = raw_data.convert_dtypes()

    return raw_data
