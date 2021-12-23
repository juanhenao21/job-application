"""Test cases for the kaggle_titanic module."""
import pandas as pd
import pytest

from job_application.kaggle_titanic import _load_train_data_kaggle_titanic


@pytest.fixture()
def train_df() -> pd.DataFrame:
    """Train dataset.

    Returns:
        pd.DataFrame: train dataset.
    """
    return _load_train_data_kaggle_titanic()


def test_columns_right_types(train_df):
    """Test if the train df has the right columns types."""
    assert train_df.dtypes["PassengerId"] == pd.Int64Dtype()
    assert train_df.dtypes["Survived"] == pd.Int64Dtype()
    assert train_df.dtypes["Pclass"] == pd.Int64Dtype()
    assert train_df.dtypes["SibSp"] == pd.Int64Dtype()
    assert train_df.dtypes["Parch"] == pd.Int64Dtype()

    assert train_df.dtypes["Age"] == pd.Float64Dtype()
    assert train_df.dtypes["Fare"] == pd.Float64Dtype()

    assert pd.api.types.is_string_dtype(train_df.dtypes["Name"])
    assert pd.api.types.is_string_dtype(train_df.dtypes["Sex"])
    assert pd.api.types.is_string_dtype(train_df.dtypes["Ticket"])
    assert pd.api.types.is_string_dtype(train_df.dtypes["Cabin"])
    assert pd.api.types.is_string_dtype(train_df.dtypes["Embarked"])


# def test_df(train_df):
#     print(train_df.head)
#     print(train_df.columns)
#     print(train_df.dtypes)
#     assert False
