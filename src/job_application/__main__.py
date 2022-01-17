"""Command-line interface."""
import click
import pandas as pd  # type: ignore

from job_application.InVision import data_preprocessing  # type: ignore
from job_application.InVision import visualization  # type: ignore
from job_application.InVision import weighted_moving_avg  # type: ignore


@click.group()
@click.version_option()
def cli() -> None:
    """Job Application.

    Python package to test the data analysis cases for a job application.
    """


@cli.command()
@click.option("--overview", is_flag=True, help="flag to show the overview of the data.")
@click.option("--moving_average", is_flag=True, help="flag to compute moving average.")
@click.option(
    "--num_obs", type=int, default=5, help="number of observations to make the average."
)
def invision(overview: bool, moving_average: bool, num_obs: int) -> None:
    """Invision forecasting examples."""
    click.echo("InVision")
    data: pd.DataFrame = data_preprocessing._load_data()

    if overview:
        print(data.head())
        visualization.plot_time_series(data, "Original data", show=True)

    if moving_average:
        mv_avg_prediction = weighted_moving_avg.moving_avg_prediction(data, num_obs)
        visualization.plot_moving_avg_one_point_prediction(
            mv_avg_prediction, "Moving Average prediction one point", show=True
        )
