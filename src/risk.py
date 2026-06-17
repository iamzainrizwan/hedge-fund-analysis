import numpy as np
import pandas as pd


def annualised_volatility(returns: pd.Series) -> float:
    """returns annualised volatility, assuming monthly returns."""
    return returns.std() * np.sqrt(12)


def max_drawdown(returns: pd.Series) -> float:
    """returns maximum peak to trough drawdown of a return series."""
    cumulative = (1 + returns).cumprod()

    peak = cumulative.cummax()

    drawdown = (cumulative - peak) / peak

    return drawdown.min()


def sharpe_ratio(returns: pd.Series) -> float:
    """returns the sharpe ratio, assuming a risk-free rate of zero."""
    return returns.mean() / returns.std()
