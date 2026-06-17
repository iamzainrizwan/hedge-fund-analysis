import pandas as pd

import config


def load_data() -> pd.DataFrame:
    """loads raw returns data from configured excel path."""
    df = pd.read_excel(config.DATA_PATH)
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """cleans the raw dataframe.

    - parses and sorts dates
    - removes observation where factor return exceeds magnitude threshold (|x| > 2)
    """
    # keep only required cols
    cols = [config.DATE_COL, config.TARGET_COL] + config.FACTOR_COLS
    df = df[cols].copy()

    # date parsing and sorting
    df[config.DATE_COL] = pd.to_datetime(df[config.DATE_COL])
    df.sort_values(config.DATE_COL)

    # remove outliers
    threshold = 2
    factor_data = df[config.FACTOR_COLS]

    bad_rows = (factor_data.abs() > threshold).any(axis=1)
    df = df.loc[~bad_rows].copy()

    df = df.reset_index(drop=True)

    return df
