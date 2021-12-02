"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Job Application.

    Python package to test the data analysis cases for a job application.
    """

    click.echo("Hello, world!")


if __name__ == "__main__":
    main(prog_name="job-application")  # pragma: no cover
