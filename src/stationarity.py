import pandas as pd
from statsmodels.tsa.api import adfuller

from model import FactorModel


def rolling_betas(
    df: pd.DataFrame, factors: list[str], window: int = 36
) -> pd.DataFrame:
    """computes rolling OLS betas over a sliding window.

    returns a dataframe of beta estimates, one row per window.
    """
    betas = []

    for i in range(window, len(df)):
        window_df = df.iloc[i - window : i]

        model = FactorModel(window_df, factors)
        result = model.fit()
        betas.append(result.params)
    return pd.DataFrame(betas)


def adf_beta_test(betas: pd.Series, factor: str):
    result = adfuller(betas.dropna())

    statistic = result[0]
    p_value = result[1]

    print(f"{factor} beta ADF p-value: {p_value:.4f}")
    if p_value < 0.05:
        print("Conclusion: stationary")
    else:
        print("Conclusion: not stationary")

    return p_value
