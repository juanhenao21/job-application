"""InVision - Data pre-processing."""
import git
import pandas as pd


def _load_data() -> pd.DataFrame:
    """Load data to analyze."""
    repository: git.repo.baseRepo = git.Repo(".", search_parent_directories=True)
    root: str = repository.working_tree_dir
    filename: str = root + "/data/ads.csv"
    data: pd.DataFrame = pd.read_csv(filename, index_col=["Time"], parse_dates=["Time"])
    return data


def main():
    """Main function of the module."""
    pass


if __name__ == "__main__":
    main()
