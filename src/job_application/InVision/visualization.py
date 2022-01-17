"""InVision - Data visualization."""
import git
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.metrics import mean_absolute_error


def plot_time_series(
    data: pd.DataFrame,
    title: str,
    save: bool = False,
    filename: str = "default",
    show: bool = False,
) -> plt.Figure:
    """Plot time series.

    Args:
        data (pd.DataFrame): data to be plotted.
        title (str): title of the figure.
        save (bool): flag to save the plot.
        filename (str): filename.
        show (bool): flag to show the plot.

    Returns:
        plt.Figure: the figure with the time series.
    """
    figure = plt.figure(figsize=(16, 9))
    plt.plot(data)
    plt.title(title)
    plt.xlabel("Time")
    plt.grid(True)

    if save:
        repository: git.repo.base.Repo = git.Repo(".", search_parent_directories=True)
        root: str = repository.working_tree_dir
        plt.savefig(figure, root + f"plot/{filename}.png")

    if show:
        plt.show()

    plt.close()

    return figure


def plot_moving_avg_one_point_prediction(
    data: pd.DataFrame,
    title: str,
    save: bool = False,
    filename: str = "default",
    show: bool = False,
) -> plt.Figure:
    """Plot time series.

    Args:
        data (pd.DataFrame): data to be plotted.
        title (str): title of the figure.
        save (bool): flag to save the plot.
        filename (str): filename.
        show (bool): flag to show the plot.

    Returns:
        plt.Figure: the figure with the time series.
    """
    figure = plt.figure(figsize=(16, 9))
    plt.plot(data[:-1])
    plt.plot(data[-1:], "ro", markersize=10)
    plt.title(title)
    plt.xlabel("Time")
    plt.grid(True)

    if save:
        repository: git.repo.base.Repo = git.Repo(".", search_parent_directories=True)
        root: str = repository.working_tree_dir
        plt.savefig(figure, root + f"plot/{filename}.png")

    if show:
        plt.show()

    plt.close()

    return figure


def plot_moving_avg_smoothing(
    original_data: pd.DataFrame,
    rolling_data: pd.DataFrame,
    window: int,
    title: str,
    scale: float = 1.96,
    plot_intervals: bool = False,
    plot_anomalies: bool = False,
    save: bool = False,
    filename: str = "default",
    show: bool = False,
) -> plt.Figure:
    """Plot time series.

    Args:
        original_data (pd.DataFrame): original data.
        rolling_data (pd.DataFrame): rolling data.
        window (int): window used to smooth the time series.
        title (str): title of the figure.
        scale (float): scale for the standard deviation to be used.
        plot_intervals (bool): plot confidence intervals.
        plot_anomalies (bool): plot anomalies.
        save (bool): flag to save the plot.
        filename (str): filename.
        show (bool): flag to show the plot.

    Returns:
        plt.Figure: the figure with the time series.
    """
    figure = plt.figure(figsize=(16, 9))
    plt.title(title + f" window size {window}")
    plt.xlabel("Time")
    plt.grid(True)

    plt.plot(rolling_data, "g", label="Rolling mean trend")
    plt.plot(original_data, label="Actual values")

    # Plot confidence intervals for smoothed values
    if plot_intervals:
        mean_abs_error = mean_absolute_error(
            original_data[window:], rolling_data[window:]
        )
        deviation = (original_data[window:] - rolling_data[window:]).std()
        lower_bond = rolling_data - (mean_abs_error + scale * deviation)
        upper_bond = rolling_data + (mean_abs_error + scale * deviation)
        plt.plot(upper_bond, "r--", label="Upper Bond / Lower Bond")
        plt.plot(lower_bond, "r--")

        # Having the intervals, find abnormal values
        if plot_anomalies:
            anomalies = pd.DataFrame(
                index=original_data.index, columns=original_data.columns
            )
            anomalies[original_data < lower_bond] = original_data[
                original_data < lower_bond
            ]
            anomalies[original_data > upper_bond] = original_data[
                original_data > upper_bond
            ]
            plt.plot(anomalies, "ro", markersize=10)

    plt.legend(loc="upper left")

    if save:
        repository: git.repo.base.Repo = git.Repo(".", search_parent_directories=True)
        root: str = repository.working_tree_dir
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
