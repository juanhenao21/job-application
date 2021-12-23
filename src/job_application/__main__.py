"""Command-line interface."""
import click

from job_application import kaggle_titanic


@click.command()
@click.version_option()
@click.option(
    "--kaggle",
    type=bool,
    default=False,
    help="Boolean, True to select the Kaggle Titanic dataset.",
)
def main(kaggle: bool) -> None:
    """Job Application.

    Python package to test the data analysis cases for a job application.

    Args:
        kaggle (bool): True to select the Kaggle Titanic dataset.
    """
    if kaggle:
        train_df = kaggle_titanic._load_train_data_kaggle_titanic()
        print(train_df.head())


if __name__ == "__main__":
    main(prog_name="job-application")  # pragma: no cover
