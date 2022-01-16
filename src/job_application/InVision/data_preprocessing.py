"""InVision - Data pre-processing."""
import git
import pandas as pd


def _load_data() -> pd.DataFrame:
    """Load data to analyze."""
    repo: git.Repo = git.Repo(".", search_parent_directories=True)
    root: str = repo.working_tree_dir
    data: pd.DataFrame = pd.read_csv(
        root + "/data/ads.csv", index_col=["Time"], parse_dates=["Time"]
    )
    return data


def main():
    """Main function of the module."""
    pass


if __name__ == "__main__":
    main()
