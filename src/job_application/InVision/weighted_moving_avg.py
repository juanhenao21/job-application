"""InVision - Weighted Moving Average."""
from typing import List

import click
import numpy as np
import pandas as pd


def moving_avg_prediction(data: pd.DataFrame, num_obs: int) -> pd.DataFrame:
    """Computes average of the last n observations.

    A future value of the variable depends on the average of its n previous values.

    Args:
        data (pd.DataFrame): series to be analyzed.
        num_obs (int): number of observations to make the average.

    Returns:
        pd.DataFrame: dataframe with the prediction.
    """
    data_map: pd.DataFrame = data.copy()
    prediction = data_map.iloc[-num_obs:].mean()
    next_date = max(data_map.index) + pd.to_timedelta(1, unit="h")
    data_map.loc[next_date] = prediction

    click.echo(
        f"The predicted value using a moving average for {next_date} is {prediction.values[0]}"
    )

    return data_map


def moving_avg_smoothing(data: pd.DataFrame, window: int) -> pd.DataFrame:
    """Smooths the original time series to identify trends.

    Args:
        data (pd.DataFrame): series to be analyzed.
        window (int): rolling window size.

    Returns:
        pd.DataFrame: smoothed dataframe.
    """
    rolling_mean: pd.DataFrame = data.rolling(window=window).mean()

    return rolling_mean


def weighted_moving_avg_prediction(
    data: pd.DataFrame, weights: List[float]
) -> pd.DataFrame:
    """Computes the weighted average of the last n observations.

    The weights sum up to one with larger weights assigned to more recent observations.

    Args:
        data (pd.DataFrame): series to be analyzed.
        weights (List[float]): weights.

    Returns:
        pd.DataFrame: dataframe with the prediction.
    """
    data_wmap: pd.DataFrame = data.copy()
    np_weights: np.ndarray = np.array(weights)

    num_obs: int = len(weights)
    data_values = data_wmap.iloc[-num_obs:].values.flatten().reshape((3,))
    prediction = np.dot(data_values, np_weights)
    next_date = max(data_wmap.index) + pd.to_timedelta(1, unit="h")
    data_wmap.loc[next_date] = prediction

    click.echo(
        f"The predicted value using a weighted moving average for {next_date} is "
        f"{prediction}"
    )

    return data_wmap


def main():
    """Main function of the module."""
    pass


if __name__ == "__main__":
    main()
