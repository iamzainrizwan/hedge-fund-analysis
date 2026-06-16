import numpy as np


def annualised_volatility(returns):
    return returns.std() * np.sqrt(12)


def max_drawdown(returns):
    cumulative = (1 + returns).cumprod()

    peak = cumulative.cummax()

    drawdown = (cumulative - peak) / peak

    return drawdown.min()


def sharpe_ratio(returns):
    return returns.mean() / returns.std()
