"""Command-line interface."""
import click


@click.group()
@click.version_option()
def cli() -> None:
    """Job Application.

    Python package to test the data analysis cases for a job application.
    """


@cli.command()
@click.option("--summary", is_flag=True)
def invision(summary: bool) -> None:
    """Invision forecasting examples.

    Args:
        summary: flag to show the summary of the data
    """
    click.echo("InVision")
    if summary:
        print("Holi")
