import statsmodels.api as sm

import config


class FactorModel:
    def __init__(self, df, factor_cols=config.FACTOR_COLS) -> None:
        self.y = df[config.TARGET_COL]
        self.X = df[factor_cols]
        self.X = sm.add_constant(self.X)
        self.result = None

    def fit(self):
        self.result = sm.OLS(self.y, self.X).fit()
        return self.result
