"""InVision - Weighted Moving Average."""
import click
import pandas as pd


def moving_avg_prediction(data: pd.DataFrame, num_obs: int) -> pd.DataFrame:
    """Computes average of the last n observations.

    Args:
        data (pd.DataFrame): series to be analyzed.
        num_obs (int): number of observations to make the average.

    Returns:
        pd.DataFrame: dataframe with the prediction.
    """
    prediction = data.iloc[-num_obs:].mean()
    next_date = max(data.index) + pd.to_timedelta(1, unit="h")
    data.loc[next_date] = prediction

    click.echo(
        f"The predicted value using a moving average for {next_date} is {prediction.values[0]}"
    )

    return data


def main():
    """Main function of the module."""
    pass


if __name__ == "__main__":
    main()
