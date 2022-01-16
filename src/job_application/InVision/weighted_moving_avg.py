"""InVision - Weighted Moving Average."""
import pandas as pd


def moving_avg(data: pd.DataFrame, num_obs: int) -> pd.DataFrame:
    """Computes average of the last n observations.

    Args:
        data (pd.DataFrame): series to be analyzed.
        num_obs (int): number of observations to make the average.

    Returns:
        pd.DataFrame: dataframe with the prediction.
    """
    prediction = data.iloc[-num_obs:].mean()
    data.loc[max(data.index) + pd.to_timedelta(1, unit="h")] = prediction

    return data


def main():
    """Main function of the module."""
    pass


if __name__ == "__main__":
    main()
