"""Command-line interface."""
import click
import pandas as pd

from job_application.InVision import data_preprocessing
from job_application.InVision import visualization

# from job_application.InVision import weighted_moving_avg


@click.group()
@click.version_option()
def cli() -> None:
    """Job Application.

    Python package to test the data analysis cases for a job application.
    """


@cli.command()
@click.option("--overview", is_flag=True)
def invision(overview: bool) -> None:
    """Invision forecasting examples.

    Args:
        overview: flag to show the overview of the data.
    """
    click.echo("InVision")
    if overview:
        data: pd.DataFrame = data_preprocessing._load_data()
        print(data.head())
        visualization.plot_time_series(data, "Original data")
