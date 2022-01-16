"""InVision - Data visualization."""
import git
import pandas as pd
from matplotlib import pyplot as plt


def plot_time_series(
    data: pd.Series,
    title: str,
    save: bool = False,
    filename: str = "default",
    show: bool = False,
) -> plt.Figure:
    """Plot time series."""
    figure = plt.figure(figsize=(16, 9))
    plt.plot(data)
    plt.title(title)
    plt.xlabel("Time")
    plt.grid(True)

    if save:
        repo: git.Repo = git.Repo(".", search_parent_directories=True)
        root: str = repo.working_tree_dir
        plt.savefig(figure, root + f"plot/{filename}.png")

    if show:
        plt.show()

    plt.close()

    return figure


def main():
    """Main function of the module."""
    pass


if __name__ == "__main__":
    main()
