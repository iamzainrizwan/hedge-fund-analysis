import pandas as pd
from statsmodels.tsa.api import adfuller

from model import FactorModel


def rolling_betas(df, factors, window=36):
    betas = []

    for i in range(window, len(df)):
        window_df = df.iloc[i - window : i]

        model = FactorModel(window_df, factors)
        result = model.fit()
        betas.append(result.params)
    return pd.DataFrame(betas)


def adf_beta_test(betas, factor):
    result = adfuller(betas.dropna())

    statistics = result[0]
    p_value = result[1]

    print(f"{factor} beta ADF p-value: {p_value:.4f}")
    if p_value < 0.05:
        print("Conclusion: stationary")
    else:
        print("Conclusion: not stationary")

    return p_value
