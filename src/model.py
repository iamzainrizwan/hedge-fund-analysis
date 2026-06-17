import statsmodels.api as sm

import config


class FactorModel:
    """OLD factor omdel for hedge fund return decomposition

    fits the regression R_t = alpha + sum(beta_i * F_i_t) + epsilon_t
    """

    def __init__(self, df, factor_cols=config.FACTOR_COLS) -> None:
        self.y = df[config.TARGET_COL]
        self.X = df[factor_cols]
        self.X = sm.add_constant(self.X)
        self.result = None

    def fit(self):
        """fits the OLS model and returns the results object"""
        self.result = sm.OLS(self.y, self.X).fit()
        return self.result
