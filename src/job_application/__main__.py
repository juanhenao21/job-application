"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Job Application."""


if __name__ == "__main__":
    main(prog_name="job-application")  # pragma: no cover
