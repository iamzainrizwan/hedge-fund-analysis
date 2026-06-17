import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.stats.diagnostic import het_breuschpagan


def evaluate_model(results) -> dict[str, float]:
    """retirms key fit statistics from an OLS result: R^2, adjusted R^2. F-stat, F p-value"""
    metrics = {
        "R^2": results.rsquared,
        "Adjusted R^2": results.rsquared_adj,
        "F-stat": results.fvalue,
        "F p-value": results.f_pvalue,
    }

    return metrics


def plot_residuals(results) -> None:
    """plots residuals vs predicted values and saves to plots/residuals.png."""
    plt.scatter(results.fittedvalues, results.resid)
    plt.axhline(0, color="red")
    plt.xlabel("Predicted")
    plt.ylabel("Residuals")
    plt.title("Residuals vs Predicted")
    plt.savefig("plots/residuals.png")
    plt.close()


def plot_qq(results) -> None:
    """plots a Q-Q plot of regression residuals and saves to plots/qq_plot.png."""
    plt.figure(figsize=(6, 6))
    sm.qqplot(results.resid, line="45", fit=True)
    plt.title("Q-Q Plot of Regression Residuals")
    plt.savefig("plots/qq_plot.png")


def test_heteroskedasticity(model):

    result = het_breuschpagan(model.resid, model.model.exog)
    lm_stat, lm_pvalue, f_stat, f_pvalue = result

    return lm_pvalue
